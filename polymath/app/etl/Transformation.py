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
        self.stackDFS = []
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
            self.dictCategories[str(category[0])] = category

    def rowsToGraph(self, rows):
        for (category, subCategory) in rows:
            self.graph.addEdge(int(category),int(subCategory))
        
    def buildHTML(self,categoryID,(dataNodes, dataCategories)):
        
        def depthFirstSearch(node,parent):
            visited[node] = True
            self.stackDFS.append((node,parent))
            for nodeAdj in self.graph.adjNodes[node]:
                if (visited.get(nodeAdj) == False):
                    depthFirstSearch(nodeAdj,node)
            
        def rebootVisited():
            for nodeParent in self.graph.adjNodes:
                for nodeAdj in self.graph.adjNodes[nodeParent]:
                    visited[nodeAdj] = False

        def buildHTMLTagItem(category):
            CategoryID = '<li>CategoryID: '+str(category[0])+'</li>'
            CategoryName = '<li>CategoryName: '+str(category[1])+'</li>'
            CategoryLevel = '<li>CategoryLevel: '+str(category[2])+'</li>'
            BestOfferEnabled = '<li>BestOfferEnabled:'+str(category[3])+'</li>'
            AutoPayEnabled = '<li>AutoPayEnabled:'+str(category[4])+'</li>'
            return 'Info Category '+str(category[0])+CategoryID+CategoryName+CategoryLevel+BestOfferEnabled+AutoPayEnabled

        # Create a graph (tree).This represents the hierarchy of categories
        # Save categories into dic by using categoryid as key
        self.rowsToGraph(dataNodes)
        self.rowsToCategories(dataCategories)
        
        # Make a DFS traverse and detect when should build a html tag
        visited = {}
        rebootVisited()
        import sys
        #Parent of Node CategoryID might be negative infinite
        depthFirstSearch(categoryID,-sys.maxsize)
        stackDFS = self.stackDFS
        stackHTML = []
        while(stackDFS):
            (node,parent) = stackDFS.pop()
            if not stackHTML:
                category = self.dictCategories.get(str(node),None)
                if(category == None):
                    print('CategoriID no found')
                    import sys
                    sys.exit(1)
                    return
                htmlitems = buildHTMLTagItem(category)
                tag = "<ul>"+htmlitems+"</ul>"
                stackHTML.append(((node,parent),tag))
            else:
                ((n,p),t) = stackHTML[len(stackHTML)-1]
                # if node is parent of node built as htlm
                if(node == p):
                    # get all nodes from stackhtml
                    acc = ''
                    while(stackHTML):
                        ((n,p),t) = stackHTML.pop()
                        acc = t+acc
                    category = self.dictCategories[str(node)]
                    htmlitems = buildHTMLTagItem(category)
                    tag = "<ul>"+htmlitems+acc+"</ul>"
                    #tag = "<ul>"+str(node)+acc+"</ul>"
                    stackHTML.append(((node,parent),tag))
                else:
                    category = self.dictCategories[str(node)]
                    htmlitems = buildHTMLTagItem(category)
                    tag = "<ul>"+htmlitems+"</ul>"
                    #tag = "<ul>"+str(node)+"</ul>"
                    stackHTML.append(((node,parent),tag))

        (root,out) = stackHTML.pop()
        return out.encode('utf-8')
