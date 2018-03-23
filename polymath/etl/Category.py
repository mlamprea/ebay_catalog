#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 10:20:16 2018

@author: Milton Lamprea
"""

class Category:
    
    def __init__(self, categoryID, categoryName, CategoryLevel, BestOfferEnabled,AutoPayEnabled):
        self.categoryID = categoryID
        self.categoryName = categoryName
        self.CategoryLevel = CategoryLevel
        self.BestOfferEnabled = BestOfferEnabled
        self.AutoPayEnabled = AutoPayEnabled
    