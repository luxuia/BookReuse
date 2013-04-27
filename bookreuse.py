#!/usr/bin/env python
from flask import Flask, request, session, g, redirect, url_for,\
        abort, render_template, flash
from pyquery import PyQuery as pq
from sqlalchemy import create_engine

# configuration
DATABASE = './book.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = '123456'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return create_engine('sqlite://///home/luxuia/www/BookReuse/book.db')


def fetch_from_douban():
    homebook = []
    d = pq(url="http://book.douban.com/tag/%E7%A7%91%E6%99%AE")
    for i in d('li.subject-item').items():
        imgsrc = i('img').attr('src')
        info   = i('div.info')('a').attr('title')
        url    = i('div.info')('a').attr('href')
        homebook.append(dict(src=imgsrc, name=info, url=url))
    return homebook


@app.route('/')
def index():
    e = connect_db()
    homebook = e.execute('SELECT * FROM bookinfo').fetchall()


    return render_template( 'index.html', homebook=homebook )

@app.route('/login')
def login():
    return "try login"

@app.route('/logout')
def logout():
    return "try logout"

@app.route('/search_book')
def search_book():
    return "searching"

@app.route('/ranklist')
def ranklist():
    return "ranklist"

if __name__ == '__main__':
    app.run()
