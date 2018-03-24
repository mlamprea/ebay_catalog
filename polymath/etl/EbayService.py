#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 20:56:23 2018

@author: Milton Lamprea
"""

import requests
import sys

class EbayService:
    
    def __init__(self, prop):
        self.prop = prop
        # endpoint
        self.URL = self.prop.get('ebayservice','URL')
         
        # Headers
        self.call_name =  self.prop.get('ebayservice','call_name')
        self.app_name = self.prop.get('ebayservice','app_name')
        self.cert_name = self.prop.get('ebayservice','cert_name')
        self.dev_name = self.prop.get('ebayservice','dev_name')
        self.site_id = self.prop.get('ebayservice','site_id')
        self.compatibility = self.prop.get('ebayservice','compatibility')
        self.data_function_api = self.prop.get('ebayservice','data_function_api')
        self.data_function_api_level1 = self.prop.get('ebayservice','data_function_api_level1')
         
        # defining a params dict for the parameters to be sent to the API
        self.headers = {'X-EBAY-API-CALL-NAME':self.call_name, 'X-EBAY-API-APP-NAME': self.app_name,'X-EBAY-API-CERT-NAME':self.cert_name,'X-EBAY-API-DEV-NAME':self.dev_name,'X-EBAY-API-SITEID':self.site_id,'X-EBAY-API-COMPATIBILITY-LEVEL':self.compatibility}
            
    def retrieveCategories(self,categoryID):
        try:
            # sending post request and saving the response as response object
            request = str(self.data_function_api).replace("PARAM1",str(categoryID))
            resp = requests.post(url = self.URL, headers = self.headers, data = request)
            # extracting data
            xmlString = resp.text
            #print(resp.status_code)            
            return xmlString
         
        except requests.exceptions.Timeout as ex_time_out:
            print(ex_time_out)
            # Maybe set up for a retry, or continue in a retry loop
        except requests.exceptions.TooManyRedirects:
            print('URL was bad and try a different one')
        except requests.exceptions.RequestException as e:
            print('Error HTTP')
            print(e)
            sys.exit(1)


    def retrieveLevel1(self):
        try:
            # sending post request and saving the response as response object
            resp = requests.post(url = self.URL, headers = self.headers, data = self.data_function_api_level1)
            # extracting data
            xmlString = resp.text
            fileOutput = open(self.prop.get('ebayservice','fileOutput'),"w")
            fileOutput.write(xmlString) 
            fileOutput.close() 
            #print(resp.status_code)
            
            return xmlString
         
        except requests.exceptions.Timeout as ex_time_out:
            print(ex_time_out)
            # Maybe set up for a retry, or continue in a retry loop
        except requests.exceptions.TooManyRedirects:
            print('URL was bad and try a different one')
        except requests.exceptions.RequestException as e:
            print('Error HTTP')
            print(e)
            sys.exit(1)