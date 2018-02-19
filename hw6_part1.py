# 507/206 Homework 6 Part 1
import requests
from bs4 import BeautifulSoup


#### Part 1 ####
print('\n*********** PART 1 ***********')
print("Mark's page -- Alt tags\n")

### Your Part 1 solution goes here


html = requests.get(" http://newmantaylor.com/gallery.html").text
soup = BeautifulSoup(html, "html.parser")

#print(soup.head)
#print(soup.body)

print(soup.find("img"))

for eachTag in soup.find_all('img'):
    if eachTag.has_attr('alt'):
        print(eachTag['alt'])
    else:
        print("No alternative text provided!!")
