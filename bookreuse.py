#!/usr/bin/env python
import sqlite3
from flask import Flask, request, session, g, redirect, url_for,\
        abort, render_template, flash
from pyquery import PyQuery as pq
# configuration
DATABASE = './book.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = '123456'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route('/')
def index():
    homebook = []
    d = pq(url="http://book.douban.com/tag/%E7%A7%91%E6%99%AE")
    for i in d('li.subject-item').items():
        imgsrc = i('img').attr('src')
        info   = i('div.info')('a').attr('title')
        url    = i('div.info')('a').attr('href')
        homebook.append(dict(src=imgsrc, name=info, url=url))
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
