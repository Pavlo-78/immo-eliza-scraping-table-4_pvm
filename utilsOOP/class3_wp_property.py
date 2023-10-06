import sys
import csv
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
sys.stdout.reconfigure(encoding='utf-8')
import class2_wp_links as c2


class wpage_property(c2.wpage_links):
    def __init__(self, desc, url, no):
        super().__init__(desc, url)
        self.no = no 
        # self.Postal_code = None


    def get_data_immoweb(self):
        #
        r = requests.get(self.url)
        #
        s = BeautifulSoup(r.text, "lxml")
        # get the tag 
        script_tag = s.find('script', type='text/javascript')
        # Get the text content from the <script> tag
        script_content = script_tag.string  
        # preparing to get jawa dictionary
        json_start = script_content.find('{')
        json_end = script_content.rfind('}')
        # get the row text of java dict
        json_text1 = script_content[json_start:json_end+1]
        # checking the data of the link - if the data is bad, stop and out with message "Error" 
        if json_text1[2:4] != 'id': # get "id" and check if it exists  
            return False
        # convert row java text of dict to python dict
        self.row_data = json.loads(json_text1) #print(type(json_data)) >> <class 'dict'>
      
        try:
            self.PropertyId = self.row_data["id"]            
        except (KeyError, TypeError):
            self.PropertyId = None

        try:
            self.Locality_Name = self.row_data["property"]["location"]["locality"]
        except (KeyError, TypeError):
            self.Locality_Name = None

        try:
            self.Postal_code = self.row_data["property"]["location"]["postalCode"]
        except (KeyError, TypeError):
            self.Postal_code = None

        try:
            self.Type_of_property = self.row_data["property"]["type"]
        except (KeyError, TypeError):
            self.Type_of_property = None

        try:
            self.Subtype_of_property = self.row_data["property"]["subtype"]
        except (KeyError, TypeError):
            self.Subtype_of_property = None

        try:
            self.Price = self.row_data["transaction"]["sale"]["price"]
        except (KeyError, TypeError):
            self.Price = None

        try:
            self.Type_of_sale = self.row_data["transaction"]["type"]
        except (KeyError, TypeError):
            self.Type_of_sale = None

        try:
            self.Number_of_rooms = self.row_data["property"]["bedroomCount"]
        except (KeyError, TypeError):
            self.Number_of_rooms = None

        try:
            self.Living_Area = self.row_data["property"]["netHabitableSurface"]
        except (KeyError, TypeError):
            self.Living_Area =None

        try:    
            self.Equipped_kitchen = self.row_data["property"]["kitchen"]["type"]
        except (KeyError, TypeError):   
            self.Equipped_kitchen = None

        try:
            self.Furnished = self.row_data["transaction"]["sale"]["isFurnished"]
        except (KeyError, TypeError):
            self.Furnished = None

        try:
            self.Open_fire = self.row_data["property"]["fireplaceExists"]
        except (KeyError, TypeError):
            self.Open_fire = None

        try:
            self.Terrace_YN = self.row_data["property"]["hasTerrace"]
        except (KeyError, TypeError):
            self.Terrace_YN = None

        try:
            self.TerraceSurface = self.row_data["property"]["hasTerrace"]
        except (KeyError, TypeError):
            self.TerraceSurface = None

        try:
            self.Garden_YN = self.row_data["property"]["hasGarden"]
        except (KeyError, TypeError):
            self.Garden_YN = None

        try:
            self.Garden_area = self.row_data["property"]["gardenSurface"]
        except (KeyError, TypeError):
            self.Garden_area = None

        try:
            self.Surface_of_good = self.row_data["property"]["building"]["streetFacadeWidth"]
        except (KeyError, TypeError):
            self.Surface_of_good = None

        try:
            self.Number_of_facades = self.row_data["property"]["building"]["facadeCount"]
        except (KeyError, TypeError):
            self.Number_of_facades = None

        try:
            self.Swimming_pool_YN = self.row_data["property"]["hasSwimmingPool"]
        except (KeyError, TypeError):
            self.Swimming_pool_YN = None

        try:
            self.State_of_building = self.row_data["property"]["building"]["condition"]
        except (KeyError, TypeError):
            self.State_of_building = None

        return True