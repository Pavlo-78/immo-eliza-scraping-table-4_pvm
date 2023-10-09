import sys
import csv
import json
from pip import datetime
sys.stdout.reconfigure(encoding='utf-8')
import class1_wp_home as c1
import class2_wp_links as c2
import class3_wp_property as c3


def proc_links(coumter, file_json):
    """
    A function that reads links from the specified json file and starts processing links one by one

    :return: list of dictionaries with information from the web page. One dictionary is returned for each json link. 
    If there are 10 links in the json file, it will return one list with 10 dictionaries
    """      
    # open json file with ordinary links to (jurls) list
    print( datetime.now().strftime("%d/%m/%Y %H:%M:%S") +" = Processing links from " + file_json )
    lst=[]
    try:
        with open(file_json, encoding='utf-8') as f: 
            j1 = f.read()
            j2 =j1.replace('][', ',')
            jurls = json.loads(j2)
        # link by limk    
        # for jurl in (jurls[:50]): #<<<===
        for jurl in (jurls):    
            p = c3.wpage_property(jurl['No'], jurl["url"], jurl['No'])  # create immo objects 
            if p.get_data_immoweb()==True:  # get & set data to obj + feedback     
                if int(coumter)%100==0:        # check getting data            
                    log_msg = datetime.now().strftime("%d/%m/%Y %H:%M:%S") +" = " + str(coumter) + ' links are processed'
                    print(log_msg)            
            else:             
                    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") +" = " + str(p.no) + ' bad link')
                    continue # if it run into bad link  
            lst.append(p.ddict)
            coumter+=1
        log_msg = datetime.now().strftime("%d/%m/%Y %H:%M:%S") +" = Processing link from" + file_json + " finished." 
        return lst

    except json.JSONDecodeError: 
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") +" = Processing links from " + file_json + " finished.")       
        return lst

    
    
    
"""---------------------------------
------- START SCRAPPING ------------
---------------------------------"""

ooc_wpage_main=c1.w_page("immoweb","https://www.immoweb.be") 
ooc_wpage_searchsale = c2.wpage_links("webpage with all objects for SALE", 
                                   ooc_wpage_main.url +
                                   "/en/search/house-and-apartment/for-sale?countries") 

# clear file with group links
with open('web_urls_2.json', 'w', encoding='utf-8') as f:
    f.write('')

# getting ordinary links, save them to json-file and get count scrapped links
lc = ooc_wpage_searchsale.get_links(1) #<<<=== 500

# Starting link processing and saving data to the list of dictionaries
lst_alli = list()
lst_alli = proc_links(1,"web_urls_1.json")
lst_alli = lst_alli + proc_links(1,"web_urls_2.json")


# preparing save dict to CSV
    # get headers 
field_names = lst_alli[0].keys() # get all keys od dict for csv.DictWriter
    # writing dict to CSV
with open('web_urls_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(lst_alli)

# log message
print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "= The scrapping is fifnished.")
  

