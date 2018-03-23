#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 11:41:08 2018

@author: Milton Lamprea
"""


import sqlite3

class DBConnection:
    def __init__(self,dbname):
        self.dbname = dbname   
        
    def createConnection(self):
        try:
            connection = sqlite3.connect(self.dbname)
            return connection
        except Exception as e:
            print("App can not access database")
            print(e)
            return None

    def closeConnection(self,connection):
        connection.close()
            

    