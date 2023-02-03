from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime
import csv

url = "https://www.amazon.in/SIDRUM-Shoulder-Adjustable-Compatible-Mirrorless/dp/B09P74TZY8/ref=sr_1_47?crid=2M096C61O4MLT&keywords=bags&qid=1675451564&sprefix=ba%2Caps%2C283&sr=8-47"


headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36" }

page = requests.get(url,headers=headers)

soup1 = BeautifulSoup(page.content,"html.parser")

soup2 = BeautifulSoup(soup1.prettify(),"html.parser")
title = soup2.find(id="productTitle").get_text().strip()
price = soup2.find(class_ = "a-offscreen").get_text().strip()
rating = soup2.find(id = "acrPopover").get_text().strip()
reviews = soup2.find(id = "acrCustomerReviewText").get_text().strip()
decription = soup2.find(id = "feature-bullets").get_text().strip()
product = soup2.find(id = "aplus_feature_div").get_text().strip()
# print(title.strip() )
# print(price.strip())
# print(rating.strip())
# print(reviews.strip())
# print(product.strip())

data = [url,title, price, rating,reviews,decription,product]

# # Write the list to a CSV file
with open('product_data.csv', 'a', newline='',encoding="UTF8") as file:
    writer = csv.writer(file)
    # writer.writerow(["URL","Title", "Price","Rating","Reviews","DeSription","Product"]) 
    writer.writerow(data)







