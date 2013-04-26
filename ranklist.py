#!/usr/bin/env python

from __future__ import division
from pyquery import PyQuery as pq
import codecs
import math

scoreTable = []
for index in xrange(0,1800, 20):
    print index,"walking"
    url = "http://book.douban.com/tag/%E7%A7%91%E5%AD%A6?start="+str(index)
    b = pq(url=url)
    for book in b('li.subject-item').items():
        bookinfo = book('.info')
        name = bookinfo('a').attr('title')
        #print bookinfo('span.rating_nums').text(), name
        if (bookinfo('span.rating_nums').text() != None):
            rating = float(str(bookinfo('span.rating_nums').text()))
        else:
            rating = 1
        #num = int( str(bookinfo('span.pl').text()) )
        num = 1000
        score = rating*math.log(num/100.0)
        scoreTable.append(dict(score=score, name=name))


scoreTable.sort(key=lambda book: book['score'])
scoreTable.reverse()
fout = codecs.open("score.out", mode="w", encoding='utf-8')
for score in scoreTable:
    fout.write(u"score %0.2f name %s\n" % (score['score'], score['name']))
