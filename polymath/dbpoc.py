#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 21:37:50 2018

@author: dev02
"""

import sqlite3

c =  connection = sqlite3.connect('data/ebay.db')
cursor = c.cursor()
stmt = 'INSERT INTO Category VALUES (?,?,?,?,?,?,?)'
data = [(2222,11111, "aaaaaa", 3,1,1,1),]
rep = cursor.executemany(stmt,data);
print(rep)
c.commit();
cursor.close
c.close()