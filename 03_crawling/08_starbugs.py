from bs4 import BeautifulSoup
import requests

url = 'https://www.starbucks.co.kr/store/store_map.do?disp=quick'
res = requests.get(url).text
soup = BeautifulSoup(res,'html.parser')
# print(soup)
print(soup.select('.quickSearchResultBox strong'))