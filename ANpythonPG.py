# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 17:47:14 2021

@author: Anthony
"""
import requests
import dataset

class ANimport():
    my_headers = {'OSDI-API-Token' : 'e08d0fc56391ce71fdcc71c91eae45d5'}
    tables = {}
    link = ""
    def connect_an(self):
        response = requests.get("https://actionnetwork.org/api/v2/", headers = ANimport.my_headers)
        res = response.json()
        if (res["motd"] == "Welcome to the Action Network OSDI API v2 Entry Point!"):
            return("OK")
        else: 
            return("No Connection")
        
    def get_all_of_table(self, table_string):
        response = requests.get("https://actionnetwork.org/api/v2/" + table_string +"/?background_request=true", headers =ANimport.my_headers)
        self.link = response.json()
        self.tables[table_string] = self.link["_embedded"]["osdi:" + table_string]
        while ("next" in self.link["_links"].keys()) :
            self.link = requests.get(self.link["_links"]["next"]["href"] + "&background_request=true", headers =self.my_headers).json()
            self.tables[table_string] = self.tables[table_string] + self.link["_embedded"]["osdi:" + table_string]
            print(str(len(self.tables[table_string])) + " " + table_string)
            
    def status(self):
        print("Downloaded items")
        for t in list(self.tables.keys()):
            print(str(len(self.tables[t])) + " " + t)

    
            
ai = ANimport()        
a = ai.connect_an()
ai.get_all_of_table("people")
ai.get_all_of_table("events")
ai.get_all_of_table("petitions")
ai.get_all_of_table("fundraising_pages")
ai.get_all_of_table("donations")
ai.get_all_of_table("queries")
ai.get_all_of_table("forms")
ai.get_all_of_table("tags")
ai.get_all_of_table("lists")
ai.get_all_of_table("wrappers")
ai.get_all_of_table("messages")

ai.status()
#ai.get_all_of_table("person_signup_helper") - this didn't work
#ai.get_all_of_table("advocacy_campaigns") - this didn't work
#ai.get_all_of_table("metadata") - this didn't work

