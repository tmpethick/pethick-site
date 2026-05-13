
import datetime
import re

# ablog configuration
import ablog
extensions = ["ablog"] + extensions
fontawesome_included = True
blog_path = "posts"
blog_title = "Thomas Pethick's blog"
blog_baseurl = "https://pethick.dk/"
blog_feed_archives = True
github_pages = "tmpethick"
post_show_prev_next = False

# Populate publication context for jinja template
import yaml
with open("publications.yml", "r") as stream:
    publications = yaml.safe_load(stream)
jinja_contexts = {
  'publications_ctx': {'publications': publications}
}

# Provide Jinja filter
def format_date(date_string):
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    return date.strftime("%b %d, %Y")

jinja_filters = {
    'format_date': format_date,
}


# Makes footnotes Tufte-style sidenotes
# (see https://sphinx-book-theme.readthedocs.io/en/stable/content-blocks.html?highlight=sidenote#activate-sidenotes-and-marginnotes)
html_theme_options['use_sidenotes'] = True


def _bibtex_escape(value):
    replacements = {
        "\\": r"\textbackslash{}",
        "{": r"\{",
        "}": r"\}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
    }
    return "".join(replacements.get(char, char) for char in value)


def _citation_key(year, slug):
    slug = re.sub(r"^\d{4}-\d{2}-\d{2}-?", "", slug)
    key_slug = re.sub(r"[^A-Za-z0-9]+", "", slug).lower()
    return f"pethick{year}{key_slug}"


def _append_post_citation(app, docname, source):
    if not docname.startswith("posts/") or "/" in docname[len("posts/"):]:
        return

    text = source[0]
    post_match = re.search(r"^```\{post\}\s+(\d{4}-\d{2}-\d{2})", text, re.MULTILINE)
    title_match = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
    if not post_match or not title_match:
        return

    date = post_match.group(1)
    year, month, day = date.split("-")
    title = re.sub(r"\s+", " ", title_match.group(1)).strip()
    slug = docname.rsplit("/", 1)[-1]
    baseurl = app.config.blog_baseurl.rstrip("/")
    url = f"{baseurl}/posts/{slug}/"
    bibtex = f"""@misc{{{_citation_key(year, slug)},
  author = {{Thomas Pethick}},
  title = {{{_bibtex_escape(title)}}},
  year = {{{year}}},
  month = {{{month}}},
  day = {{{day}}},
  url = {{{url}}},
  note = {{Blog post}}
}}"""

    source[0] = text.rstrip() + f"""

## Cite this post

```bibtex
{bibtex}
```
"""


def setup(app):
    app.connect("source-read", _append_post_citation)
