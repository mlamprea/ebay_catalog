#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 08:35:57 2018

@author: Milton Lamprea
"""
import ConfigParser

from etl.ETL import ETL

class Main:
    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read('../resources/App.properties')
        self.etl = ETL(config)
        
    def getTreeNodesHTML(self,categoryID):
        self.etl.SQLToHTML(categoryID)

    def downloadData(self):
        self.etl.WSToSQL()
        print("OK")
        
    def __del__(self):
        self.prop = None
        

#if __name__ == "__main__":
    #app = Main()
    #app.getTreeNodes()

from optparse import OptionParser

def main():
    parser = OptionParser(usage="usage: ./categories [options] filename",
                          version="%prog 1.0")
    parser.add_option("-b", "--rebuild",
                      action="store_true",
                      dest="rebuild",
                      default=False,
                      help="Build database from Ebay Service")
    parser.add_option("-n", "--render",
                      action="store", 
                      dest="categoryID",
                      default="-1",
                      help="Render HTML associated to a CategoryID",)
    (options, args) = parser.parse_args()


    categoryID = int(options.categoryID)
    app = Main()
    if(options.rebuild):
        app.downloadData()
    else:
        print("Rendering HTML ",str(categoryID)+".hmtl")
        app.getTreeNodesHTML(categoryID)
        

if __name__ == '__main__':
    main()
     