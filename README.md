# Amir Rahman Portfolio

A static portfolio website presenting Amir's AI, computer vision, data, web-development, writing, and community work.

## Run locally

Serve the repository over HTTP so embedded pages and assets resolve correctly:

```powershell
python -m http.server 8000
```

Then open `http://localhost:8000`.

## Structure

- `index.html` — main portfolio page
- `assets/` — styles, scripts, documents, and media
- `assets/gallery.html` — embedded awards gallery
- `networkgraphs/` — interactive graphs and their Python generators

## Updating network graphs

Install the graph dependencies:

```powershell
python -m pip install -r requirements.txt
```

Run a generator from the `networkgraphs` directory, then confirm the generated HTML uses the vendored files under `networkgraphs/lib/`.

## Contact

Use `rahman.amir.h@gmail.com` for all portfolio inquiries.
