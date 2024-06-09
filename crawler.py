import requests
from  bs4 import BeautifulSoup 
print("\n \nThis tool is made by localh0ste (vikram)\n ")
print("\n----------------swiftsafe-------------------\n")
print("\n................CRAWLER....................\n")
ask = input("Enter your site you want to Crawl  ")
url = 'https://'+ask

reqs = requests.get(url)

soup = BeautifulSoup(reqs.text, 'html.parser')
 

urls = []

for link in soup.find_all('a'):

    print(link.get('href'))

print("\n-------------------END------------\n")


