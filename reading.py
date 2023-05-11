from config import *
from parsing import *
import openpyxl
import matplotlib.pyplot as plt
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)



def get_img(datte, clas: str):
  wookbook = openpyxl.load_workbook(f"/outputs/{datte}.xlsx")
  ws = wookbook.active
  dict_classes = {
    '5': ['C 2', 'E 2'],
    '6': ['G 2', 'I 2'],
    '7': ['K 2', 'M 2'],
    '8': ['C 11', 'E 11'],
    '9': ['G 11', 'I 11'],
    '10': ['K 11'],
    '11': ['M 11']
  }
  time_classes = 'B 2'.split(' ')
  
  if clas != '10' and clas != '11':
    a_class = dict_classes[clas][0].split(' ')
    b_class = dict_classes[clas][1].split(' ')
    
    times = []
    a = []
    b = []

    for i in range(int(a_class[1]), int(a_class[1])+9):
      a.append(ws[f'{a_class[0]}{i}'].value)
      b.append(ws[f'{b_class[0]}{i}'].value)
      times.append(ws[f'{time_classes[0]}{i}'].value)
    
    #define figure and axes
    fig, ax = plt.subplots()
    im = plt.imread('/home/bot-schedule/bb.png')
    imagebox = OffsetImage(im, zoom = 0.05)
    ab = AnnotationBbox(imagebox, (0.05, 1), frameon = False)
    ax.add_artist(ab)
    #create values for table
    table_data=[]
    for g in zip(a,b, times):
      table_data.append(tuple([g[2], g[0], g[1]]))

    #create table
    plt.rcParams['font.family'] = 'Arial'
    table = ax.table(cellText=table_data, loc='center')
    csfont = {'fontname':'Arial'}
    # plt.title('f.png')
    ax.set_title(f"{clas} класс на {datte}", x=0.34, y=0.96, fontsize=10, fontweight='bold', **csfont, color='#048B7B')
    
    table[(0, 0)].set_facecolor("#048B7B")
    table[(0, 1)].set_facecolor("#048B7B")
    table[(0, 2)].set_facecolor("#048B7B")
    table[(0,0)].set_text_props(weight='bold', color='w')
    table[(0,1)].set_text_props(weight='bold', color='w')
    table[(0,2)].set_text_props(weight='bold', color="w")
    ax.axis('off')
    table.scale(1,2)
    #display table
    plt.savefig(f'/outputs/{datte} {clas}.png', dpi=800)
  else:
    time_classes = 'B 2'.split(' ')
    sep = dict_classes[clas][0].split(' ')
    
    times = []
    res = []

    for i in range(int(sep[1]), int(sep[1])+9):
      res.append(ws[f'{sep[0]}{i}'].value)
      times.append(ws[f'{time_classes[0]}{i}'].value)
    #define figure and axes
    fig, ax = plt.subplots()
    im = plt.imread('/home/bot-schedule/bb.png')
    imagebox = OffsetImage(im, zoom = 0.05)
    ab = AnnotationBbox(imagebox, (0.04, 1), frameon = False)
    ax.add_artist(ab)
    #create values for table
    table_data=[]
    for g in zip(res, times):
      table_data.append(tuple([g[1], g[0]]))



    #create table
    plt.rcParams['font.family'] = 'Arial'
    csfont = {'fontname':'Arial'}
    table = ax.table(cellText=table_data, loc='center')
    ax.set_title(f"{clas} класс на {datte}", x=0.26, y=0.96, fontsize=10, fontweight='bold', **csfont, color='#048B7B')
    #modify table
    table[(0, 0)].set_facecolor("#048B7B")
    table[(0, 1)].set_facecolor("#048B7B")
    table[(0,0)].set_text_props(weight='bold', color='w')
    table[(0,1)].set_text_props(weight='bold', color='w')
    table.scale(1,2)
    ax.axis('off')

    #display table
    plt.savefig(f'/outputs/{datte} {clas}.png', dpi=800)


def get_hw():
  ls = parsing_homework(get_data(0))[0]
  hws = parsing_homework(get_data(0))[1]
  ls.insert(0, str('Предметы'))
  hws.insert(0, str('Домашнее задание'))


  for n in hws:
    if len(n) > 100:

      # s = n.split(' ')
      # print(s)
      # s[int(len(s)/2)] = '\n'
      # s[int(len(s)/2/2)] = '\n'
      hws.insert(hws.index(n), "".join(n.split(' ')[:4]))
      hws.remove(n)


  fig, ax = plt.subplots()
  im = plt.imread('/home/bot-schedule/bb.png')
  imagebox = OffsetImage(im, zoom = 0.06)
  ab = AnnotationBbox(imagebox, (0.5, 1), frameon = False)
  ax.add_artist(ab)
  table_data=[]
  for g in zip(ls, hws):
    table_data.append(tuple([g[0], str(g[1])]))
  plt.rcParams['font.family'] = 'Arial'
  table = ax.table(cellText=table_data, loc='center')
  
  table[(0, 0)].set_facecolor("#048B7B")
  table[(0, 1)].set_facecolor("#048B7B")
  table[(0,0)].set_text_props(weight='bold', color='w')
  table[(0,1)].set_text_props(weight='bold', color='w')
  table.scale(1, 4)

  ax.axis('off')
  plt.savefig(f'/outputs/hw {tomorrow()}.png', dpi=800)
