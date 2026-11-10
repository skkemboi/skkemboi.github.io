# Personal research website (Quarto)

## Put it online with GitHub Pages
1. Create a repo named `yourusername.github.io`.
2. Upload everything in this folder (including `docs/` and `_freeze/`).
3. Settings → Pages → Deploy from a branch → `main`, folder `/docs`.
4. Site appears at https://yourusername.github.io within a few minutes.

Before uploading, replace `yourusername` in `_quarto.yml`.

## Edit or add posts
- Install Quarto (quarto.org) and Python with numpy, scipy, matplotlib, jupyter.
- `quarto preview` shows a live local preview.
- New post: copy a folder in `posts/`, rename it, and edit `index.qmd`.
- `quarto render` rebuilds `docs/`. Commit and push.
