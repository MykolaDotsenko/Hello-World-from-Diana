from __future__ import annotations

import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAGES = ("index.html", "places.html")
IGNORED_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript"}


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tags: list[tuple[str, dict[str, str | None]]] = []
        self.ids: list[str] = []
        self.links: list[tuple[str, dict[str, str | None]]] = []
        self.images: list[dict[str, str | None]] = []
        self.main_count = 0
        self.h1_count = 0
        self.html_lang: str | None = None
        self.has_viewport = False
        self.has_description = False

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        attributes = dict(attrs)
        self.tags.append((tag, attributes))

        element_id = attributes.get("id")
        if element_id:
            self.ids.append(element_id)

        if tag == "html":
            self.html_lang = attributes.get("lang")
        elif tag == "main":
            self.main_count += 1
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "img":
            self.images.append(attributes)
            self.links.append((tag, attributes))
        elif tag in {"a", "link", "script"}:
            self.links.append((tag, attributes))
        elif tag == "meta":
            if attributes.get("name") == "viewport":
                self.has_viewport = True
            if attributes.get("name") == "description":
                self.has_description = bool(attributes.get("content"))


def is_external(value: str) -> bool:
    parsed = urlsplit(value)
    return bool(parsed.scheme in IGNORED_SCHEMES or value.startswith("//"))


def local_target(page: Path, value: str) -> tuple[Path, str | None] | None:
    if not value or is_external(value):
        return None

    parsed = urlsplit(value)
    raw_path = unquote(parsed.path)
    fragment = unquote(parsed.fragment) or None

    if raw_path.startswith("/"):
        target = ROOT / raw_path.lstrip("/")
    elif raw_path:
        target = page.parent / raw_path
    else:
        target = page

    return target.resolve(), fragment


def check_page(page_name: str) -> list[str]:
    errors: list[str] = []
    page = ROOT / page_name

    if not page.is_file():
        return [f"{page_name}: file is missing"]

    parser = SiteParser()
    parser.feed(page.read_text(encoding="utf-8"))

    if not parser.html_lang:
        errors.append(f"{page_name}: <html> is missing a lang attribute")
    if parser.main_count != 1:
        errors.append(f"{page_name}: expected exactly one <main>, found {parser.main_count}")
    if parser.h1_count != 1:
        errors.append(f"{page_name}: expected exactly one <h1>, found {parser.h1_count}")
    if not parser.has_viewport:
        errors.append(f"{page_name}: viewport meta tag is missing")
    if not parser.has_description:
        errors.append(f"{page_name}: description meta tag is missing")

    duplicate_ids = sorted({item for item in parser.ids if parser.ids.count(item) > 1})
    for duplicate_id in duplicate_ids:
        errors.append(f"{page_name}: duplicate id #{duplicate_id}")

    for image in parser.images:
        if "alt" not in image:
            errors.append(
                f"{page_name}: image {image.get('src', '<unknown>')} is missing alt"
            )

    for tag, attributes in parser.links:
        value = (
            attributes.get("href")
            if tag in {"a", "link"}
            else attributes.get("src")
        )
        if not value:
            continue

        if tag == "a" and attributes.get("target") == "_blank":
            rel = set((attributes.get("rel") or "").split())
            required = {"noopener", "noreferrer"}
            missing = sorted(required - rel)
            if missing:
                errors.append(
                    f"{page_name}: target=_blank link {value} is missing "
                    + ", ".join(missing)
                )

        target_data = local_target(page, value)
        if target_data is None:
            continue

        target, fragment = target_data

        if not target.exists():
            errors.append(f"{page_name}: local reference does not exist: {value}")
            continue

        if fragment and target.suffix.lower() == ".html":
            target_parser = SiteParser()
            target_parser.feed(target.read_text(encoding="utf-8"))
            if fragment not in target_parser.ids:
                errors.append(
                    f"{page_name}: fragment #{fragment} does not exist in "
                    f"{target.relative_to(ROOT)}"
                )

    return errors


def check_manifest() -> list[str]:
    errors: list[str] = []
    manifest_path = ROOT / "site.webmanifest"

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"site.webmanifest: invalid or unreadable JSON: {exc}"]

    for key in ("name", "short_name", "icons", "theme_color", "background_color"):
        if not manifest.get(key):
            errors.append(f"site.webmanifest: required value is missing: {key}")

    for icon in manifest.get("icons", []):
        src = icon.get("src")
        if not src:
            errors.append("site.webmanifest: icon is missing src")
            continue
        if not (ROOT / src).is_file():
            errors.append(f"site.webmanifest: icon does not exist: {src}")

    return errors


def main() -> int:
    errors: list[str] = []

    for required in ("styles.css", "logo.png"):
        if not (ROOT / required).is_file():
            errors.append(f"missing required file: {required}")

    for page_name in PAGES:
        errors.extend(check_page(page_name))

    errors.extend(check_manifest())

    if errors:
        print("Site quality checks failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("Site quality checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
