from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
from time import sleep
from threading import Thread

lcd = LCD()

def safe_exit(signum, frame):
  exit(1)

signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

def display(str, line, timeout=0.25):
  WINDOW_SIZE = 16
  if len(str) <= 16:
    lcd.text(str, line)
    return
  l = WINDOW_SIZE
  str = (" " * WINDOW_SIZE) + str
  while True:
    disp = str[l:]
    lcd.text(disp, line)
    l = (l + 1) % len(str)
    if l == WINDOW_SIZE:
      sleep(timeout * 4)
      continue
    sleep(timeout)

str1 = "Hi there!"
str2 = "I'm DanielT. I'm programming with the LCD1602 display ahahahahahahah!"

try:
  display(str2, 2)
  pause()
except KeyboardInterrupt:
  pass
finally:
  lcd.clear()

