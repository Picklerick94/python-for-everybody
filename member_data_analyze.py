import csv
import json

with open('query_results.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    high = 0
    middle = 0
    low = 0
    for row in reader:
    	badge_num = len(json.loads(row['badges']))
    	if (badge_num <= 3):
    		low += 1
    	elif (badge_num <= 5 & badge_num > 3):
    		middle += 1
    	else:
    		high += 1
    print(high, middle, low)