
import sys
import csv
import json
from bs4 import BeautifulSoup
from datetime import datetime
sys.stdout.reconfigure(encoding='utf-8')
import class1_wp_home as c1
import class2_wp_links as c2
import class3_wp_property as c3


# ***************************
# MAINE DATA GATHERING
# ***************************


ooc_wpage_main=c1.w_page("immoweb","https://www.immoweb.be") 
ooc_wpage_searchsale = c2.wpage_links("webpage with all objects for SALE", 
                                   ooc_wpage_main.url +
                                   "/en/search/house-and-apartment/for-sale?countries") 


# getting links
# print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),"=", 'Collecting links is started...')
# lc=msg=ooc_wpage_searchsale.get_links(500)
# time=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
# msg1="Collecting links is finished."
# msg2="links are collected and saved to json."
# msg3= f"{time} {msg1} {lc} {msg2}"
# print(msg3)

#-- ПОСИЛАННЯ
# -----------
# open json file with urls 
with open('web_urls_.json', encoding='utf-8') as f: 
    # load json to (jurls) list of dictionaries with urls,no,num of page...
    jurls = json.load(f) 

#-- ОБ'ЄКТИ
# -----------
alldata_lst=[]
alldata_lst2=[]
pp=[]
# create immo objects by cycle each url-dict to extract url & no. "iobj" - object of immo property
for jurl in (jurls[0:2]): #dbg
# for jurl in (jurls):
    ob=f"iobj{jurl['No']}"
    no=jurl['No']
    ur=jurl["url"]
    pp.append(c3.wpage_property(ob, ur, no))

# ЗАВАНТАЖЕННЯ ІНФО В ОБ'ЄКТИ
# handeling all immo_oblects
for p in(pp):
    # get & set data to obj + feedback
    if p.get_data_immoweb()==True: # 
        # log_msg
        if int(p.no)%100==0: 
            log_msg = datetime.now().strftime("%d/%m/%Y %H:%M:%S") +"=" + p.no + 'links are proceeded'
            print(log_msg)            
    else: 
            print("bad link=",p.no)
            continue # if it run into bad link  

    # reading all attibuties names from object 
    att=['no', 'url', 'PropertyId', 'Locality_Name', 'Postal_code', 'Type_of_property', 
         'Subtype_of_property', 'Price', 'Type_of_sale', 'Number_of_rooms', 'Living_Area', 
         'Equipped_kitchen', 'Furnished', 'Open_fire', 'Terrace_YN', 'TerraceSurface', 
         'Garden_YN', 'Garden_area', 'Surface_of_good', 'Number_of_facades', 'Swimming_pool_YN', 
         'State_of_building']
    # Type_of_sale



    # all data obj
    obj_data_dict = {} 
    #  make record
    for vn in(att):
        obj_data_dict[vn] = getattr(p, vn)
    #  add record in list for CSV    
    alldata_lst.append(obj_data_dict)
    alldata_lst2.append(p.ddict)
print(alldata_lst2)


# preparing save dict to CSV 
field_names = alldata_lst2[0].keys() # get all keys od dict for csv.DictWriter
# print(field_names)
# writing dict to CSV
with open('web_urls_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(alldata_lst2)


print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "= The scrapping is fifnished.")
  

