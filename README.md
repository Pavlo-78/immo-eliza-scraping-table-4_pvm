# Project "Immo-Eliza"
## Table of Content
- Description
- Getting Started
    - Pre-requisites
    - Installation
    - Additional info on running the program
- Version
## Description
Python program for scraping web site "Immoweb" for all objects for sale. 
The information is output to the file "as is", without additional processing.
If there are doubts about a certain unit of data, we always know that the program did not process them. 
Further data processing will be at the stage of data cleaning.

To check the operation, in the "main.py" module, to call the "get_links(500)" function, set a smaller value instead of 500, for example 5 or 10. This parameter is responsible for the number of search pages from which ad links will be taken. 
With a smaller value, the program will collect less data and spend less time.

How does the program work?
1. First, the program opens a page with a search for objects for sale, which contains 333 pages. If desired, the number of pages can be limited (there is a function parameter get_links() )
2. The program collects links from each page and saves them in the json file. (web_urls_1.json) There are approximately 19+ thousand of them.
3. The program analyzes each received link, visits the page, collects and accumulates data.
4. Some ads advertise a group of properties, each of which has its own weblink and page. In this case, all links are collected and stored in an additional json file (web_urls_2.json)
5. After processing all links from the search page (web_urls_1.json), the program additionally processes links from group ads (web_urls_2.json).
6. All collected information is recorded in the web_urls_data.csv file.

The program scraps information and save it to csv file with the following columns : 
- Property ID
- Locality Name
- Postal Code
- Type of Property
- Subtype of Property
- Price
- Type of Sale
- Number of Rooms
- Living Area
- Equipped Kitchen
- Furnished
- Open Fire
- Terrace
- Terrace Area
- Garden
- Garden Area
- Surface of Good
- Number of Facades
- Swimming Pool
- State of Building

The service fields are additionally saved to make work easier:
url
id
ipiNo
customer_type
regionCode
region
province
location_type

## Getting Started
### Pre-requisites
- Be sure to have Python 3.x installed
### Installation
- Clone the repository
- Create a virtual environment and activate it
- Install the libraries from the requirements.txt file
- run the main.py file
### Additional info on running the program
1) The program displays a message at each stage of work with an indication of the time. 
Therefore, we can monitor the progress of the data collection.
2) The program uses some OOP concepts, namely encapsulation, inheritance, and decorator. The mentioned concepts complicate the program code somewhat, but they are used for educational purposes.
3) Also, for educational purposes, the classes are coded in different modules that interact with each other.