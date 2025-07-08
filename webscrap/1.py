import requests
import pandas as pd
from bs4 import BeautifulSoup
response=requests.get("https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io")
print(response)
soup=BeautifulSoup(response.content,"html.parser")
#print(soup)
#data is in unstructured need to convert 
""""
names=soup.findAll("div",class_="KzDlHZ")
name=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)


#price
prices=soup.findAll("div",class_="Nx9bqj _4b5DiR")
price=[]
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)

#rating
rating=soup.findAll("div",class_="XQDdHH")
rate=[]
for i in rating[0:20]:
    d=i.get_text()
    rate.append(d)

#image
images=soup.findAll("img",class_="DByuf4")
image=[]
for i in images[0:20]:
    d=i["src"]
    image.append(d)

"""
#link
links=soup.findAll('a',class_="DByuf4")
link=[]
for i in links[0:20]:
    d="https://www.flipkart.com/"+i["href"]
    link.append(d)
print(link)


"""
df=pd.DataFrame()
df["names"]=name
df["prices"]=price
df["ratings"]=rate
df["images"]=image
df["links"]=link
print(df)
"""


    
