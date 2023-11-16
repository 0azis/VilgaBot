import requests
from bs4 import BeautifulSoup


def math(classs: str, problem: str):
  r = requests.get(f'https://gdz.ru/class-{classs}/algebra/')
  soup = BeautifulSoup(r.text, 'html.parser')
  books = soup.find_all("a", {'class': "book book-regular text-undecorated"})
  books2 = soup.find_all("span", {'itemprop': "author"})
  
  url = ''
  for i in zip(books2, books):
    if classs != '10' and classs != '11':
      if str(i[0].contents[0].split(',')[0]) == "Ю.Н. Макарычев":
        url = i[1]['href']
        break
    else:
      if str(i[0].contents[0].split(',')[0]) == "А.Г. Мордкович":
        url = i[1]['href']
        break
  


  r2 = requests.get(f'https://gdz.ru{url}')
  soup2 = BeautifulSoup(r2.text, 'html.parser')
  tasks = soup2.find_all("a", {'class': "task-button js-task-button"})


  task_url = ''
  for n in tasks:
    if str(n['title']) == problem:
      task_url = n['href']

  r3 = requests.get(f'https://gdz.ru{task_url}')
  soup3 = BeautifulSoup(r3.text, 'html.parser')
  solution = soup3.find_all("div", {'class': "with-overtask"})
  soup4 = BeautifulSoup(str(solution), 'html.parser')
  solution2 = soup4.find_all("img")
  solution_url = 'https:' + solution2[0]['src']
  
  img_data = requests.get(solution_url).content
  with open(f'./outputs/{problem} {classs}.jpg', 'wb') as handler:
    handler.write(img_data)
