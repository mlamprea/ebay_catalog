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
        return self.loader.loadHTML(self.transformer.buildHTML(categoryID,self.extractor.extractTreeFromDB()),categoryID)

        