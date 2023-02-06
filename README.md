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
- Modify `sphinx-book-theme` (remember to delete `__pycache__`)
- then only modify `<post>.md` to be recompiled with `make autobuild`
- Rename `_build` to `_website` and add `.nojekyll`
- Run `ablog deploy`

```python
                    # second children of footnote node is the content text
                    foot_node_content = foot_node.children[1].children

                    sidenote = SideNoteNode()
                    para = docutil_nodes.inline()
                    # first children of footnote node is the label
                    label = foot_node.children[0].astext()

                    if foot_node_content[0].astext().startswith("{-}"):
                        # marginnotes will have content starting with {-}
                        # remove the number so it doesn't show
                        para.attributes["classes"].append("marginnote")
                        foot_node_content[0] = docutil_nodes.Text(
                            foot_node_content[0].replace("{-}", "")
                        )
                        para.children = foot_node_content

                        sidenote.attributes["names"].append(f"marginnote-role-{label}")
                    else:
                        # sidenotes are the default behavior if no {-}
                        # in this case we keep the number
                        superscript = docutil_nodes.superscript("", label)
                        para.attributes["classes"].append("sidenote")
                        parachildren = [superscript] + foot_node_content
                        para.children = parachildren

                        sidenote.attributes["names"].append(f"sidenote-role-{label}")
                        sidenote.append(superscript)
```
