#!/usr/bin/python

import urllib, webbrowser, ConfigParser, os, unicodedata

def results(parsed, original_query):
    return {
        "title": 'Confluence search',
        "run_args": [parsed['~words']]
    }

def run(words):
    config = ConfigParser.SafeConfigParser()
    config.read('%s/.confluence' % os.environ['HOME'])
    baseurl = config.get('confluence', 'baseurl')
    normalized = unicodedata.normalize('NFC', words)
    encoded = urllib.quote_plus(normalized.encode('utf8'))
    url = '%s/wiki/dosearchsite.action?queryString=%s' % (baseurl, encoded)
    webbrowser.open_new_tab(url)
