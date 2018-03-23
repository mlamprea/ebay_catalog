#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 22:27:17 2018

@author: Milton Lamprea
"""
import xml.etree.ElementTree as ET
class SQLTransformation:
    def __init__(self):
        self.ns = '{urn:ebay:apis:eBLBaseComponents}'
        pass
    def transform(self, xml):
        out = []
        root = ET.fromstring(xml)
        for categories in root.findall('{0}CategoryArray'.format(self.ns)):
            category = categories.findall('{0}Category'.format(self.ns))
            for data in category:
                categoryID = data.find('{0}CategoryID'.format(self.ns)).text
                categoryParentID = data.find('{0}CategoryParentID'.format(self.ns)).text
                categoryName = data.find('{0}CategoryName'.format(self.ns)).text
                categoryLevel = data.find('{0}CategoryLevel'.format(self.ns)).text
                bestOfferEnabled = data.find('{0}BestOfferEnabled'.format(self.ns)).text
                autoPayEnabled = data.find('{0}AutoPayEnabled'.format(self.ns)).text
                out.append((int(categoryID),int(categoryParentID),categoryName,int(categoryLevel),bestOfferEnabled,autoPayEnabled))
        return out
        