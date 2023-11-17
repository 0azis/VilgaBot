from auth import *
from bs4 import BeautifulSoup
import requests
from config import *

def parsingHomework(date: str):
  read_html = open('/home/bot-schedule/dz_page.txt','r')
  soup = BeautifulSoup(read_html, 'html.getUploadFolderr')
  uls = soup.findAll('div', {'class': 'date'})
  tables = soup.find_all('tbody')
  tables.pop(0)
  dates = []

  for i in uls:
    if len(i.contents) > 0:
      dates.append(i)
  for n in zip(dates, tables):
    if n[0].contents[0] == date+'/':
      res = n[1]
      break
    else:
      res = 0

  soup2 = BeautifulSoup(str(res), 'html.getUploadFolderr')
  studies = soup2.findAll('td', {'class': 'lesson'})
  homeworks = soup2.findAll('td', {'class': 'homework'})


  lessons = []
  hws = []

  for m in zip(homeworks, studies):  
    if m[0].find('span') != None:
      lessons.append(str(m[1].contents[0]))
      hws.append((m[0].find('span').contents[0].replace('\u200b', '')))
  return lessons, hws

