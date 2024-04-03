SITENAME = "Twinkle's Blog"
SITEURL = ""

PATH = "content"
TIMEZONE = 'Asia/Seoul'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

DISQUS_SITENAME = "twinklekhj"

#######################################
# THEME Options
#######################################
# Statics
STATIC_PATHS = ["images", "extra/robots.txt"]
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
}

# THEME
THEME = "themes/pelican-twinkle"
THEME_STATIC_DIR = 'theme'

# JINJA
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.loopcontrols']
}

# PLUGINS
PLUGIN_PATHS = [THEME + '/plugins']
PLUGINS = [
    'pelican.plugins.sitemap',
    'representative_image',
    'share_post',
    'neighbors',
    'custom_article_urls'
]

# PLUGIN - custom_article_urls
ARTICLE_URL = "posts/{slug}.html"
CUSTOM_ARTICLE_URLS = {
    'pelican': {
        'URL': 'posts/{category}/{slug}/',
        'SAVE_AS': 'posts/{category}/{slug}.html'
    }
}

# PLUGIN - sitemap
SITEMAP = {
    'format': 'xml'
}

# Author Links
LINKS = (
    ("home", "https://twinklekhj.xyz", "fontawesome"),
    ("velog", "https://velog.io/@developer_khj", "image"),
    ("github", "https://github.com/hjkim1004", "image"),
    ("gmail", "mailto:developer.heejeong@gmail.com", "image"),
)

# Author Name
AUTHOR = "Heejeong Kim"
AUTHOR_INFO = {
    "GITHUB": "hjkim1004",
    "DESCRIPTION": "Hi, I'm full-stack developer<br>Thanks for visiting"
}

# OG METADATA
OG_TITLE = SITENAME
OG_DESCRIPTION = AUTHOR_INFO["DESCRIPTION"]

# Date Format
DEFAULT_DATE_FORMAT = ('%b %d, %Y')
