from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import csv

for year in range(2020,2037):
    y = year; year = str(year)
    tide_website = urlopen('https://tides.mobilegeographics.com/calendar/year/7137.html?y='+year).read()

    m = 0
    formatted_data = []
    data = BeautifulSoup(tide_website,'lxml').findChildren('td')

    for i in range(0,len(data)-10,11):
        d = int(data[i].text[4:6])
        if d == 1:
            m += 1
        for j in range(5):
            hl = data[i+j+1].text
            if hl == '':
                continue
            ti = hl.index('WAT ')+4
            tide = hl[ti:len(hl)-2]
            time = hl[:hl.index(' WAT')]

            date = datetime.date(y,m,d).strftime('%m-%d-%y')
            time = datetime.datetime.strptime(time,'%I:%M %p').strftime('%H:%M')
            date_time = date+' '+time

            formatted_data.append((date_time,tide))

    with open('C:\\Users\\Astro\\Desktop\\tides\\tides_'+year+'.csv', 'w', newline='') as csvfile:
        tides_writer = csv.writer(csvfile, delimiter = ',')
        tides_writer.writerows(formatted_data)