# Hello, World from Diana

A small family microsite from 2023, kept public as an early HTML/CSS learning project and refreshed without changing its simple character.

[**Open the site →**](https://mykoladotsenko.github.io/Hello-World-from-Diana/)

## What it is

- a two-page family site;
- a small photo gallery;
- responsive layouts for phone/tablet/desktop;
- static assets with no build step or application runtime.

The live experience is intentionally family-first rather than a technical showcase.

## Stack

- semantic HTML
- modern CSS
- Bootstrap 5
- Bootstrap navigation JavaScript
- GitHub Pages

There is no React/Vue layer or custom application state because a two-page site does not need one.

## Refresh work

The original project was updated with:

- clearer semantic landmarks/headings;
- skip navigation and visible focus;
- meaningful image alt text;
- reduced-motion support;
- responsive WebP `srcset` variants;
- explicit image dimensions and lazy loading;
- shared stylesheet;
- page/social metadata;
- safe new-tab links.

Large family images were also resized/compressed and generated without EXIF/GPS metadata.

## Quality check

```bash
python scripts/check_site.py
```

The checker validates local links/assets, document landmarks, unique IDs, image alt text, safe new-tab links, metadata and the web manifest.

## Run locally

No installation is required:

```bash
python -m http.server 8000
```

Open `http://localhost:8000/`.

## History

I keep this repository public because it is part of the progression of my frontend work. The refresh improves fundamentals without pretending the original small family project was something more complex.

## Author

Mykola Dotsenko
