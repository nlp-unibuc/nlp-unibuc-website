#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'nlp'
SITENAME_LOC = dict(en=u'Center for Computational Linguistics',
                    ro=u'Centrul pentru Lingvistică Computațională')
SITESUBTITLE_LOC = dict(en=u'University of Bucharest',
                        ro=u'Universitatea din București')
SITEURL = ''

TIMEZONE = 'Europe/Bucharest'

DEFAULT_LANG = u'en'
SITENAME = SITENAME_LOC[DEFAULT_LANG]
SITESUBTITLE = SITESUBTITLE_LOC[DEFAULT_LANG]

TYPOGRIFY = True

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

THEME = 'themes/clc1.0'

ARTICLE_DIR = 'blog'
ARTICLE_EXCLUDES = ()

ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_LANG_URL = 'blog/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = 'blog/{slug}-{lang}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'
