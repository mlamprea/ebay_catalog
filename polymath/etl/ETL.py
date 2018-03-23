#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 18:45:31 2018

@author: Milton Lamprea

"""
from Extractor import Extractor
from Transformation import Transformation
from LoaderSQL import LoaderSQL

"""
ETL (Extract, Transform and Load) Process

"""
class ETL:
    def __init__(self, prop):
        self.prop = prop
        self.extractor = Extractor(prop)
        self.transformer = Transformation(prop)
        
    def WSToSQL(self):
        LoaderSQL().load(Transformation().transformXML(Extractor().extractFromEbayService()))
        
    def SQLToHTML(self):
        dataNodes = self.extractor.extractNodesFromDB()
        self.transformer.rowsToGraph(dataNodes)
        dataCategories = self.extractor.extractCategoriesFromDB()
        self.transformer.rowsToCategories(dataCategories)
        self.transformer.depthFirstSearch();

        
        pass
        
 
       
# =============================================================================
# if __name__ == "__main__":
#     etl = ETL()
#     #data2 = [("2222","11111", "aaaaaa", "3","1","1"),(11111,11111, "aaaaaappppp", 3,1,1),(22221,11111, "aaaaaa1", 3,1,1)]
#     data2 = [('151737', '151726', 'Other Antique Non-U.S. Silver', '4', 'true', 'true'), ('169270', '20096', 'Unknown', '3', 'true', 'true'), ('171168', '20096', 'Price Guides & Publications', '3', 'true', 'true')]
#     etl.WSToSQL()
# =============================================================================
        