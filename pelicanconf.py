#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kendra Frederick'
SITENAME = 'Data Science: A Scenic Date'
# SITETITLE = "Kendra Frederick"
SITETITLE = "A Scenic Date"
SITESUBTITLE = "Kendra Frederick's Data Science Blog"
SITEURL = 'https://kbfreder.github.io'
SITELOGO = SITEURL + '/images/profile.png'
# SITELOGO = 'images/profile.png'

PATH = 'content'
THEME = 'theme/pelican-clean-blog'
# https://github.com/gilsondev/pelican-clean-blog
# CUSTOM_CSS = 'static/custom.css'
HEADER_COLOR = 'blue'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Analytics
GOOGLE_ANALYTICS = 'UA-126640488-1'

# links in sidebar under picture & site-title
# LINKS = (('about', '/about.html'),
        # ('contact', '/contact.html'),
         # )

# Social widget
SOCIAL = ( ('github', 'https://github.com/kbfreder'),
            ('linkedin', 'https://linkedin.com/in/kbfreder'),
          )

DEFAULT_PAGINATION = 10

MAIN_MENU = True
MENUITEMS = (('Categories', '/categories.html'),
             ('Tags', '/tags.html'),
             ('About Me', '/pages/about.html#about')
             # ('Archives', '/archives.html'),
             )

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

# static paths are copied without parsing their content
STATIC_PATHS = ['images', 'static']

# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored.
IGNORE_FILES = [".ipynb_checkpoints"]
