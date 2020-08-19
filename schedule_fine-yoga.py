from bs4 import BeautifulSoup
import ssl
from urllib import request, parse
import json
import datetime as DT

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

venues = [
	{'name': 'fine_yueliangwan', 'filename': '378.csv', 'partnerid': 378, 'shopid': '42'},
	{'name': 'fine_changshoulu', 'filename': '379.csv', 'partnerid': 379, 'shopid': '36'},
	{'name': 'fine_889', 'filename': '380.csv', 'partnerid': 380, 'shopid': '41'},
	{'name': 'fine_xintiandi', 'filename': '381.csv', 'partnerid': 381, 'shopid': '39'},
	{'name': 'fine_xinggeng', 'filename': '382.csv', 'partnerid': 382, 'shopid': '63'},
	{'name': 'fine_caoyanglu', 'filename': '376.csv', 'partnerid': 376, 'shopid': '37'},
	{'name': 'fine_shangchenglu', 'filename': '377.csv', 'partnerid': 377, 'shopid': '38'}
]

for index in range(len(venues)):
	filename = venues[index]['filename']
	f = open(filename, "w")
	headers = "title_en, title_cn, day_num, start_time, end_time\n"
	f.write(headers)

	url = 'https://api.fineyoga.com/hall/course/index/course-plan/website-list'
	data = {
		'end_at': '2020-08-23 23:59:59',
	    'hall_id': venues[index]['shopid'],
	    'start_at': '2020-08-17 00:00:00'
	}

	data = parse.urlencode(data).encode()
	req =  request.Request(url, data=data)
	res = request.urlopen(req).read()
	contents = json.loads(res).get("data")

	for num in range(7):
		day_num = str(num + 1)
		class_num = num
		activities = contents[day_num]
		for activity in activities:
			title_en = activity.get("course_name_en")
			title_cn = activity.get("course_name")
			start_time = activity.get("start_time")
			end_time = activity.get("end_time")
			f.write(str(title_en) + "," + str(title_cn) + "," + str(class_num) + "," + str(start_time) + "," + str(end_time) + "," + "\n")

	f.close()