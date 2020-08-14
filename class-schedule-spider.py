from bs4 import BeautifulSoup
import ssl
from urllib.request import urlopen
import json
import datetime as DT

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.styd.cn/m/383138/default/search?date=2020-06-28&shop_id=1000118&type=1'
res = urlopen(url).read()
content = json.loads(res).get("data")
html = content.get("class_list")
soup = BeautifulSoup(html, "html.parser")
containers = soup.find_all('a', {"class": "course_link"})

bookable = True

for container in containers:
	activity_title = container.find_all('p', {"class": "name"})[0].text
	if activity_title.strip().split('/')[0]:
		title_en = activity_title.strip().split('/')[0]
		if len(activity_title.strip().split('/')) > 1:
			title_cn = activity_title.strip().split('/')[1]
		else:
			title_cn = activity_title.strip().split('/')[0]
	activity_time = container.find_all('p', {"class": "date"})[0].text
	all_time = activity_time.split()
	start_time = all_time[0]
	end_time = all_time[2]
	activity_status = container.find_all('i', {"class": "course_status"})[0]
	status = activity_status['class'][1]
	if (status == 'full') or (status == 'queue') or (status == 'stop'):
		bookable = False
	else:
		bookable = True
	print(title_cn, bookable)