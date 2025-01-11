import os
import time 
import threading 
import bubble 
keepon = True 
opened = False 
espaces =' '*25 
def displayApps() :
  print('Terminal = /terminal\nBubble = /search\nOpenIDE = /py\nLumina = /lumina')
def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def login() : 
  clearScreen()
  username = input('🚹')
  password = input('🔒')
  if username == 'live session' and password == 'live' :
    clearScreen()
    print('🚹'+username)
    print('🔓'+password)
    print('Connecting...')
    time.sleep(1)
    return True
  else :
    return False 
def terminal() :
  command = input('usr///live_session_user:/bash $ ')
  if command == 'shutdown' :
    clearScreen()
    print(espaces+'Goodbye...')
    time.sleep(2)
    while True :
      clearScreen()
  elif command == 'logout' :
    opened = False 
def research() :
  bubble.Bubble() 
def openIde() :
  while True :
    command = input('>>>')
    if command == '/quit' :
      break
    else :
      try :
        exec(command)
      except :
        print('Traceback (most recent call last) :\nfile = \'usrCommand\' : Unknown Error') 
def luminaApp() :
  while True :
    text = input(espaces + 'Lumina Editor\n')
    if text == '/quit' :
      break
    else :
      namefile = input('Type the name of the file or create new one : ')
      f = open(namefile, 'w+')
      f.write(text)
      f.close()
def background() :
  from turtle import *
  global t
  t = Turtle()
  t.shape(image('background.png'))
  def move() :
    while True :
      t.goto(200, 0)
      time.sleep(0.5)
      t.goto(-200, 0)
    thr = threading.Thread(target=move)
    thr.start()
def desktop() :
  if opened == False :
    print('Welcome to BoltOS.')
    print('The lightning fast web operationg system.')
    time.sleep(1)
    while True :
      a = login()
      if a :
        break
      else :
        print('Incorrect username or password')
    displayApps()
    app = input('action : ')
    if app == '/terminal' :
      terminal() 
    elif app == '/search' :
      research()
    elif app == '/py' :
      openIde()
    elif app == '/lumina' :
      luminaApp()
    else :
      print('Unknown app')
background()
while keepon :
  desktop()
  opened = True
      
