import requests
from bs4 import BeautifulSoup
st=input("Please enter the url of website\n")
url = st
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)
anchors=soup.find_all('a')
all_links = set()
for link in anchors:
    if(link.get("href") != '#'):
        link=st + link.get("href")
        all_links.add(link)
        print(link)