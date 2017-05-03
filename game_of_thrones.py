#!/usr/bin/env python
# -*- coding:utf-8 -*-

from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Game_of_Thrones"

open_got = urlopen(url).read()

soup = BeautifulSoup(open_got)

wikitable = soup.find("table", {"class": "wikitable"})

views = 0

for link in wikitable.findAll('a'):
    if "Season 7" in link.string:
        pass
    elif "Season" in link.string:
        season_link = "https://en.wikipedia.org" + link["href"]
        open_season_link = urlopen(season_link).read()
        soup2 = BeautifulSoup(open_season_link)

        wikitable2 = soup2.find("table", {"class": "wikitable plainrowheaders wikiepisodetable"})

        for row in wikitable2.findAll("tr")[1:]:  #excludes first row of the table
            for td in row.findAll("td")[5:]:    #takes only the last column
                #print td.text[:4]
                #views += float(td.text[:4])  #takes only first four numbers
                #print td.find(text=True, recursive=False)
                views += float(td.find(text=True, recursive=False))  # ignores child tags in td

print (str(views) + " millions")
