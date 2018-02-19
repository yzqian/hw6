# 507/206 Homework 6 Part 2
import requests
from bs4 import BeautifulSoup


#### Part 2 ####
print('\n*********** PART 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Part 2 solution goes here
html = requests.get('https://www.michigandaily.com/').text
soup = BeautifulSoup(html, "html.parser")

chunk = soup.find('div', attrs={'class':'panel-pane pane-mostread'})

s = chunk.find_all('li')

for li in s:
    print(li.string)
