#!/usr/local/bin/python3

import pypandoc
import urllib.request
import re
import os.path

pages = [
"and-more-on-our-garden-soil.html",
"garden-meeting.html",
"cover-crops.html",
"garden-opens.html",
"enjoying-summer-and-planting-for-fall.html",
"garden-rules.html",
"garden-closes.html",
"good-sources-for-seeds-and-plants.html",
"mulch.html",
"our-garden-soil.html",
"garden-contest-2012.html",
"planting-deadline.html",
"garden-contest-2013.html",
"what-tomato-disease-is-it.html",
"garden-contest-2014.html",
"zone-7-planting-calendar.html",
"garden-contest-2015.html"
]

base_url = 'http://nyackcommunitygarden.info/'

def get_page(page):
    url = base_url + page + '?action=raw'
    print(url)
    '''
Note that urlopen returns a bytes object. This is because there is no way for urlopen to
automatically determine the encoding of the byte stream it receives from the http server.
In general, a program will decode the returned bytes object to string.
	'''
    html = urllib.request.urlopen(url)
    return str(html.read())

# Download
# for page in pages:
# 	if os.path.isfile(page + ".html") is False:
# 		html_text = get_page(page)
# 		# If there's a / ...
# 		new_page = page.replace('/', '_')
# 		html_f = open("{}.html".format(new_page), 'w')
# 		html_f.write(html_text)

# Convert
for page in pages:
	# page = page.replace('/', '_')
	f = open(page)
	html_text = f.read()

    # Various replacements that pandoc does not do
	print("Converting {}".format(page))
	#html_text = html_text.replace('<perl>', '\n```perl\n')
	#html_text = html_text.replace('</perl>', '\n```\n')
	#html_text = html_text.replace("\\n", "\n")

	md_text = pypandoc.convert(html_text, 'markdown_github', format='html')

	# Correct some conversion errors
	#md_text = md_text.replace('\\\\', '')
	#md_text = md_text.replace('1.  !', '#!')
	#md_text = md_text.replace('\\`\\`\\`', '```')
	#md_text = md_text.replace('\\_', '_')

	md_page = page.replace('.html', '')
	md_f = open("{}.md".format(page), 'w')
	md_f.write(md_text)
