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
