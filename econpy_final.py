import csv
from selenium import webdriver
MAX_PAGE_NUM = 5
 
with open('results.csv', 'w') as f:
    f.write("Buyer, Price \n")
driver = webdriver.Chrome()

for x in range(MAX_PAGE_NUM):
    page_number = str(x+1)
    url="http://econpy.pythonanywhere.com/ex/00"+page_number+".html"
    driver.get(url)
    buyers_name = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
    price = driver.find_elements_by_xpath('//span[@class="item-price"]')
    number_of_buyers = len(buyers_name)
    with open('results.csv', 'a') as f:
        for x in range(number_of_buyers):
            f.write(buyers_name[x].text + ","+price[x].text+"\n")
driver.close()
