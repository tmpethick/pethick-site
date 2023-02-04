# Personal blog

This is the source code for my personal blog.

## Develop

The following commands are available:

- `make build`: For building without autoupdate (uses `.html` so browsing works without a local host)
- `make autobuild`: Generates `conf.py` and then auto-builds (mind that changes to `conf.py` will not be registered)
- `make autorebuild`: Like autobuild but will remove all `_build` to prevent caching
- `make deploy`: Deploys to Github Pages using ablog scripts.

## Documentation

- https://jupyterbook.org/en/stable/structure/configure.html
- https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html
- https://sphinx-book-theme.readthedocs.io/en/latest/reference/kitchen-sink/index.html


## Fixes

Using cutting edge to fix math in footnote (https://github.com/executablebooks/sphinx-book-theme/issues/612):

```
pip install git+https://github.com/executablebooks/sphinx-book-theme.git@v0.4.0rc1 
-e https://github.com/executablebooks/sphinx-book-theme.git@v0.4.0rc1#egg=sphinx-book-theme
```

Alternatively to fix it locally, modify `sphinx-book-theme` (specifically `/usr/local/Caskroom/miniconda/base/lib/python3.9/site-packages/sphinx_book_theme/_transforms.py`) with `https://github.com/executablebooks/sphinx-book-theme/pull/641/files`.
