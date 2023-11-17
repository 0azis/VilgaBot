import urllib.request

def DownloadSchedule(data, res: str): 
  try:
    urllib.request.urlretrieve(f"https://nvschool3.ru/upload/iblock/{res}/{data}%20%D0%9E%D0%A1%D0%9D%D0%9E%D0%92%D0%9D%D0%90%D0%AF%20%D0%98%20%D0%A1%D0%A0%D0%95%D0%94%D0%9D%D0%AF%D0%AF%20%D0%A8%D0%9A%D0%9E%D0%9B%D0%90.xlsx", f"./outputs/{data} schedule.xlsx")
  except Exception as _ex:
    raise "Ошибка при скачивании расписания"

def DownloadFood(data):
  try:
    urllib.request.urlretrieve(f"https://nvschool3.ru/food/{data}-sm.xlsx", f"./outputs/{data} food.xlsx")
  except Exception as _ex:
    raise "Ошибка при скачивании меню"
