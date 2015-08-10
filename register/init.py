#!/usr/bin/env python
# -*- coding: utf-8 -*-
#*******************************************************************************
# Description: https://docs.python.org/2/library/sqlite3.html
# Dependances:
# Date:
#*******************************************************************************

import sqlite3
conn = sqlite3.connect('register.db')

c = conn.cursor()

"""
CREATE TABLE users (
  id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  name text,
  password text,
  email text
);
"""

import datetime

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id integer primary key UTOINCREMENT NOT NULL, name TEXT, password TEXT, email TEXT)''')

# Insert a row of data
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

