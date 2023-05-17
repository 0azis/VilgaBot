import urllib.request



def download(data, res: str): 
  try:
    urllib.request.urlretrieve(f"https://nvschool3.ru/upload/iblock/{res}/{data}%20%D0%9E%D0%A1%D0%9D%D0%9E%D0%92%D0%9D%D0%90%D0%AF%20%D0%98%20%D0%A1%D0%A0%D0%95%D0%94%D0%9D%D0%AF%D0%AF%20%D0%A8%D0%9A%D0%9E%D0%9B%D0%90.xlsx", f"/outputs/{data}.xlsx")
  except Exception as _ex:
    print("Error", _ex)
