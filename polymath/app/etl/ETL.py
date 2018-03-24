#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 18:45:31 2018

@author: Milton Lamprea

"""
from Extractor import Extractor
from Transformation import Transformation
from Loader import Loader

"""
ETL (Extract, Transform and Load) Process

"""
class ETL:
    def __init__(self, prop):
        self.prop = prop
        self.extractor = Extractor(prop)
        self.transformer = Transformation(prop)
        self.loader = Loader(prop)
        
    def WSToSQL(self):
        categoriesLevel1 = self.transformer.transformXML(self.extractor.extractLevel1FromEbayService())
        self.loader.preLoadSQL()
        size = len(categoriesLevel1)
        for (idx,category) in enumerate(categoriesLevel1):
            categoryID = category[0]
            print("Building "+str(int(idx)*100/size)+"%")
            self.loader.loadSQL(self.transformer.transformXML(self.extractor.extractFromEbayService(categoryID)))
        
    def SQLToHTML(self,categoryID):
        dataNodes = self.extractor.extractNodesFromDB()
        self.transformer.rowsToGraph(dataNodes)
        dataCategories = self.extractor.extractCategoriesFromDB()
        self.transformer.rowsToCategories(dataCategories)
        html = self.transformer.depthFirstSearch(categoryID)
        #html = self.transformer.breadthFirstSearch(categoryID)
        return self.loader.loadHTML(html)

        
 
       
# =============================================================================
# if __name__ == "__main__":
#     etl = ETL()
#     #data2 = [("2222","11111", "aaaaaa", "3","1","1"),(11111,11111, "aaaaaappppp", 3,1,1),(22221,11111, "aaaaaa1", 3,1,1)]
#     data2 = [('151737', '151726', 'Other Antique Non-U.S. Silver', '4', 'true', 'true'), ('169270', '20096', 'Unknown', '3', 'true', 'true'), ('171168', '20096', 'Price Guides & Publications', '3', 'true', 'true')]
#     etl.WSToSQL()
# =============================================================================
        