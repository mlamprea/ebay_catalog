#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 22:06:43 2018

@author: Milton Lamprea
"""
from EbayService import EbayService

class Extractor:
    def __init__(self):
        '''
        Load properties WS Ebay
        '''
        pass

    def extract(self):
        service = EbayService()
        xmlString = service.retrieveCategories()
        return xmlString
