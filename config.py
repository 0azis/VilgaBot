# Config with time settings
# 
import datetime
import time
import requests
from bs4 import BeautifulSoup


# creating the today date for sending schedule for that date
dt_now = str(datetime.datetime.now()).split(" ")[0].split('-')

# today is variable with today date, using in function "Gimme the schedule"
# today = str(dt_now[2] + '.' + dt_now[1] + '.' + dt_now[0])
# folder_today is variable, which contains folder for URL link for schedule
# folder_today = str(getUploadFolder(today))


def getUploadFolder(date: str):
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

TIME_TO_SEND = '17:00( 00 )'
def check_send_time():
  t_n = str(datetime.datetime.now()).split(' ')[1].split(':')
  time_now = str(t_n[0] + ":" + t_n[1] + "( " + t_n[2].split('.')[0] + " )")
  if time_now == TIME_TO_SEND:
    return True

# return tomorrow
def tomorrow():
  week_day = datetime.datetime.today().weekday()
  if week_day == 5 or week_day == 4:
    if int(dt_now[2]) < 9:
      s = str(datetime.datetime.now()).split(" ")[0].split('-')
      s[2] = '0' + str(int(s[2])+2) 
      tomorrow = str(str(s[2]) + '.' + s[1] + '.' + s[0])
      return str(tomorrow)
    else:
      s = str(datetime.datetime.now()).split(" ")[0].split('-')
      s[2] = int(s[2])+3
      tomorrow = str(str(s[2]) + '.' + s[1] + '.' + s[0])
      return str(tomorrow)
  else:
    if int(dt_now[2]) < 9:
      s = str(datetime.datetime.now()).split(" ")[0].split('-')
      s[2] = '0' + str(int(s[2])+1) 
      tomorrow = str(str(s[2]) + '.' + s[1] + '.' + s[0])
      return str(tomorrow)
    else:
      s = str(datetime.datetime.now()).split(" ")[0].split('-')
      s[2] = int(s[2])+1
      tomorrow = str(str(s[2]) + '.' + s[1] + '.' + s[0])
      return str(tomorrow)

def get_data(option: int):
  date = tomorrow()
  # options: 
  # 0 - number will be like '01'
  # 1 - number will be like '1'
  if option == 0:
    date = str(date.split('.')[0])
  else:
    date = str(date.split('.')[0]).replace('0', '')
  return str(date)

def FoodTime():
  dt_now = str(datetime.datetime.now()).split(" ")[0].split("-")
  dt_now[2] = str(int(dt_now[2]) + 1)
  return '-'.join(dt_now)
  
