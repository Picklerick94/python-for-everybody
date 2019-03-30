import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Leighton.html'

for i in range(7):
  html = urllib.request.urlopen(url, context=ctx).read()
  soup = BeautifulSoup(html, 'html.parser')
  links = soup('a')
  link = links[17].get('href', None)
  url = link
  print(re.findall('known_by_([A-Z]\w+)', link)[0])
