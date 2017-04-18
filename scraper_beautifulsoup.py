#weather forecast scraper modified, original tutorial is found on dataquest.io

import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
this_afternoon = forecast_items[0]
tonight = forecast_items[1]

#scrape data for this afternon:
this_aft = this_afternoon.find(class_="period-name").get_text()
print (this_aft)
aft_desc = this_afternoon.find(class_="short-desc").get_text()
print (aft_desc)
temp_h = this_afternoon.find(class_="temp temp-high").get_text()
print ("Temperature High:",temp_h)
img_now = this_afternoon.find("img")
desc_now = img_now['title']
print (desc_now)

#scrape data for tonight:
tonite = tonight.find(class_="period-name").get_text()
print (tonite)
tonite_desc = tonight.find(class_="short-desc").get_text()
print (tonite_desc)
temp_l = tonight.find(class_="temp temp-low").get_text()
print ("Temperature Low:",temp_l)
img_later = tonight.find("img")
desc_later = img_later['title']
print (desc_later)

#define a period of time and create a Data Frame with pandas
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]

short_desc2 = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]

temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]

descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

weather = pd.DataFrame({"period": periods, "short-desc": short_desc2, "temp":temps})
print ("Data Frame:")
print (weather)

temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"] = temp_nums.astype('int')
print ("Temperatures only:", temp_nums)

