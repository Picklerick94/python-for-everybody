from bs4 import BeautifulSoup
import ssl
from urllib.request import urlopen
import json
import datetime as DT

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

today = DT.date.today()
day_num = 0

# MySoul
# filename = "19.csv"

# infinity
filename = "347.csv"

f = open(filename, "w")

headers = "title_en, title_cn, day_num, start_time, end_time, bookable, spots_left\n"

f.write(headers)

for day_num in range(7):
	date = today + DT.timedelta(days=day_num)

	# Mysoul
	# url = f'https://yun.qingchengfit.cn/api/mobile/schedules/group/?shop_id=49220&date={date}'

	# infinity
	url = f'https://yun.qingchengfit.cn/api/mobile/schedules/group/?shop_id=64898&date={date}'
	
	res = urlopen(url).read()
	contents = json.loads(res).get("data").get("schedules")
	for content in contents:
		title_en = content.get("course").get("name").lstrip('*')
		title_cn = title_en
		start_time = content.get("start").split('T')[1]
		end_time = content.get("end").split('T')[1]
		if (content.get("current_max_capacity") == 0):
			bookable = False
		else:
			bookable = True
		spots_left = content.get("current_max_capacity")
		f.write(title_en + "," + title_cn + "," + str(day_num) + "," + start_time + "," + end_time + "," + str(bookable) + "," + str(spots_left) + "\n")

f.close()
