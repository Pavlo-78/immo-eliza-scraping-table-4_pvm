import sys
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
sys.stdout.reconfigure(encoding='utf-8')
import class1_wp_home as c1


# A class of the search web page, that inherits from the class of the home page 
# The inheritance is used for educational purposes
class wpage_links(c1.w_page):
    def __init__(self, desc, url):
        super().__init__(desc, url)
            

    # Decorator for viewing self.desc + self.url properties  
    # Decorator is used for educational purposes     
    @property 
    def info(self): return f'desc={self.desc} url={self.url}'

    
    def get_links(self, count_page): 
        """
        Collects all ad links from the main search page. 
        The number of pages can be limited - the "count_page" parameter

        :return: File web_urls_.json with list of links/
        """  
            # log message
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),"=", 'Scrapping links is started...') 

        self.count_page = count_page      
        # Send an HTTP GET request
        lst_urls=list()
        var_i=1     # the number of this link
        var_ii=1    # the number of the web page with link od ad 
        # var_ii=195    # the number of the web page with link od ad <<<<<<<<

        url = f"{self.url}=BE&page={var_ii}&orderBy=relevance"
        response = requests.get(url)
        var_respcode=response.status_code
        while var_respcode == 200 and var_ii<count_page+1: 
            
            # Parsing the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Finding tags
            soupF = soup.find_all("a", class_="card__title-link") 

            # Extract and print the ad links
            var_x=1
            for e in soupF:        
                if e:
                    href = e.get("href")
                    # print(var_i, var_ii, var_x, href)
                    lst_urls.append({"No":var_i, "Np":var_ii, "Nl":var_x, "url":href})
                    if var_i%1000==0: 
                        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),"=", var_i, 'links are collected')
                    var_x+=1
                    var_i+=1
            var_ii+=1
            # next while           
            url = f"{self.url}=BE&page={var_ii}&orderBy=relevance"
            response = requests.get(url)
            var_respcode=response.status_code
            # print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            
        #
        var_json = json.dumps(lst_urls, indent=2, ensure_ascii=False) #indent=2 >> pretty-printing      
        with open("web_urls_1.json", "w", encoding='utf-8') as var_jf:
            var_jf.write(var_json) 

            # log message
        time=datetime.now().strftime("%d/%m/%Y %H:%M:%S")    
        print(f"{time} = Scrapping links is finished. {var_i-1} links are saved to json.")
        return var_i-1 # count collected urls
      




  