# 507/206 Homework 6 Extra Credit 1
import requests
from bs4 import BeautifulSoup

#### Extra Credit 1 ####
print('\n*********** EXTRA CREDIT 1 ***********')
print('Top Headlines\n')

### Your Extra Credit 1 solution goes here
html = requests.get('https://www.michigandaily.com/').text
soup = BeautifulSoup(html, "html.parser")

def newstitle(keyword):
    print("Top 10 Headlines:"+ keyword)

    chunk_1 = soup.find('div', attrs={'id':'section-'+keyword})
    chunk_2 = chunk_1.find_all(class_='views-field views-field-field-short-headline')
    for i in range(0,len(chunk_2)):
        chunk_3 = chunk_2[i].find_all(class_='field-content')
        for div in chunk_3:
            print(div.string)

    print("______________________")

newstitle("news")
newstitle('sports')
newstitle('arts')
