#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 22:06:43 2018

@author: Milton Lamprea
"""
from EbayService import EbayService
from DBService import DBService

class Extractor:
    def __init__(self,prop):
        self.prop = prop

    def extractFromEbayService(self):
        service = EbayService()
        xmlString = service.retrieveCategories()
        return xmlString

    def extractFromDB(self,dbname, query):
        dbService  = DBService(dbname)
        data = dbService.fetchData(query)
        return data
    
    def extractNodesFromDB(self):
        dbname = self.prop.get('DB','dbname')
        qNodes = self.prop.get('DB','qNodes')
        return self.extractFromDB(dbname, qNodes)

    def extractCategoriesFromDB(self):
        dbname = self.prop.get('DB','dbname')
        qCategories = self.prop.get('DB','qCategories')
        return self.extractFromDB(dbname, qCategories)
