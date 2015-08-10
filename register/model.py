#!/usr/bin/env python
# -*- coding: utf-8 -*-
#*******************************************************************************
# Description:
# Dependances:
# Date:
#*******************************************************************************

import web

#db = web.database(dbn='mysql', db='wiki', user='justin')
db = web.database(dbn='sqlite', db='register.db')

def get_pages():
    return db.select('pages', order='id DESC')

def get_page_by_url(url):
    try:
        return db.select('pages', where='url=$url', vars=locals())[0]
    except IndexError:
        return None

def get_page_by_id(id):
    try:
        return db.select('pages', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def get_users():
    return db.select('users',order = 'id DESC')

def new_user(name,password,email):
    db.insert('users', name=name, password=password, email=email)

def get_userbyname(name):
    if db.select('users', where = 'name = $name',vars=locals()):
        return db.select('users', where ='name=$name',vars=locals())[0]
    else:
        return None

def get_userbyemail(email):
    return db.select('users', where ='email=$email',vars=locals())[0]


def new_page(url, title, text):
    db.insert('pages', url=url, title=title, content=text)

def del_page(id):
    db.delete('pages', where="id=$id", vars=locals())

def update_page(id, url, title, text):
    db.update('pages', where="id=$id", vars=locals(),
        url=url, title=title, content=text)
