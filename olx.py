# import requests 
# import time
# from bs4 import BeautifulSoup

# url = 'https://www.olx.ba/pretraga?kategorija=154&id=154&stanje=0&vrstapregleda=grid&sort_order=desc&sort_po=datum&od=200&do=900&vrsta=samoprodaja&ram-memorija_select_8gb=8GB';
# lastData = []
# firstRun = True

# while(True):
#   res = requests.get(url)
#   articleIds = []
#   soup = BeautifulSoup(res.content, 'html.parser')
#   rezultatiPretrage = soup.find('div', id ='rezultatipretrage')

  
#   for link in rezultatiPretrage.find_all('div', {"class": "artikal" }):
#     if link.get('id'):
#       articleIds.append(link.get('id')) 

#   if lastData == [] or lastData[0] != articleIds[0]:
#     for item in articleIds:
#       if item not in lastData and firstRun == True:
#         p = (soup.find('div', id=item)).find('p', class_="na")
#         c = (soup.find('div', id=item)).find('div', class_="datum")
#         print('Naziv: ', p.text)
#         print('Cijena: ', c.find('span').text)
#         print('Datum: ', c.find('div', class_="kada").text)
#         print('--------------------------')

#     lastData = articleIds
#     firstRun = False
#     time.sleep(300)