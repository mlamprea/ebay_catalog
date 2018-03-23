#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 10:55:13 2018

@author: Milton Lamprea
"""
from collections import defaultdict

class Graph:
    def __init__(self):
        self.adjNodes = defaultdict(list)
    
    def addEdge(self,idNode, node):
        self.adjNodes[idNode].append(node)
        