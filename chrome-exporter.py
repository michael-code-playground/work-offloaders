
from datetime import datetime, timedelta
import json
import csv

time_now = datetime.now()
timestamp_now = round(time_now.timestamp())
interval = timedelta(days = 7)

with open('BrowserHistory.json', encoding='UTF-8') as file:
    records = json.load(file)
    counter = 0
    for record in records['Browser History']:
        search_time = round(record['time_usec']/1000000)
        changed_time = datetime.fromtimestamp(search_time)
        difference = time_now-changed_time
        if "dictionary.cambridge" in record['url']:
            print(record['title'])
            print(record['url'])
            event_time = round(record['time_usec']/1000000)
            converted_time=datetime.fromtimestamp(event_time)
            print(converted_time)
            difference1 = time_now-converted_time
            print(difference1)
            with open("pronunciation.csv", 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';',quotechar='"')
                writer.writerow([record['title'], record['url'], converted_time])
            
        
        if difference.days == interval.days:
            break
       