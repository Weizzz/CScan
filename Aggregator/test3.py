#!/usr/bin/python

import urllib2
from bs4 import BeautifulSoup

site = 'http://dfat.gov.au/aid/who-we-work-with/ngos/Pages/list-of-australian-accredited-non-government-organisations.aspx'

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = urllib2.Request(site, headers=hdr)

page = urllib2.urlopen(req).read() 

soup = BeautifulSoup(page, "html.parser")

content = soup.findAll('div',{'class':'content-area'})[0]
lists = content('p')[0]
print lists.string
if lists==None:
    print "returned null"
else:
    print "returned not null"

#for lists in soup('div',{'class':'content-area'})[0]('ul'):
#    list_items = lists('li')
#    for item in list_items:
#    	print item('a')[0].string


