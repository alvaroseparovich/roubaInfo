import bs4 as bs
import urllib.request

def roubaInfo(siteToRobe):#passar url como parametro
    sauce = urllib.request.urlopen(siteToRobe,).read()
    soup = bs.BeautifulSoup(sauce,'lxml')
    mainInfo = soup.find('div', class_='texto-livro')

    if soup.find('h1', class_='archive_title'):
        print('Title: -- ' + soup.find('h1', class_='archive_title').text)
        title = soup.find('h1', class_='archive_title').text
    else:
        title = ""

    #print('IMG: -- ' + soup.find('div', class_='coverbook').find('img').get('src'))
    if soup.find('div', class_='coverbook').find('img'):
        img = soup.find('div', class_='coverbook').find('img').get('src')
    else:
        img = ""

    #print('Sinopse: -- ' + mainInfo.find('p',class_='lead').text)
    if mainInfo.find('p',class_='lead'):
        sinopse = mainInfo.find('p',class_='lead').text
    else:
        sinopse = ''

    #print('Autor: -- ' + mainInfo.find_all('a')[0].text)
    if mainInfo.find_all('a')[0]:
        autor = mainInfo.find_all('a')[0].text
    else:
        autor = ""

    #print('Genero: -- ' + mainInfo.find_all('a')[1].text)
    if len(mainInfo.find_all('a')) > 1:
        genero = mainInfo.find_all('a')[1].text
    else:
        genero = ""

    odInfo = []
    for a in mainInfo.find_all('div')[-1]:
        #print(a.string)
        odInfo.append(a.string)

    #print([title,img,sinopse,autor,genero,odInfo[3],odInfo[4],odInfo[5],odInfo[6]])
    print("=======================================================")
    print("Page Complete")
    print("=======================================================")

    return [siteToRobe,title,img,sinopse,autor,odInfo[3],odInfo[4],odInfo[5],odInfo[6]]

# print( roubaInfo(siteToRobe) )
