
import datetime

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
