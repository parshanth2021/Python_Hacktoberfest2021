# Input Date =  http://py4e-data.dr-chuck.net/known_by_Juan.html

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Darcy.html'
position=int(input("Enter position: "))
repetitions=int(input("Enter count: "))
for times in range(repetitions):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position -1].get('href')
    result=tags[position -1].contents[0]
print(result)
