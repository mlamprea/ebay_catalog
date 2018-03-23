#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 08:35:57 2018

@author: Milton Lamprea
"""
import ConfigParser

from ETL import ETL

class Main:
    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read('../resources/App.properties')
        
        print("Main - Properties")
        print(config.get('DB','dbname'))
        self.etl = ETL(config)
        
    def getTreeNodes(self):
        self.etl.SQLToHTML()
        
    def __del__(self):
        self.prop = None
        

if __name__ == "__main__":
    app = Main()
    app.getTreeNodes()
     