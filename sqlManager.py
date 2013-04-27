#!/usr/bin/env python

from sqlalchemy import create_engine, text
from pyquery import PyQuery as pq
import urllib

e = create_engine('sqlite://///home/luxuia/www/BookReuse/book.db')
d = pq(url="http://book.douban.com/tag/%E7%A7%91%E6%99%AE")
homebook = []
for i in d('li.subject-item').items():
    imgsrc = i('img').attr('src')
    mtitle   = i('div.info')('a').attr('title')
    url    = i('div.info')('a').attr('href')
    rate_num = float(i('div.info')('.rating_nums').text())
    rate_man = i('div.info')('.pl').text()
    info = i('div.info')('p').text()

    homebook.append(dict(src=imgsrc, name=mtitle, url=url, rate_num=rate_num,
                    rate_man = rate_man, info=info))
count = e.execute("select count(*) from bookinfo").first()[0]

for book in homebook:
    urllib.urlretrieve(book['src'],
            "./static/img/%d.jpg"%count)
    e.execute(text("insert into bookinfo(main_title, \
            img_url,rating_num, rating_man, short_info)\
            values(:title,:url,:rating_n,:rating_m, :info)"),
            {'title':book['name'],
            'url':"/static/img/%d.jpg"%count,\
            'rating_n':book['rate_num'], 'rating_m':book['rate_man'],\
            'info':book['info']})
    count+=1
