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
THEME = "themes/twinkle"
THEME_STATIC_DIR = 'theme'

# JINJA
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.loopcontrols']
}

# PLUGINS
PLUGIN_PATHS = ['./themes/twinkle/plugins']
PLUGINS = [
    'pelican.plugins.sitemap',
    'representative_image',
    'share_post',
    'github_activity',
    'neighbors'
]

CLEAN_SUMMARY_MAXIMUM = 0
CLEAN_SUMMARY_MINIMUM_ONE = False

SITEMAP = {
    'format': 'xml'
}

LINKS = (
    ("home", "https://twinklekhj.xyz", "fontawesome"),
    ("velog", "https://velog.io/@developer_khj", "image"),
    ("github", "https://github.com/hjkim1004", "image"),
    ("gmail", "mailto:developer.heejeong@gmail.com", "image"),
)

# Author Name
AUTHOR = "Heejeong Kim"
AUTHOR_GITHUB = "hjkim1004"
AUTHOR_DESC = "Hi, I'm full-stack developer<br>Thanks for visiting"

GITHUB_ACTIVITY_FEED = 'https://github.com/hjkim1004.atom'
GITHUB_ACTIVITY_MAX_ENTRIES = 10

# OG METADATA
OG_TITLE = SITENAME
OG_DESCRIPTION = "Welcome To Twinkle's Blog."
