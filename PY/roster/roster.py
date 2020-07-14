# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 10:54:37 2020

@author: Sahil Shaikh
"""


import json
import sqlite3

conn=sqlite3.connect('rosterdb.sqlite')
cur=conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT UNIQUE);

CREATE TABLE Course(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
title TEXT UNIQUE); 

CREATE TABLE Member(
user_id INTEGER,
course_id INTEGER,
role INTEGER,
PRIMARY KEY (user_id,course_id));              
''')

fname=input('Enter File Name:')
if len(fname)<1: fname='roster_data.json'
str_data=open(fname).read()
json_data=json.loads(str_data)

for entry in json_data:
    name=entry[0]
    title=entry[1]
    role=entry[2]
    if role==0: role_mean='Student'
    else: role_mean='Instructor'
    print(name,role_mean,title)
    
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)',(name,))
    cur.execute('SELECT id FROM User WHERE name=?',(name,))
    user_id=cur.fetchone()[0]
    
    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)',(title,))
    cur.execute('SELECT id FROM Course WHERE title=?',(title,))
    course_id=cur.fetchone()[0]
    
    cur.execute('INSERT OR REPLACE INTO Member (user_id,course_id,role) VALUES (?,?,?)',(user_id,course_id,role))

    conn.commit()    


