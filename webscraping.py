import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://mail.google.com/mail/u/0/#inbox/').read()

soup = bs.BeautifulSoup(source,'lxml')
nav = soup.nav

for url in nav.find_all('a'):
    print(url.get('heref'))

# title of the page


#print(soup.title.name)

# get values:
#print(soup.title.string)

# beginning navigation:
#print(soup.title.parent.name)

# getting specific values:
#print(soup.p)

#for paragraph in soup.find_all('p'):
    #print(paragraph.string)
    #print(str(paragraph.text))

#for url in soup.find_all('a'):
   # print(url.get('href'))

#print(soup.get_text())

