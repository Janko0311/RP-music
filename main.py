# This program was created in Arduino Lab for MicroPython
from machine import Pin
import time
import random
btn = Pin("GP16",Pin.IN)
led = [None]*11#use array to store
led[1]=Pin("GP15", Pin.OUT)
led[2]=Pin("GP14", Pin.OUT)
led[3]=Pin("GP13", Pin.OUT)
led[4]=Pin("GP12", Pin.OUT)
led[5]=Pin("GP11", Pin.OUT)
led[6]=Pin("GP10", Pin.OUT)
led[7]=Pin("GP9", Pin.OUT)
led[8]=Pin("GP8", Pin.OUT)
led[9]=Pin("GP7", Pin.OUT)
led[10]=Pin("GP6", Pin.OUT)
def forward():#for loop--Right to left
  for i in range(10,1,-1):  
      led[i].value(1)
      time.sleep(AnimationSpeed)
      led[i].value(0)
    

def backward():#for loo--left to right
   for i in range(1,10):  
       led[i].value(1)
       time.sleep(AnimationSpeed)
       led[i].value(0)
def spread():  #LEDs ANIMATE MIDDLE TO PERIPHERAL
  led[5].value(1)
  led[6].value(1)
  time.sleep(AnimationSpeed)
  time.sleep(AnimationSpeed)
  led[5].value(0)
  led[6].value(0)
  led[4].value(1)
  led[7].value(1)
  time.sleep(AnimationSpeed)
  time.sleep(AnimationSpeed)
  led[4].value(0)
  led[7].value(0)
  led[3].value(1)
  led[8].value(1)
  time.sleep(AnimationSpeed)
  time.sleep(AnimationSpeed)
  led[3].value(0)
  led[8].value(0)
  led[2].value(1)
  led[9].value(1)
  time.sleep(AnimationSpeed)
  time.sleep(AnimationSpeed)
  led[2].value(0)
  led[9].value(0)
  led[1].value(1)
  led[10].value(1)
  time.sleep(AnimationSpeed)
  time.sleep(AnimationSpeed)
  led[1].value(0)
  led[10].value(0)
beat_interval = 60 / 120
def GoldenHourJVKE():
    #random LED pins
    led_to_flash = random.choice(led[1:11])
    led_to_flash.value(1)  # Turn on
    time.sleep(beat_interval / 4)  # Flash for a quarter of the beat
    led_to_flash.value(0)  # Turn off


def off():  
  print("sleep..waiting for user respond....")  
  
  
  
  

AnimationType=""
AnimationSpeed=0.07  #time for the next led
#main while loop for mode switching
while True:
  if btn.value()==1:
    if AnimationType=="forward":
      AnimationType="backward"
    elif AnimationType=="backward":
      AnimationType="spread"
    elif AnimationType=="spread":
      AnimationType="song"
    elif AnimationType=="song":
      AnimationType="off"
    elif AnimationType=="off":
      AnimationType="forward"
    else:
      AnimationType="forward"
      
    time.sleep(0.5)
#animation method calling
  if AnimationType=="forward":
    forward()
  elif AnimationType=="backward":
    backward()
  elif AnimationType=="spread":
    spread()
  elif AnimationType=="song":
    GoldenHourJVKE()
  elif AnimationType=="off":
    off()
  

    



  
