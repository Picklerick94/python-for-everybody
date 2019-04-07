import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_198345.json'
uh = urllib.request.urlopen(url, context=ctx).read()

data = json.loads(uh)

sum_num = 0
for data in data['comments']:
  sum_num += int(data['count'])
print(sum_num)
