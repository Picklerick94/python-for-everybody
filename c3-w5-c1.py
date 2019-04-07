import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_198344.xml'

data = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(data)

results = tree.findall('comments/comment')
sum_num = 0
for i in results:
  sum_num += int(i.find('count').text)
print(sum_num)
