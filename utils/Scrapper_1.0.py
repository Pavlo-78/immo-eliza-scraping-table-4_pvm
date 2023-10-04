import sys
import csv
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
sys.stdout.reconfigure(encoding='utf-8')


# ----------------------------------
def get_links_from_immoweb():
# THIS FUNC COLLECTS LINKS OF ADDS # and save them in json
# ----------------------------------

    # Send an HTTP GET request
    lst_urls=list()
    var_i=1
    var_ii=1

    url = f"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&page={var_ii}&orderBy=relevance"
    response = requests.get(url)
    var_respcode=response.status_code
    while var_respcode == 200 and var_ii<500:  
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        # Finding tags
        soupF = soup.find_all("a", class_="card__title-link") ###### 30 
        # Extract and print the ad links
        var_x=1
        for e in soupF:        
            if e:
                href = e.get("href")
                # print(var_i, var_ii, var_x, href)
                lst_urls.append({"No":var_i, "Np":var_ii, "Nl":var_x, "url":href})
                var_x+=1
                var_i+=1
        var_ii+=1

        url = f"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&page={var_ii}&orderBy=relevance"
        response = requests.get(url)
        var_respcode=response.status_code
        # print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

    var_json = json.dumps(lst_urls, indent=2, ensure_ascii=False) #indent=2 >> pretty-printing      
    with open("web_urls_.json", "w", encoding='utf-8') as var_jf:
        var_jf.write(var_json)   



