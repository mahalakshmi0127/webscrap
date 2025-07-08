import requests
import pandas as pd
from bs4 import BeautifulSoup

response=requests.get('https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io')
print(response)
soup=BeautifulSoup(response.content,'html.parser')
# print(soup)
# data is in unstructed need to convert into structed data
names=soup.findAll('div',class_="KzDlHZ")
print(names)
name=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
print(name)
prices=soup.findAll('div',class_="Nx9bqj _4b5DiR")
price=[]
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
print(price)
rates=soup.findAll('div',class_="XQDdHH")
rate=[]
for i in rates[0:20]:
    d=i.get_text()
    rate.append(float(d))
print(rate)
images=soup.findAll('img',class_="DByuf4")
image=[]
for i in images[0:20]:
    d=i["src"]
    image.append(d)
print(image)

links=soup.findAll("a",class_="CGtC98")
link=[]
for i in links[0:20]:
    d="https://www.flipkart.com"+i["href"]
    link.append(d)
print(link)

df=pd.DataFrame()
df["names"]=name
df["prices"]=price
df["rates"]=rate
df["images"]=image
df["links"]=link
print(df)
# convert df into csv
df.to_csv("Mobile.csv")





    
