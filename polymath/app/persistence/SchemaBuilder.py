#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 17:35:06 2018

@author: Milton Lamprea
"""
from DBConnection import DBConnection

class SchemaBuilder:
     def __init__(self,dbname):
        self.dbConnectionFactory = DBConnection(dbname)
        self.dbConnection = self.dbConnectionFactory.createConnection();
        self.dbCursor = self.dbConnection.cursor()
      
     def buildSchema(self,script):
        try:
            self.dbCursor.executescript(script)
            self.dbConnection.commit()
            return True
        except Exception as e:
            print('BuilderDatabase-->: ',e)
            return False
        
     def builData(self,stmt,data):
        try:
            #print('inserting ',data)
            self.dbCursor.executemany(stmt,data)
            self.dbConnection.commit()
            return True
        except Exception as e:
            print('BuilderCategories -->: ',e)
            return False
    
     def __del__(self):
        #print("destroying .. schema builder")
        self.dbCursor.close()
        self.dbConnectionFactory.closeConnection(self.dbConnection)
        