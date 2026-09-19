# Hello, World from Diana

A small, warm family microsite built as a deliberately lightweight static web project.

The original 2023 learning project has been refreshed to preserve its personal character while applying modern frontend fundamentals without changing the core stack.

## What it does

- introduces Diana on a simple landing page
- presents a small family photo gallery
- links each gallery card to a larger version of the photo
- works across mobile, tablet, and desktop layouts
- requires no build step or application runtime

## Stack

- semantic HTML5
- modern CSS
- Bootstrap 5.3.8
- Bootstrap's bundled JavaScript for responsive navigation
- GitHub Pages-ready static assets

The project intentionally does **not** use React, Vue, a bundler, or a custom JavaScript application layer. For a two-page static site, those tools would add complexity without improving the product.

## Product and design approach

The public-facing experience is intentionally family-first rather than technology-first.

The visual direction is a **small digital family album**, designed to feel warm, gentle, nostalgic, and emotionally familiar rather than like a conventional portfolio landing page.

The site uses:

- warm ivory, cream, peach, and dusty-rose tones
- soft paper-like surfaces instead of hard white cards
- editorial serif typography for a personal, timeless feeling
- subtle photo-album and instant-photo framing
- restrained paper-tape details around photographs
- small rotations that make the gallery feel collected rather than mechanically aligned
- affectionate microcopy focused on home, togetherness, and memory
- soft shadows and low-contrast borders
- subtle motion only where it improves affordance
- no external font dependency and no unnecessary visual library

Technical proof belongs in the repository documentation; the website itself is designed to feel like something a family would enjoy revisiting years later.

## Engineering improvements

The refresh focuses on high-value fundamentals:

- semantic page landmarks and heading structure
- keyboard-accessible skip navigation
- visible focus states
- meaningful image alternative text
- unique accessible names for repeated gallery links
- explicit new-tab announcements for photo links
- responsive image presentation
- lazy loading for non-critical images
- `prefers-reduced-motion` support
- project-relative asset and navigation URLs that work on GitHub Pages
- Bootstrap CDN Subresource Integrity (SRI)
- shared styling in a dedicated stylesheet instead of duplicated inline CSS
- page descriptions plus Open Graph and Twitter summary metadata
- safer new-tab image links with `rel="noopener noreferrer"`
- an intentionally small dependency surface

## Quality checks

The repository includes a small zero-dependency validation script and a GitHub Actions workflow.

The checker verifies:

- expected local files and linked assets exist
- every page has one `<main>` and one `<h1>`
- HTML IDs are unique within each page
- images include `alt` attributes
- links opened in a new tab use both `noopener` and `noreferrer`
- local fragment links point to existing IDs
- each page includes viewport and description metadata
- the web manifest is valid JSON and references existing icon files

Run it locally with:

    python scripts/check_site.py

## Project structure

    .
    ├── .github/
    │   └── workflows/
    │       └── quality.yml
    ├── scripts/
    │   └── check_site.py
    ├── index.html
    ├── places.html
    ├── styles.css
    ├── img.jpg
    ├── img1.jpg
    ├── img1-1.jpg
    ├── img2.jpg
    ├── img2-2.jpg
    ├── img3.jpg
    ├── img3-3.jpg
    ├── logo.png
    ├── site.webmanifest
    └── favicon assets

## Run locally

No installation is required.

Open `index.html` directly in a browser, or serve the folder with any static HTTP server.

For example:

    python -m http.server 8000

Then visit `http://localhost:8000`.

## Architecture

This is intentionally a static two-page website.

Bootstrap provides proven responsive layout primitives and the collapsible navigation. Custom CSS owns the visual language and responsive presentation. There is no framework, client-side state layer, build pipeline, or application abstraction because none of those solve a real requirement here.

That is the main architectural decision of the project: keep the implementation proportional to the product.

## Image strategy

The original family photographs are preserved as project assets. The gallery already separates smaller page images from larger versions opened on demand, so the full-size originals are not loaded as part of the gallery view.

Further binary transcoding to WebP/AVIF would be a deployment optimization rather than an architectural change and can be added independently without changing the runtime stack.

## Author

Mykola Dotsenko
