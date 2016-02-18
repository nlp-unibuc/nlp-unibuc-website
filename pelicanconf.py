#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'nlp'
SITENAME_LOC = dict(en=u'Center for Computational Linguistics',
                    ro=u'Centrul pentru Lingvistică Computațională')
SITESUBTITLE_LOC = dict(en=u'University of Bucharest',
                        ro=u'Universitatea din București')
SITEURL = ''

TIMEZONE = 'Europe/Bucharest'

GOOGLE_ANALYTICS='UA-69680045-1'

#LOCALE = u'en'
DEFAULT_LANG = u'en'
SITENAME = SITENAME_LOC[DEFAULT_LANG]
SITESUBTITLE = SITESUBTITLE_LOC[DEFAULT_LANG]

TYPOGRIFY = True

# Disable feeds
FEED_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
FEED_RSS = None
CATEGORY_FEED_RSS = None

# Blogroll
LINKS = None
#LINKS = (('Github repository', 'http://github.org/nlp-unibuc'),
#        ('Vlad Niculae', 'http://vene.ro'))

# Social widget
SOCIAL = ()

# Plugins
PLUGIN_PATHS = ['plugins/']
PLUGINS = ['pelican-bibtex']
PUBLICATIONS_SRC = 'content/pubs.bib'

THEME = 'themes/clc1.0'

DIRECT_TEMPLATES = ('blog', 'publications')
PAGINATED_DIRECT_TEMPLATES = ('index', 'blog')

DEFAULT_PAGINATION = False
ARTICLE_PATHS = ['blog']
ARTICLE_EXCLUDES = []

ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_LANG_URL = 'blog/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = 'blog/{slug}-{lang}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'
CATEGORY_URL = 'blog/category/{slug}.html'
CATEGORY_SAVE_AS = 'blog/category/{slug}.html'
TAG_URL = 'blog/tag/{slug}.html'
TAG_SAVE_AS = 'blog/tag/{slug}.html'
BLOG_SAVE_AS = 'blog/index.html'

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    # ('News', SITEURL + '/blog/'),  # siteurl not needed?
    ('News', '/blog/'),
    ('People', '/people.html'),
    ('Projects', '/projects.html'),
    ('Resources', '/resources.html'),
    ('Publications', '/publications.html'),
)

# "static" files
STATIC_PATHS = ['CNAME', 'papers/', 'resources/', 'courses/']
