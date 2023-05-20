from multiprocessing.spawn import import_main_path
from turtle import position
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Open URL and retrieve all anchor tag
def openurl(x):
    url = x
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    c = 0
    for tag in tags:
        c = c + 1
        if c == post:
            a = tag.get('href', None)
            return a

#Entries
entry = input('Enter - ')
count = int(input('Enter Count: '))
post = int(input('Enter Position: '))

#The actual work
ou = openurl(entry)
for i in range(count-1):
    ou = openurl(ou)
h = urllib.request.urlopen(ou, context=ctx).read()
s = BeautifulSoup(h, 'html.parser')
text = s.get_text().strip()
name = text.split('\n', 1)[0].split()[2]
print(name)