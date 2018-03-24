#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 07:54:19 2018

@author: Milton Lamprea
"""

from DBConnection import DBConnection

class DBService:
    def __init__(self,dbname):
        self.dbConnectionFactory = DBConnection(dbname)
        self.dbConnection = self.dbConnectionFactory.createConnection();
        self.dbCursor = self.dbConnection.cursor()
    
    def fetchData(self, query):
        try:
            rows = self.dbCursor.execute(query).fetchall()
            return rows
        except Exception as e:
            print('DBService ->',e)
            import sys
            sys.exit(1)
        
        pass
        
    def __del__(self):
        self.dbCursor.close()
        self.dbConnectionFactory.closeConnection(self.dbConnection)
        