#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 18:07:57 2018

@author: Milton Lamprea
"""
from persistence.SchemaBuilder import SchemaBuilder

class Loader:
    def __init__(self, prop):
        try:
            
            self.prop = prop
            dbname = self.prop.get('DB','dbname')
            self.builder = SchemaBuilder(dbname)
            
        except Exception:
            print('Error: can\'t create database scheme ')

    def preLoadSQL(self):
        try:
            filename = self.prop.get('DB','filename')
            file = open(filename)
            script = file.read()
            file.close();
            self.builder.buildSchema(script);
        except IOError:
            print('Error: can\'t find file or read data ',filename)
        except Exception as e:
            print('It can\'t  prepare database ',e)        


    def loadSQL(self,data):
        try:
            stmt = self.prop.get('DB','stmtInsert')
            self.builder.builData(stmt,data)       
        except Exception as e:
            print('It can\'t save into table ',e)

    def loadHTML(self,htmlString,categoryID):
        try:
            filename = self.prop.get('HTML','templateHTML')
            file = open(filename)
            script = file.read()
            file.close()
            htmldoc = str(script).replace("HTMLTEXT",str(htmlString))
            fileOutputName = str(categoryID)+".html"
            fileOutput = open(fileOutputName,"w")
            fileOutput.write(htmldoc) 
            fileOutput.close() 
            print(fileOutputName+" generated.")
            
        except IOError:
            print('Loader -> Error: can\'t find file or read data ',filename)
        except Exception as e:
            print('Loader -> It can\'t generate HTML file ',e)