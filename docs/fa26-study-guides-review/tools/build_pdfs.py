#!/usr/bin/env python3
"""Render the review study guides (md/*.md) to PDF (pdf/*.pdf) with headless Chrome.

Usage: python3 tools/build_pdfs.py   (requires `pip install markdown` and google-chrome)
"""
import html
import pathlib
import re
import subprocess
import sys
import tempfile

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
MD_DIR = ROOT / "md"
PDF_DIR = ROOT / "pdf"
CHROME = "/opt/google/chrome/chrome"

CSS = """
@page {
  size: Letter;
  margin: 0.7in 0.65in 0.75in 0.65in;
  @bottom-left { content: "Study aid only — not for submitted work · FA26 Opus review 2026-09-24"; font: 8pt 'DejaVu Sans', sans-serif; color: #666; }
  @bottom-right { content: "p. " counter(page) " / " counter(pages); font: 8pt 'DejaVu Sans', sans-serif; color: #666; }
}
body { font-family: 'Noto Sans', 'DejaVu Sans', sans-serif; font-size: 10.2pt; line-height: 1.42; color: #111; }
h1 { font-size: 18pt; border-bottom: 2px solid #333; padding-bottom: 4px; margin-top: 0; }
h2 { font-size: 13.5pt; margin-top: 18px; border-bottom: 1px solid #bbb; padding-bottom: 2px; page-break-after: avoid; }
h3 { font-size: 11.5pt; margin-top: 14px; page-break-after: avoid; }
p, li { orphans: 3; widows: 3; }
p:first-of-type strong:first-child { color: #8a1c1c; }
table { border-collapse: collapse; width: 100%; margin: 6px 0 10px; font-size: 9.2pt; page-break-inside: avoid; }
th, td { border: 1px solid #999; padding: 3px 6px; vertical-align: top; text-align: left; }
th { background: #eee; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: 8.8pt; background: #f3f3f3; padding: 0 2px; }
pre { background: #f6f6f6; border: 1px solid #ddd; padding: 6px 8px; font-size: 8.6pt; line-height: 1.3; page-break-inside: avoid; white-space: pre-wrap; }
pre code { background: none; padding: 0; }
.pagebreak { page-break-before: always; }
hr { border: 0; border-top: 1px solid #ccc; margin: 14px 0; }
"""


LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+\.)\s")


def separate_lists(text: str) -> str:
    """Python-Markdown (unlike GitHub) needs a blank line before a list that follows a paragraph."""
    out, in_fence, prev = [], False, ""
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        elif not in_fence and LIST_ITEM.match(line) and prev.strip() and not LIST_ITEM.match(prev):
            out.append("")
        out.append(line)
        prev = line
    return "\n".join(out) + "\n"


def render(md_path: pathlib.Path) -> pathlib.Path:
    text = separate_lists(md_path.read_text(encoding="utf-8"))
    text = text.replace("<!-- PAGEBREAK -->", '\n<div class="pagebreak"></div>\n')
    body = markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists"])
    title = re.search(r"^# (.+)$", text, re.M)
    doc = (
        "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>"
        f"<title>{html.escape(title.group(1) if title else md_path.stem)}</title>"
        f"<style>{CSS}</style></head><body>{body}</body></html>"
    )
    PDF_DIR.mkdir(exist_ok=True)
    out = PDF_DIR / (md_path.stem + ".pdf")
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(doc)
        tmp = f.name
    # The google-chrome wrapper on some hosts adds a shared profile + debugging port that keeps
    # the process alive after printing, so call the binary with a throwaway profile.
    with tempfile.TemporaryDirectory() as profile:
        subprocess.run(
            [CHROME, "--headless", "--disable-gpu", "--no-sandbox", "--no-first-run",
             f"--user-data-dir={profile}", "--no-pdf-header-footer",
             f"--print-to-pdf={out}", f"file://{tmp}"],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90,
        )
    return out


def main() -> int:
    for md_path in sorted(MD_DIR.glob("*.md")):
        print("wrote", render(md_path).relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
