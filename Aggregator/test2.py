#!/usr/bin/python

import urllib2
from bs4 import BeautifulSoup

site = 'https://www.unodc.org/ngo/list.jsp'

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = urllib2.Request(site, headers=hdr)

page = urllib2.urlopen(req).read() 

soup = BeautifulSoup(page)

#for row in soup('table')[0].tbody('tr', attr={'bgcolor':'#F0F0F0'}):
for row in soup('table')[0].tbody('tr'):
    print row.string
#    tds = row('td')
#    name = tds[0]('p')
#    print name[0].string

