# Personal blog

This is the source code for my personal blog.

## Develop

The following commands are available:

- `make build`: For building without autoupdate (uses `.html` so browsing works without a local host)
- `make autobuild`: Generates `conf.py` and then auto-builds (mind that changes to `conf.py` will not be registered)
- `make rebuild`/`make autorebuild`: Like (auto)build but will remove all `_build` to prevent caching
- `make deploy`: Deploys to Github Pages using ablog scripts.

## Documentation

- https://jupyterbook.org
- https://myst-parser.readthedocs.io
- https://sphinx-book-theme.readthedocs.io


## Fixes

Using cutting edge to fix math in footnote (https://github.com/executablebooks/sphinx-book-theme/issues/612):

```
pip install git+https://github.com/executablebooks/sphinx-book-theme.git@v0.4.0rc1 
-e https://github.com/executablebooks/sphinx-book-theme.git@v0.4.0rc1#egg=sphinx-book-theme
```

Alternatively to fix it locally, modify `sphinx-book-theme` (specifically `/usr/local/Caskroom/miniconda/base/lib/python3.9/site-packages/sphinx_book_theme/_transforms.py`) with `https://github.com/executablebooks/sphinx-book-theme/pull/641/files`.

Steps:

- Run `make autorebuild` without modification
- Modify `sphinx-book-theme` (remember to delete `__pycache`)
- then only modify `<post>.md` to be recompiled
- Rename `_build` to `_website` and add `.nojekyll`
- Run `ablog deploy`
