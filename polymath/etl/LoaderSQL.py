#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 18:07:57 2018

@author: Milton Lamprea
"""
from SchemaBuilder import SchemaBuilder

class LoaderSQL:
    def __init__(self):
        try:
            dbname = '../data/ebay.db'
            self.builder = SchemaBuilder(dbname)
        except Exception:
            print('Error: can\'t create database scheme ',dbname)
        
    def load(self,data):
        try:
            #property
            filename = '../resources/db_schema.sql'
            file = open(filename);
            script = file.read()
            file.close();
            # property
            self.builder.buildSchema(script);
            stmt = 'INSERT INTO Category VALUES (?,?,?,?,?,?)'
            self.builder.builData(stmt,data)
            
        except IOError:
            print('Error: can\'t find file or read data ',filename)
        except Exception as e:
            print('It can\'t save into table ',e)
