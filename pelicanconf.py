AUTHOR = "User"
SITENAME = "My Portfolio"
SITEURL = "http://localhost:8000"

SITETITLE = "My Portfolio"  # genusテーマで使用
SITESUBTITLE = ""

PATH = "content"

TIMEZONE = "Asia/Tokyo"

DEFAULT_LANG = "Japanese"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# THEME = "crowsfoot"
THEME = "genus"

PAGE_URL = "{category}/{slug}.html"
PAGE_SAVE_AS = "{category}/{slug}.html"

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

STATIC_PATHS = ["images", "theme"]

MARKDOWN = {
    "extensions": [
        "markdown.extensions.extra",
        "markdown.extensions.codehilite",
        "markdown.extensions.meta",
        "mdx_truly_sane_lists",  # sane_listsが機能しない問題への対応
    ],
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}
