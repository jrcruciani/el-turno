"""Pruebas aisladas del renderizador: importan build.py sin construir el sitio.

    python3 -m unittest discover -s tests
"""
import importlib.util
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("turno_build", ROOT / "build.py")
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)  # solo define funciones; build() no se llama


class Links(unittest.TestCase):
    def test_normal_links(self):
        self.assertEqual(b.md_inline("[a](https://x.org/p)"), '<a href="https://x.org/p">a</a>')
        self.assertEqual(b.md_inline("[a](/p/x.html)"), '<a href="/p/x.html">a</a>')
        self.assertEqual(b.md_inline("[a](#nota)"), '<a href="#nota">a</a>')
        self.assertEqual(b.md_inline("[a](mailto:x@y.org)"), '<a href="mailto:x@y.org">a</a>')
        self.assertIn('href="HTTPS://X.org"', b.md_inline("[a](HTTPS://X.org)"))

    def test_ampersand_query(self):
        self.assertEqual(b.md_inline("[a](https://x.org/?a=1&b=2)"),
                         '<a href="https://x.org/?a=1&amp;b=2">a</a>')

    def test_quotes_cannot_break_attribute(self):
        out = b.md_inline('[a](https://x.org/"onmouseover="alert(1))')
        self.assertNotIn('" onmouseover', out)
        self.assertNotIn('"onmouseover="', out)
        self.assertIn("&quot;onmouseover=&quot;", out)
        out = b.md_inline("[a](https://x.org/'x=1)")
        self.assertIn("&#x27;", out)

    def test_formatting_does_not_touch_href(self):
        out = b.md_inline("[a](https://x.org/*b*c*) *em*")
        self.assertIn('href="https://x.org/*b*c*"', out)
        self.assertIn("<em>em</em>", out)

    def test_forbidden_schemes(self):
        for u in ["javascript:alert(1)", "JaVaScRiPt:alert(1)", "vbscript:msgbox",
                  "data:text/html,x", "file:///etc/passwd", "foo:bar",
                  "java\x00script:x", "\x01javascript:x", "java\x7fscript:x"]:
            with self.subTest(u=u), self.assertRaises(b.UnsafeContent):
                b.md_inline(f"[a]({u})")

    def test_whitespace_or_entities_never_yield_executable_href(self):
        # con espacios no se forma enlace; con entidades, el & se escapa y el
        # navegador lo lee como ruta relativa literal
        for u in ["java\tscript:alert(1)", "java\u2028script:x",
                  "javascript&#58;alert(1)", "&#x6A;avascript:x", "\u00a0javascript:x"]:
            out = b.md_inline(f"[a]({u})")
            with self.subTest(u=u):
                self.assertNotRegex(out, r'href="\s*javascript:')
                if "<a " in out:
                    self.assertIn("&amp;", out)

    def test_safe_url_rejects_unicode_space(self):
        for u in ["\u00a0javascript:x", "java\u3000script:x", "\u200bjavascript:x"]:
            with self.subTest(u=u), self.assertRaises(b.UnsafeContent):
                b.safe_url(u)

    def test_entity_lookalike_is_not_decoded(self):
        # sin esquema real => se trata como ruta relativa literal, inofensiva
        out = b.md_inline("[a](&#106;avascript:x)")
        self.assertNotIn("javascript", out)

    def test_md_to_html_and_rss_share_validation(self):
        with self.assertRaises(b.UnsafeContent):
            b.md_to_html("| h |\n|---|\n| [x](javascript:1) |")
        with self.assertRaises(b.UnsafeContent):
            b.md_to_html("- [x](javascript:1)")


class Literal(unittest.TestCase):
    def test_code_block_literal(self):
        out = b.md_to_html("```\n<script>x</script> [a](javascript:1) **b**\n```")
        self.assertIn("&lt;script&gt;x&lt;/script&gt; [a](javascript:1) **b**", out)
        self.assertNotIn("<a ", out)

    def test_inline_code_literal(self):
        out = b.md_inline("`[a](javascript:1)` y `<b>`")
        self.assertEqual(out, "<code>[a](javascript:1)</code> y <code>&lt;b&gt;</code>")

    def test_raw_html_escaped(self):
        self.assertEqual(b.md_inline('<img src=x onerror=alert(1)>'),
                         "&lt;img src=x onerror=alert(1)&gt;")

    def test_code_lang_attribute(self):
        out = b.md_to_html('```py" onclick="x\nprint(1)\n```')
        self.assertNotIn("onclick", out)
        self.assertIn('<code class="lang-python">', b.md_to_html("```python\nx\n```"))


class Slugs(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(b.safe_slug("verde-no-es-una-orden"), "verde-no-es-una-orden")

    def test_invalid(self):
        for s in ["../x", "a/b", "A", "x.html", "", "-x", "a b", "a\x00"]:
            with self.subTest(s=s), self.assertRaises(b.UnsafeContent):
                b.safe_slug(s)


class AtomicBuild(unittest.TestCase):
    def test_failure_keeps_previous_output(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            (tmp / "posts").mkdir()
            (tmp / "posts" / "2026-01-01-x.md").write_text(
                "---\ntitle: X\ndate: 2026-01-01\n---\n[a](javascript:alert(1))\n")
            out = tmp / "public"
            out.mkdir()
            (out / "index.html").write_text("ULTIMA-VALIDA")
            old = (b.POSTS_DIR, b.OUT)
            b.POSTS_DIR, b.OUT = tmp / "posts", out
            try:
                with self.assertRaises(b.UnsafeContent):
                    b.build()
            finally:
                b.POSTS_DIR, b.OUT = old
            self.assertEqual((out / "index.html").read_text(), "ULTIMA-VALIDA")
            self.assertFalse((tmp / "public.tmp").exists())
        finally:
            shutil.rmtree(tmp)


if __name__ == "__main__":
    unittest.main()
