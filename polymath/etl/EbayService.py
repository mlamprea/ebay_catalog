#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 20:56:23 2018

@author: Milton Lamprea
"""

"""
Parse XML and save to SQLLite
1 - parser
2 - save somewhere else 
3- design data model OK
4- save xml into model
4- build html sample
5 - built html parser
6- build menu opts command line
7- load conf file yaml to load program

"""


import requests
import sys
 
# endpoint
URL = "https://api.sandbox.ebay.com/ws/api.dll"
 
# Headers
call_name = "GetCategories"
app_name = "EchoBay62-5538-466c-b43b-662768d6841"
cert_name = "00dd08ab-2082-4e3c-9518-5f4298f296db"
dev_name = "16a26b1b-26cf-442d-906d-597b60c41c19"
site_id = "0"
compatibility = "861"
data_function_api = '<?xml version="1.0" encoding="utf-8"?><GetCategoriesRequest xmlns="urn:ebay:apis:eBLBaseComponents"><RequesterCredentials><eBayAuthToken>AgAAAA**AQAAAA**aAAAAA**PlLuWA**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4GlDpaDpAudj6x9nY+seQ**LyoEAA**AAMAAA**wSd/jBCbxJHbYuIfP4ESyC0mHG2Tn4O3v6rO2zmnoVSF614aVDFfLSCkJ5b9wg9nD7rkDzQayiqvwdWeoJkqEpNQx6wjbVQ1pjiIaWdrYRq+dXxxGHlyVd+LqL1oPp/T9PxgaVAuxFXlVMh6wSyoAMRySI6QUzalepa82jSQ/qDaurz40/EIhu6+sizj0mCgjcdamKhp1Jk3Hqmv8FXFnXouQ9Vr0Qt+D1POIFbfEg9ykH1/I2CYkZBMIG+k6Pf00/UujbQdne6HUAu6CSj9wGsqQSAEPIXXvEnVmtU+6U991ZUhPuA/DMFEfVlibvNLBA7Shslp2oTy2T0wlpJN+f/Jle3gurHLIPc6EkEmckEpmSpFEyuBKz+ix4Cf4wYbcUk/Gr3kGdSi20XQGu/ZnJ7Clz4vVak9iJjN99j8lwA2zKW+CBRuHBjZdaUiDctSaADHwfz/x+09bIU9icgpzuOuKooMM5STbt+yJlJZdE3SRZHwilC4dToTQeVhAXA4tFZcDrZFzBmJsoRsJYrCdkJBPeGBub+fqomQYyKt1J0LAQ5Y0FQxLHBIp0cRZTPAuL/MNxQ/UXcxQTXjoCSdZd7B55f0UapU3EsqetEFvIMPxCPJ63YahVprODDva9Kz/Htm3piKyWzuCXfeu3siJvHuOVyx7Q4wyHrIyiJDNz5b9ABAKKauxDP32uqD7jqDzsVLH11/imKLLdl0U5PN+FP30XAQGBAFkHf+pAvOFLrdDTSjT3oQhFRzRPzLWkFg</eBayAuthToken></RequesterCredentials><CategoryParent>20081</CategoryParent><DetailLevel>ReturnAll</DetailLevel></GetCategoriesRequest>'
 
# defining a params dict for the parameters to be sent to the API
headers = {'X-EBAY-API-CALL-NAME':call_name, 'X-EBAY-API-APP-NAME': app_name,'X-EBAY-API-CERT-NAME':cert_name,'X-EBAY-API-DEV-NAME':dev_name,'X-EBAY-API-SITEID':site_id,'X-EBAY-API-COMPATIBILITY-LEVEL':compatibility}

class EbayService:
    
    def retrieveCategories(self):
        try:
            # sending post request and saving the response as response object
            resp = requests.post(url = URL, headers = headers, data = data_function_api)
            # extracting data
            xmlString = resp.text
            print(resp.status_code)
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
            