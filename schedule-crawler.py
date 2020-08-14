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

# smf
# filename = "54.csv"

# x-pilates
# filename = "142.csv"

# def yuyuan
# filename = "197.csv"

# VIS
# filename = "272.csv"
	
# Prime
# filename = "8.csv"

# Boxing Republic

# GG

# Shanghai Latin Dance

f = open(filename, "w")

headers = "title_en, title_cn, day_num, start_time, end_time, bookable\n"

f.write(headers)

for day_num in range(7):
	date = today + DT.timedelta(days=day_num)
	# smf
	# url = f'https://www.styd.cn/m/383138/default/search?date={date}&shop_id=1000118&type=1'

	# x-pilates
	# url = f'https://www.styd.cn/m/62bca449/default/search?date={date}&shop_id=295098953&type=1'

	# def yuyuan
	# url = f'https://www.styd.cn/m/1ff07b74/default/search?date={date}&shop_id=324831882&type=1'

	#VIS
	# url = f'https://www.styd.cn/m/383673/default/search?date={date}&shop_id=402176022&type=1'

	# Prime
	# url = f'https://www.styd.cn/m/3164e5db/default/search?date={date}&shop_id=202584433&type=1'

	# Boxing Republic
	# url = f'https://www.styd.cn/m/3164e5db/default/search?date={date}&shop_id=202584433&type=1'

	# GG

	# Shanghai Latin Dance
	# url = f'https://www.styd.cn/m/38d5cc03/default/search?date={date}&shop_id=169604963&type=1'

	res = urlopen(url).read()
	content = json.loads(res).get("data")
	html = content.get("class_list")
	soup = BeautifulSoup(html, "html.parser")
	containers = soup.find_all('a', {"class": "course_link"})

	for container in containers:
		activity_title = container.find_all('p', {"class": "name"})[0].text
		# if activity_title.strip().split('|')[0]:
		# 	title_en = activity_title.strip().split('|')[0]
		# 	if len(activity_title.strip().split('|')) > 1:
		# 		title_cn = activity_title.strip().split('|')[1]
		# 	else:
		# 		title_cn = activity_title.strip().split('|')[0]
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
		f.write(title_en + "," + title_cn + "," + str(day_num) + "," + start_time + "," + end_time + "," + str(bookable) + "\n")

f.close()
