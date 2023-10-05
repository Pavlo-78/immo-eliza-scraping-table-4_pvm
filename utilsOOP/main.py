
import sys
import csv
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
sys.stdout.reconfigure(encoding='utf-8')
import class1_wp_home as c1
import class2_wp_links as c2
import class3_wp_property as c3


# ***************************
# MAINE DATA GATHERING
# ***************************

ppl=[]
ooc_wpage_main=c1.w_page("immoweb","https://www.immoweb.be") 
ooc_wpage_searchsale = c2.wpage_links("webpage with all objects for SALE", 
                                   ooc_wpage_main.url +
                                   "/en/search/house-and-apartment/for-sale?countries") 

# list for urls from json file
# lst_all_urls = list()

# open file wit
# h all link 
with open('web_urls_.json', encoding='utf-8') as f: 
    u1 = json.load(f) # load json in variable
    u1 = u1[0:10]    # DEBAGGING
    dbgg=len(u1)
    # print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "= The scrapping is started...")

    to = len(u1) # list of dictionary with links  
for i in range(to): # loop link by link 
    u2=u1[i]        # this line 
    u3=u2["url"]    # get url from this line
    no=u2['No']     # get number of this line
    ppl.append(c3.wpage_property(f"ppage{i}",u3,no))
    # dct_by_url = get_data_immoweb(no,u3) # get data of this url
    # if dct_by_url=="ERROR": # missing bad link
    #     continue
    # else:    
    #     lst_all_urls.append(dct_by_url) # appending date of good link
    # print time message of each 100 processed link as indication of process
    # if no%100==0: 
    #     print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),"=", no, 'links are proceeded')
# ------------------------------------------------------------------------------------------
 

print(no)

# students = [Student(f"Студент_{i}") for i in range(20)]
# pl = [c3.wpage_property(f"proprty_page{i}",u3,no) for i in range(20)]
for i in(ppl):
    print(i.no, i.desc,i.url)



# ------------------------------------------------------------------------------------------


# *****************************************************
# *****************************************************

# 
# print(ooc_wpage_main.info)


# ##
# # print(ooc_wpage_searchsale.info)
# print(ooc_wpage_searchsale.get_links())