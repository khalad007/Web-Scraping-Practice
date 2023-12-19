# from bs4 import BeautifulSoup
# import requests

# url = 'https://www.scrapethissite.com/pages/forms/'
# page = requests.get(url)
# soup = BeautifulSoup(page.text, 'html.parser')


# print(soup.prettify)

from bs4 import BeautifulSoup
import requests

res = requests.get('https://btst-blush.vercel.app/posts')
soup = BeautifulSoup(res.text, "html.parser")
result = soup.find_all("h2")[0]
print(result)