"""Composable, HTML-first frontend definitions."""

from __future__ import annotations

from dataclasses import dataclass, field
from html import escape
from typing import Literal

BlockKind = Literal["html", "css", "javascript"]


@dataclass(frozen=True)
class FrontendBlock:
    """A user-supplied frontend fragment.

    Fragments are deliberately passed through unchanged so callers can use
    their own components and browser-side tooling. Treat all untrusted input
    as unsafe before adding it to a block.
    """

    kind: BlockKind
    content: str


@dataclass
class Frontend:
    """Build a standalone HTML document from HTML, CSS, and JavaScript blocks."""

    title: str = "Methys"
    blocks: list[FrontendBlock] = field(default_factory=list)

    def add_block(self, kind: BlockKind, content: str) -> "Frontend":
        """Append a frontend block and return this definition for chaining."""
        self.blocks.append(FrontendBlock(kind=kind, content=content))
        return self

    def add_html(self, content: str) -> "Frontend":
        return self.add_block("html", content)

    def add_css(self, content: str) -> "Frontend":
        return self.add_block("css", content)

    def add_javascript(self, content: str) -> "Frontend":
        return self.add_block("javascript", content)

    def render(self) -> str:
        """Render the definition as a complete HTML document."""
        html = "\n".join(block.content for block in self.blocks if block.kind == "html")
        css = "\n".join(block.content for block in self.blocks if block.kind == "css")
        javascript = "\n".join(
            block.content for block in self.blocks if block.kind == "javascript"
        )
        return (
            "<!doctype html>\n"
            "<html lang=\"en\">\n"
            "<head>\n"
            "  <meta charset=\"utf-8\">\n"
            "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
            f"  <title>{escape(self.title)}</title>\n"
            f"  <style>\n{css}\n  </style>\n"
            "</head>\n"
            f"<body>\n{html}\n  <script>\n{javascript}\n  </script>\n</body>\n"
            "</html>\n"
        )
