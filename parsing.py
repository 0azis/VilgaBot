from auth import *
from bs4 import BeautifulSoup
import requests
from config import *

def parse(date: str):
  r = requests.get('https://nvschool3.ru/raspisanie/')
  soup = BeautifulSoup(r.text, 'html.parser')
  all_p = soup.findAll('p', {'class': 'news-item'})
  soup2 = BeautifulSoup(str(all_p), 'html.parser')
  all_a = soup2.findAll('a')
  res = []
  # creating list with res
  for i in all_a:
    local = str(i['href']).split("/")
    local.insert(4, local[4].split(" "))
    res.append(local)
  for g in res:
    if g[4][0] == date and g[4][1] == "ОСНОВНАЯ":
      return str(g[3])
    elif g[4][1] == "ОСНОВНАЯ":
      return list([str(g[4][0]), str(g[3])])


def parsing_homework(date: str):
  isThere = False
  read_html = open('/home/bot-schedule/dz_page.txt','r')
  soup = BeautifulSoup(read_html, 'html.parser')
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

  soup2 = BeautifulSoup(str(res), 'html.parser')
  studies = soup2.findAll('td', {'class': 'lesson'})
  homeworks = soup2.findAll('td', {'class': 'homework'})


  lessons = []
  hws = []

  for m in zip(homeworks, studies):  
    if m[0].find('span') != None:
      lessons.append(str(m[1].contents[0]))
      hws.append((m[0].find('span').contents[0].replace('\u200b', '')))
  return lessons, hws

