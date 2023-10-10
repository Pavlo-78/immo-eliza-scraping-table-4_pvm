import sys
import json
import utils.class3_wp_property as c3
from datetime import datetime
sys.stdout.reconfigure(encoding='utf-8')

class Scrapper():
    pass

    def proc_links(self, coumter, file_json):
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
                p = c3.wpage_property("obj"+str(jurl['No']), jurl["url"], jurl['No'])  # create immo objects 
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
