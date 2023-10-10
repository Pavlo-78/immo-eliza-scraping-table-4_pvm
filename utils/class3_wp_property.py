import sys
import json
import requests
from bs4 import BeautifulSoup
sys.stdout.reconfigure(encoding='utf-8')
import utils.class2_wp_links as c2 #utils.

# A class of the web page of a real estate object, that inherits from the class of the search page 
# The inheritance is used for educational purposes
class wpage_property(c2.wpage_links):
    def __init__(self, desc, url, no):
        super().__init__(desc, url)
        self.no = str(no)
        self.ddict = {}

    def get_data_immoweb(self):
        """
        A function that collects the data of this real estate ad according to the web address 
        of the "url" property of this class object

        :return: writes data to the "ddict" property of this class object - 
        (fills this dictionary with data)
        """  
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
        # converting all info to json format and save for debuging
        # json_dbg = "link number = {self.no}" 
        # print(type(json_dbg))
        json_dbg = json.dumps(self.row_data, indent=2, ensure_ascii=False) #indent=2 >> pretty-printing 
        json_dbg = f"link number = {self.no}, " + json_dbg
        with open("web_dict---.json", "w", encoding='utf-8') as var_jf: var_jf.write(json_dbg) 
    # ---------------------------------
        if self.row_data["property"]["type"] in ["APARTMENT_GROUP","HOUSE_GROUP"]:  
            lst_urls2=[]
            soupF = s.find_all('a', class_='classified__list-item-link')
            
            # Extract and print the ad links
            var_x=1
            for e in soupF:        
                if e:
                    href = e.get("href")
                    # print(var_i, var_ii, var_x, href)
                    noo = str(self.no) + "/" + str(var_x)
                    lst_urls2.append({"No":noo, "Nl":var_x, "url":href})
                    var_x+=1  
            var_json = json.dumps(lst_urls2, indent=2, ensure_ascii=False) #indent=2 >> pretty-printing 
            # print(var_json)     
            with open("web_urls_2.json", "a", encoding='utf-8') as var_jf:
                var_jf.write(var_json) 
    # ---------------------------------

        self.ddict["no"]    = self.no
        self.ddict["url"]   = self.url


        try: # --- id
            t = self.row_data["id"]            
        except (KeyError, TypeError):
            t = None
        self.ddict["id"] = t


        try: # --- Locality_Name       
            t = self.row_data["property"]["location"]["locality"]           
        except (KeyError, TypeError):
           t = None
        self.ddict["Locality_Name"] = t


        try: # --- Postal_code
            t = self.row_data["property"]["location"]["postalCode"]           
        except (KeyError, TypeError):
            t = None
        self.ddict["Postal_code"] = t


        try: # --- Type_of_property
            t = self.row_data["property"]["type"]            
        except (KeyError, TypeError):
            t = None
        self.ddict["Type_of_property"] = t


        try: # --- Subtype_of_property
            t   = self.row_data["property"]["subtype"]            
        except (KeyError, TypeError):
            t = None
        self.ddict["Subtype_of_property"] = t


        try: # --- Price
            t = self.row_data["transaction"]["sale"]["price"]           
        except (KeyError, TypeError):
            t = None
        self.ddict["Price"] = t


        try: # --- Type_of_sale
            t  = self.row_data["transaction"]["type"]            
        except (KeyError, TypeError):
            t= None
        self.ddict["Type_of_sale"] = t


        try: # --- Number_of_rooms
            t = self.row_data["property"]["bedroomCount"]            
        except (KeyError, TypeError):
            t = None
        self.ddict["Number_of_rooms"]=t            


        try: # --- Living_Area
            t = self.row_data["property"]["netHabitableSurface"]            
        except (KeyError, TypeError):
            t = None
        self.ddict["Living_Area"]=t


        try: # --- Equipped_kitchen
            t = self.row_data["property"]["kitchen"]["type"]            
        except (KeyError, TypeError):   
            t = None
        self.ddict["Equipped_kitchen"] = t
        
        
        try: # --- Furnished   
            t = str(self.row_data["transaction"]["sale"]["isFurnished"])
        except (KeyError, TypeError):   
            t = None
        self.ddict["Furnished"] = t
     
        
        try: # --- Open_fire   
            t = str(self.row_data["property"]["fireplaceExists"])
        except (KeyError, TypeError):   
            t = None
        self.ddict["Open_fire"] = t

        
        try: # --- Terrace_YN   
            t = str(self.row_data["property"]["hasTerrace"])
        except (KeyError, TypeError):   
            t = None
        self.ddict["Terrace_YN"] = t


        try: # --- TerraceSurface
            t = self.row_data["property"]["terraceSurface"]            
        except (KeyError, TypeError):
            t = None
        self.ddict["TerraceSurface"] = t


        try: # -- Garden_YN
            t = self.row_data["property"]["hasGarden"]            
        except (KeyError, TypeError):
            t = None
        self.ddict["Garden_YN"] = t


        try: # --- Garden_area
            t = self.row_data["property"]["gardenSurface"]            
        except (KeyError, TypeError):
            t = None
        self.ddict["Garden_area"] = t


        try: # --- Surface_of_good
            t = self.row_data["property"]["building"]["streetFacadeWidth"]            
        except (KeyError, TypeError):
            t = None
        self.ddict["Surface_of_good"]=t


        try: # -- Number_of_facades
            t = self.row_data["property"]["building"]["facadeCount"]            
        except (KeyError, TypeError):
            t = None
        self.ddict["Number_of_facades"] = t


        try: # -- Swimming_pool_YN
            t = self.row_data["property"]["hasSwimmingPool"]            
        except (KeyError, TypeError):
            t = None
        self.ddict["Swimming_pool_YN"] = t


        try: # -- State_of_building
            t = self.row_data["property"]["building"]["condition"]            
        except (KeyError, TypeError):
            t = None
        self.ddict["State_of_building"] = t

        # -------------------------------------------- additional info
        try: # -- ipiNo
            t = self.row_data["customers"][0]["ipiNo"]            
        except (KeyError, TypeError):
            t = None
        self.ddict["ipiNo"] = t

        try: # -- customer_type
            t = self.row_data["customers"][0]["type"]            
        except (KeyError, TypeError):
            t = None
        self.ddict["customer_type"] = t

        try: # -- regionCode
            t = self.row_data["property"]["location"]["regionCode"]         
        except (KeyError, TypeError):
            t = None
        self.ddict["regionCode"] = t

        try: # -- location region
            t = self.row_data["property"]["location"]["region"]         
        except (KeyError, TypeError):
            t = None
        self.ddict["region"] = t

        try: # -- location province
            t = self.row_data["property"]["location"]["province"]         
        except (KeyError, TypeError):
            t = None
        self.ddict["province"] = t

        try: # -- location_type
            t = self.row_data["property"]["location"]["type"]         
        except (KeyError, TypeError):
            t = None
        self.ddict["location_type"] = t

        try: # -- seller_type-------------------------------+
            t = self.row_data["customers"][0]["type"]             
        except (KeyError, TypeError):
            t = None
        self.ddict["seller_type"] = t
        
        try: # -- seller_name
            t = self.row_data["customers"][0]["name"]             
        except (KeyError, TypeError):
            t = None
        self.ddict["seller_name"] = t

        try: # --seller_website
            t = self.row_data["customers"][0]["website"]             
        except (KeyError, TypeError):
            t = None
        self.ddict["seller_website"] = t


        return True
    


    