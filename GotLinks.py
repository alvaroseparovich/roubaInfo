import bs4 as bs
import urllib.request

import RobeScript
import csvManipulate


mainLink = urllib.request.urlopen('http://www.thomasnelson.com.br/livros/').read()
page = bs.BeautifulSoup(mainLink,'lxml')

aLinks = page.find('ul',class_='snap_nav').find_all('a')

for a in aLinks:
    print(a.get('href'))


def openAllBooksInPage(urllink):
    pageBooks = urllib.request.urlopen(urllink).read()
    SoupBooks = bs.BeautifulSoup(pageBooks,'lxml')

    lastUrl = csvManipulate.checkLast()

    for capa in SoupBooks.find('ul',class_='livros').find_all('div', class_='livro-capa'):
        if capa.find('a').get('href') not in lastUrl:
            print ( capa.find('a').get('href') )
            infProduct = RobeScript.roubaInfo(capa.find('a').get('href'))
            csvManipulate.writeOnCSV(infProduct)
        else:
            print('jump')


for a in aLinks:
    print("Rendering This Page: " + a.get("href"))
    print('======================================================')
    print('\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
    openAllBooksInPage(a.get("href"))
    print('=============================================')
    print('================ End This Page ==============')
    print('=============================================')
    print('.............')
