AUTHOR = "Heejeong Kim"
SITENAME = "Twinkle's Blog"
SITEURL = ""

PATH = "content"
TIMEZONE = 'Asia/Seoul'
DEFAULT_LANG = 'en'

# THEME settings
THEME = "themes/twinkle"
THEME_STATIC_DIR = 'theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
    ("KakaoTalk", "https://pf.kakao.com/_byerG/chat"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

DISQUS_SITENAME = "twinklekhj"

#######################################
# PLUGINS
#######################################
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['pelican.plugins.sitemap', 'representative_image', 'share_post', 'series']

SITEMAP = {
    'format': 'xml'
}

#######################################
# Config options custom
#######################################
LINKS = (
    ("home", "https://twinklekhj.xyz"),
    ("velog", "https://velog.io/@developer_khj"),
    ("github", "https://github.com/hjkim1004"),
    ("gmail", "mailto:developer.heejeong@gmail.com"),
)

AUTHOR_DESC = "Full Stack Developer"

# GitHub
GITHUB_USERNAME = "hjkim1004"

# OG METADATA
OG_TITLE = SITENAME
OG_DESCRIPTION = "Welcome To Twinkle's Blog."
