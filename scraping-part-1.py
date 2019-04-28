from selenium import webdriver
import csv
driver = webdriver.Chrome()
driver.get("http://econpy.pythonanywhere.com/ex/001.html")
buyer=driver.find_elements_by_xpath('//div[@title="buyer-name"]')
price = driver.find_elements_by_xpath('//span[@class="item-price"]')
nmuber = len(buyer)
for x in range(nmuber):
    print(buyer[x].text)
    print(price[x].text)
with open("sample.csv",'w') as f:
    f.write("buyer,price \n")
    for x in range(nmuber):
        f.write(buyer[x].text+","+price[x].text+"\n")
driver.close()
