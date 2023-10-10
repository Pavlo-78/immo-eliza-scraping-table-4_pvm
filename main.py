import csv
import utils.class1_wp_home as c1
import utils.class2_wp_links as c2
import utils.class4_wp_scrapp as c4
from datetime import datetime
import sys
sys.stdout.reconfigure(encoding='utf-8')  
    
"""---------------------------------
------- START SCRAPPING ------------
---------------------------------"""

count_likspage_for_scrap=500
url1="immoweb","https://www.immoweb.be"
url2="/en/search/house-and-apartment/for-sale?countries"

obj_wpage_home=c1.w_page("immoweb","https://www.immoweb.be") 
ooj_wpage_links = c2.wpage_links("webpage with ad links", obj_wpage_home.url + url2) 
obj_scr = c4.Scrapper()

# clear file with group links
with open('web_urls_2.json', 'w', encoding='utf-8') as f:
    f.write('')

# getting ordinary links, save them to json-file and get count scrapped links
lc = ooj_wpage_links.get_links(count_likspage_for_scrap) #<<<=== 500

# Starting link processing and saving data to the list of dictionaries
y = list()
y = obj_scr.proc_links(1,"web_urls_1.json") # json 1
y +=obj_scr.proc_links(1,"web_urls_2.json") # json 2 - adding to y


# preparing save dict to CSV
    # get headers 
field_names = y[0].keys() # get all keys od dict for csv.DictWriter
    # writing dict to CSV
with open('web_urls_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(y)

# log message
print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "= The scrapping is fifnished.")
  

