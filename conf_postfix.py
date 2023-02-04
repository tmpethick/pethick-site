

# ablog configuration
import ablog
extensions = ["ablog"] + extensions
fontawesome_included = True
blog_path = "posts"
blog_title = "Thomas Pethick's blog"
blog_baseurl = "https://pethick.dk/"
blog_feed_archives = True

# Populate publication context for jinja template
import yaml
with open("publications.yml", "r") as stream:
    publications = yaml.safe_load(stream)
jinja_contexts = {
  'publications_ctx': {'publications': publications}
}

# Makes footnotes Tufte-style sidenotes
# (see https://sphinx-book-theme.readthedocs.io/en/stable/content-blocks.html?highlight=sidenote#activate-sidenotes-and-marginnotes)
html_theme_options['use_sidenotes'] = True
