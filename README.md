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

The site uses:

- warm neutral colors and soft rose accents
- an editorial serif/sans-serif typography pairing using system fonts
- organic photo shapes and restrained decorative elements
- a compact family-story section
- a responsive photo collage built from the original project assets
- subtle motion only where it improves affordance
- no external font dependency and no unnecessary visual library

Technical proof belongs in the repository documentation; the website itself is designed to feel like a small digital family album.

## Engineering improvements

The refresh focuses on high-value fundamentals:

- semantic page landmarks and heading structure
- keyboard-accessible skip navigation
- visible focus states
- meaningful image alternative text
- responsive image presentation
- lazy loading for non-critical images
- `prefers-reduced-motion` support
- project-relative asset and navigation URLs that work on GitHub Pages
- Bootstrap CDN Subresource Integrity (SRI)
- shared styling in a dedicated stylesheet instead of duplicated inline CSS
- clearer metadata, page titles, and descriptions
- safer new-tab image links with `rel="noopener noreferrer"`
- an intentionally small dependency surface

## Project structure

    .
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

## Author

Mykola Dotsenko
