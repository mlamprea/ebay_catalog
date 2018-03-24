#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 22:27:17 2018

@author: Milton Lamprea
"""

import xml.etree.ElementTree as ET
from cs.Graph import Graph


class Transformation:
    def __init__(self,prop):
        self.ns = prop.get('ebayservice','ns')
        self.graph = Graph()
        self.dictCategories = {}
        self.visited = {}
        pass
    
    def transformXML(self, xml):
        out = []
        root = ET.fromstring(xml.encode('utf-8'))
        for categories in root.findall('{0}CategoryArray'.format(self.ns)):
            category = categories.findall('{0}Category'.format(self.ns))
            for data in category:
                categoryID = data.find('{0}CategoryID'.format(self.ns)).text
                categoryParentID = data.find('{0}CategoryParentID'.format(self.ns)).text
                categoryName = data.find('{0}CategoryName'.format(self.ns)).text
                categoryLevel = data.find('{0}CategoryLevel'.format(self.ns)).text
                if(data.find('{0}BestOfferEnabled'.format(self.ns))==None):
                    bestOfferEnabled = None
                else:
                    bestOfferEnabled = data.find('{0}BestOfferEnabled'.format(self.ns)).text
                if(data.find('{0}AutoPayEnabled'.format(self.ns)) == None):
                    autoPayEnabled = None
                else:
                    autoPayEnabled = data.find('{0}AutoPayEnabled'.format(self.ns)).text
                out.append((int(categoryID),int(categoryParentID),categoryName,int(categoryLevel),bestOfferEnabled,autoPayEnabled))
        return out
    
    def rowsToCategories(self, rows):
        for category in rows:
            self.dictCategories[category[0]] = category
        #print(self.dictCategories)    

    def rowsToGraph(self, rows):
        for (category, subCategory) in rows:
            self.graph.addEdge(int(category),int(subCategory))
        
    def depthFirstSearch(self,categoryID):
        
        def depthFirstSearch_Aux(node, htmlist):
            visited[node] = True
            print("visiting ",node)
            print(self.graph.adjNodes[node])
            for nodeAdj in self.graph.adjNodes[node]:
                print(nodeAdj,visited.get(nodeAdj) )
                if (visited.get(nodeAdj) == False):
                      htmlist = depthFirstSearch_Aux(nodeAdj,htmlist)
            return "<ul>"+str(node)+htmlist+"</ul>"
            
        def rebootVisited():
            for nodeParent in self.graph.adjNodes:
                for nodeAdj in self.graph.adjNodes[nodeParent]:
                    visited[nodeAdj] = False

        visited = {}
        rebootVisited()
        #print(visited)
        out = depthFirstSearch_Aux(categoryID,'')
        return out.encode('utf-8')
        
        
        
        