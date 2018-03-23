#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 22:27:17 2018

@author: Milton Lamprea
"""

import xml.etree.ElementTree as ET
from Graph import Graph


class Transformation:
    def __init__(self,prop):
        self.ns = prop.get('ebayservice','ns')
        self.graph = Graph()
        self.dictCategories = {}
        self.visited = {}
        pass
    
    def transformXML(self, xml):
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
    
    def rowsToGraph(self, rows):
        for (category, subCategory) in rows:
            self.graph.addEdge(category,subCategory)
        
    def rowsToCategories(self, rows):
        for category in rows:
            self.dictCategories[category[0]] = category
        #print(self.dictCategories)    

    def depthFirstSearch(self):
        
        def depthFirstSearch_Aux(node):
            print("Visiting ",node)
            visited[node] = True
            newVisited = {k: v for k,v in visited.items() if v}
            for nodeAdj in self.graph.adjNodes[node]:
                if (newVisited.get(nodeAdj) == False):
                    depthFirstSearch_Aux(nodeAdj)
        
        
        def rebootVisited():
            for nodeParent in self.graph.adjNodes:
                for nodeAdj in self.graph.adjNodes[nodeParent]:
                    visited[nodeAdj] = False

        visited = {}
        for nodeAdj in self.graph.adjNodes:
            rebootVisited()
            depthFirstSearch_Aux(nodeAdj)
            
            
        
        
        
        