import requests
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36'}
data = requests.get("https://www.naver.com", headers=header)
from bs4 import BeautifulSoup as bs
soup = bs(data.text, 'html.parser')
soup.select("img")
img = soup.select('img')
for i in img:
    if i.attrs.get('src'):
        name = i.attrs['alt'] + ".png"
        link = i.attrs['src']
        if link.startswith("http"):
            get = requests.get(link)
            if get.status_code == 200:
                with open(name, 'wb') as w:
                    w.write(get.content)