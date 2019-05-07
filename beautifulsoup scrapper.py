## importing all required libraries
from bs4 import BeautifulSoup
import requests
import csv

pages = 5 ## total number of pager
current = 1 ## start page index
dataset = [] ## empty list to store scrapped data
## loop to scrape data from all 5 pages
while current <= pages:
    url = "http://econpy.pythonanywhere.com/ex/00{}.html".format(current)
    print(url)
    response = requests.get(url) ## getting html content
    html = response.content 
    soup = BeautifulSoup(html, "lxml") ## intializing beautifulsoup instance
    divs = soup.find_all("div", {"title": "buyer-info"}) ## getting all divs with title buyer-info
    ## loop to get each buyer name and price
    for div in divs:
        buyer_info = []
        buyer_info.append(div.find("div", {"title": "buyer-name"}).text) ## getting buyer name 
        buyer_info.append(div.find("span", {"class": "item-price"}).text) ## getting item price
        dataset.append(buyer_info)
    current += 1 ## increment in current page so we can go to next page

## creating csv
with open("econpy.csv", 'w', newline='', encoding="utf-8") as writeFile:    
    writer = csv.writer(writeFile)
    writer.writerow(["Buyer Name", "Price"]) ## adding header of csv file
    writer.writerows(dataset) ## adding dataset in csv
writeFile.close()
