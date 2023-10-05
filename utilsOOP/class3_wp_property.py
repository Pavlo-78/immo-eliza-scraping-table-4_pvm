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
          self.no=no




# obj= wpage_property(1,2,3)    
# print(obj.info)   














# class ImmoWebScraper:
#     def __init__(self):
#         self.base_url = "https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&page={}&orderBy=relevance"
#         self.links = []


#     def get_links_from_immoweb(self, max_pages=500):
#         var_i = 1
#         for var_ii in range(1, max_pages + 1):
#             url = self.base_url.format(var_ii)
#             response = requests.get(url)
#             if response.status_code != 200:
#                 break
            
#             soup = BeautifulSoup(response.text, 'html.parser')
#             links = soup.find_all("a", class_="card__title-link")
#             for link in links:
#                 href = link.get("href")
#                 self.links.append({"No": var_i, "Np": var_ii, "Nl": var_i, "url": href})
#                 var_i += 1


#     def get_data_immoweb(self, url):
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, "lxml")
#         script_tag = soup.find('script', type='text/javascript')
#         script_content = script_tag.string
#         json_start = script_content.find('{')
#         json_end = script_content.rfind('}')
#         json_text = script_content[json_start:json_end + 1]
        
#         try:
#             json_data = json.loads(json_text)
#             # Extract data and return a dictionary
#             # ...
            
            
#         except (KeyError, TypeError):
#             return None


#     def scrape_data(self):
#         for link in self.links:
#             no = link["No"]
#             url = link["url"]
#             data = self.get_data_immoweb(url)
#             if data:
#                 # Process the data and save it as needed
#                 # ...
#                 a=1


# if __name__ == "__main__":
#     scraper = ImmoWebScraper()
#     scraper.get_links_from_immoweb()
#     scraper.scrape_data()
#     print(datetime.now(), "THE WORK IS DONE!")
