#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime;

# No Cache
LOAD_CONTENT_CACHE = False;

# Site Information
SITENAME = 'MSAIL';
SITEURL = '';
AUTHOR = 'MSAIL';
TIMEZONE = 'America/Detroit';
DEFAULT_LANG = 'en';

# Basic Settings
PATH = 'content';
THEME = "./theme";
DEFAULT_PAGINATION = False;
DEFAULT_DATE_FORMAT = "%a, %d %b %Y";

# Custom Settings (custom variables defined by me, to be passed to templates)
SITE_LAST_MODIFIED = datetime.datetime.now();

## Pages, Paths, and URLs ------------------------------------------------------

# Articles & Pages
ARTICLE_PATHS = ['events'];
PAGE_ORDER_BY = "order";

# Static Paths:  Simple static pages, with custom URLS
STATIC_PATHS = ['images', 'static'];
EXTRA_PATH_METADATA = {
    'static/favicon.ico': {'path': 'favicon.ico'},
    'static/CNAME'      : {'path': 'CNAME'}
};

# URL Settings (different from publishconf.py)
ARTICLE_URL = "events/{category}/{date:%Y}/{date:%b}/{date:%d}/{slug}";
ARTICLE_SAVE_AS = 'events/{category}/{date:%Y}/{date:%b}/{date:%d}/{slug}.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

## Content Generation ----------------------------------------------------------

# Delete output directory when regenerating, but save Git repositories.
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".git", ".gitignore", ".git/*"]

## External Links / Plugins ----------------------------------------------------

# Plugins
#PLUGIN_PATHS = ['plugins'];
#PLUGINS = ["render_math", "simple_footnotes"];

# Feeds (disabled while developing)
FEED_ALL_ATOM = None;
CATEGORY_FEED_ATOM = None;
TRANSLATION_FEED_ATOM = None;
AUTHOR_FEED_ATOM = None;
AUTHOR_FEED_RSS = None;

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True