# ------------------------------------------------
def get_data_immoweb(no,url):
# THIS FUNC GET LINCS IN JSON, COLLECTS DATA BY LINK (ONE-BY-ONE) AND RETURN A DICT
# ------------------------------------------------

    # 
    # u = "https://www.immoweb.be/en/classified/apartment-block/for-sale/huy/4500/10462965"
    # u = "https://www.immoweb.be/en/classified/house/for-sale/ronse/9600/10847994"
    r = requests.get(url)
    s = BeautifulSoup(r.text, "lxml")

    # get the tag 
    script_tag = s.find('script', type='text/javascript')

    # Get the text content from the <script> tag
    script_content = script_tag.string
    # print(script_content)

    # preparing to get jawa dictionary
    json_start = script_content.find('{')
    json_end = script_content.rfind('}')
    # get the row text of java dict
    json_text1 = script_content[json_start:json_end+1]
    # checking the data of the link - if the data is bad, stop and out with message "Error" 
    if json_text1[2:4] != 'id': # get "id" and check if it exists  
        return "ERROR"
    # convert row java text of dict to python dict
    json_data = json.loads(json_text1) #print(type(json_data)) >> <class 'dict'>
    # appending data to list 
    json_dataAL = [str(no)] # init list of this link with number by order
    json_dataAL.append(json_data)   # ad to list all info from website with garbage
    # converting all info to json format 
    json_dbg = json.dumps(json_dataAL, indent=2, ensure_ascii=False) #indent=2 >> pretty-printing
    # save data to json file with pretty-printing for debagging (last succsseful link)
    with open("web_url_current.json", "w", encoding='utf-8') as var_jf:
        var_jf.write(json_dbg) 

    # preparing  main dictionary for require webdata
    dct_webdata = dict()
    # adding to main dict number of link and url
    dct_webdata["no"]=no
    dct_webdata["url"]=url


    try:
        dct_webdata["PropertyId"] = json_data["id"]
    except (KeyError, TypeError):
        dct_webdata["PropertyId"]=None

    try:
        dct_webdata["Locality_Name"] = json_data["property"]["location"]["locality"]
    except (KeyError, TypeError):
        dct_webdata["Locality_Name"]=None

    try:
        dct_webdata["Postal_code"] = json_data["property"]["location"]["postalCode"]
    except (KeyError, TypeError):
        dct_webdata["Postal_code"]=None

    try:
        dct_webdata["Type_of_property"] = json_data["property"]["type"]
    except (KeyError, TypeError):
        dct_webdata["Type_of_property"]=None

    try:
        dct_webdata["Subtype_of_property"] = json_data["property"]["subtype"]
    except (KeyError, TypeError):
        dct_webdata["Subtype_of_property"]=None

    try:
        dct_webdata["Price"] = json_data["transaction"]["sale"]["price"]
    except (KeyError, TypeError):
        dct_webdata["Price"]=None

    try:
        dct_webdata["Type_of_sale"] = json_data["transaction"]["type"]
    except (KeyError, TypeError):
        dct_webdata["Type_of_sale"]=None

    try:
        dct_webdata["Number_of_rooms"] = json_data["property"]["bedroomCount"]
    except (KeyError, TypeError):
        dct_webdata["Number_of_rooms"]=None

    try:
        dct_webdata["Living_Area"] = json_data["property"]["netHabitableSurface"]
    except (KeyError, TypeError):
        dct_webdata["Living_Area"] =None

    try:    
        dct_webdata["Equipped_kitchen"] = json_data["property"]["kitchen"]["type"]
    except (KeyError, TypeError):   
        dct_webdata["Equipped_kitchen"] = None

    try:
        dct_webdata["Furnished"] = json_data["transaction"]["sale"]["isFurnished"]
    except (KeyError, TypeError):
        dct_webdata["Furnished"]=None

    try:
        dct_webdata["Open_fire"] = json_data["property"]["fireplaceExists"]
    except (KeyError, TypeError):
        dct_webdata["Open_fire"]=None

    try:
        dct_webdata["Terrace_YN"] = json_data["property"]["hasTerrace"]
    except (KeyError, TypeError):
        dct_webdata["Terrace_YN"]=None

    try:
        dct_webdata["TerraceSurface"] = json_data["property"]["hasTerrace"]
    except (KeyError, TypeError):
        dct_webdata["TerraceSurface"]=None

    try:
        dct_webdata["Garden_YN"] = json_data["property"]["hasGarden"]
    except (KeyError, TypeError):
        dct_webdata["Garden_YN"]=None

    try:
        dct_webdata["Garden_area"] = json_data["property"]["gardenSurface"]
    except (KeyError, TypeError):
        dct_webdata["Garden_area"]=None

    try:
        dct_webdata["Surface_of_good"] = json_data["property"]["building"]["streetFacadeWidth"]
    except (KeyError, TypeError):
        dct_webdata["Surface_of_good"]=None

    try:
        dct_webdata["Number_of_facades"] = json_data["property"]["building"]["facadeCount"]
    except (KeyError, TypeError):
        dct_webdata["Number_of_facades"]=None

    try:
        dct_webdata["Swimming_pool_YN"] = json_data["property"]["hasSwimmingPool"]
    except (KeyError, TypeError):
        dct_webdata["Swimming_pool_YN"]=None

    try:
        dct_webdata["State_of_building"] = json_data["property"]["building"]["condition"]
    except (KeyError, TypeError):
        dct_webdata["State_of_building"]=None

    # print(dct_webdata)
    return dct_webdata 
# end of func "get_data_immoweb"





# ***************************
# MAINE DATA GATHERING
# ***************************

# liks collecting
print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "= The link collection is started...")
get_links_from_immoweb()
print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "= The link collection is finished.")

# list for urls from json file
lst_all_urls = list()

# open file wit
# h all link 
with open('web_urls_.json', encoding='utf-8') as f: 
    u1 = json.load(f) # load json in variable
    # u1 = u1[0:220]    # DEBAGGING
    dbgg=len(u1)
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "= The scrapping is started...")

    to = len(u1) # list of dictionary with links  
for i in range(to): # loop link by link 
    u2=u1[i]        # this line 
    u3=u2["url"]    # get url from this line
    no=u2['No']     # get number of this line
    dct_by_url = get_data_immoweb(no,u3) # get data of this url
    if dct_by_url=="ERROR": # missing bad link
        continue
    else:    
        lst_all_urls.append(dct_by_url) # appending date of good link
    # print time message of each 100 processed link as indication of process
    if no%100==0: 
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),"=", no, 'links are proceeded')

# preparing save dict to CSV
field_names=lst_all_urls[0].keys() # get all keys od dict for csv.DictWriter
# writing dict to CSV
with open('web_urls_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(lst_all_urls)

print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "= The scrapping is fifnished.")
