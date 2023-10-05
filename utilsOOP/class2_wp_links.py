import sys
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
sys.stdout.reconfigure(encoding='utf-8')
import class1_wp_home as c1


class wpage_links(c1.w_page):
      def __init__(self, desc, url):
            super().__init__(desc, url)
            
            
      #
      @property #перші дві властивості тягнуть з батьківського класу
      def info(self): return f'desc={self.desc} url={self.url}'

      #  
      def get_links(self):
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),"=", 'Collecting links is started...')
        # Send an HTTP GET request
        lst_urls=list()
        var_i=1
        var_ii=1

        url = f"{self.url}=BE&page={var_ii}&orderBy=relevance"
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
                    if var_i%1000==0: 
                        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),"=", var_i, 'links are collected')
                    var_x+=1
                    var_i+=1
            var_ii+=1
           
            url = f"{self.url}=BE&page={var_ii}&orderBy=relevance"
            response = requests.get(url)
            var_respcode=response.status_code
            # print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            
        #
        var_json = json.dumps(lst_urls, indent=2, ensure_ascii=False) #indent=2 >> pretty-printing      
        with open("web_urls_.json", "w", encoding='utf-8') as var_jf:
            var_jf.write(var_json) 

        #
        time=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        msg1="Collecting links is finished."
        msg2="links are collected and saved to json."
        #
        return f"{time} {msg1} {var_i-1} {msg2}"
      




  