#!/bin/python3
#Author PyLogik, Title: Lesson 7
#Description: A simple model of a thermometer.

from vpython import *
import serial
import time

pico_data = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(1)

origin_shift = -12
display = label(text='null',height=15,box=False,pos=vector(0,-20.5,0))

merc_fluid_base = sphere(size=vector(6,6,6), color=color.red, 
                  pos=vector(0,-8+origin_shift,0))
merc_fluid_body = cylinder(size=vector(6,2,1.7), color=color.red,
                  axis=vector(0,1,0), pos=vector(0,-5.5+origin_shift,0))
annoying_thermo_line = box(size=vector(36,1,.5), color=color.white,
                pos=vector(0,12+origin_shift,1), opacity=.4, axis=vector(0,1,0))

glass_tube = cylinder(size=vector(35,4,3), color=color.white, opacity=.3,
             axis=vector(0,1,0), pos=vector(-0,-4.5+origin_shift,0))
glass_ball = sphere(size=vector(8,8,8), color=color.white, opacity=.3,
             pos=vector(0,-8+origin_shift,0))

backboard = box(size=vector(50,12,1), color=color.white,
                pos=vector(0,10+origin_shift,0), axis=vector(0,1,0), opacity=.98,
                shininess=1)
label  = text(text=str('PyLogik'), align='center', height=1.5, depth=.01,
        color=color.black, pos = vector(0, 32+origin_shift, .5))
celsius_label =  text(text=str('C'), align='center', height=2,
             color=color.black, pos=vector(3.5,-3.8+origin_shift,.5), 
             shininess=.01)
fahrenheit_label =  text(text=str('F'), align='center', height=2,
             color=color.black, pos=vector(-3.5,-3.8+origin_shift,.5), 
             shininess=.01)
    
for celsius_digits in range(-40,55, 5):
    indicator = .289*celsius_digits + 11.6
    indicator = round(indicator, 2)
    number = text(text=str(celsius_digits), align='center', height=1,
             color=color.black, pos=vector(4.5,indicator+origin_shift,.5), 
             shininess=.01)
    major_tick_marks = text(text=str('-'), align='center', height=1,
                 color=color.black, pos=vector(2.75,indicator+origin_shift,.5), 
                 shininess=.01)
for fahrenheit_digits in range(-40, 130, 10):
    indi = .161*fahrenheit_digits + 6.54
    indi = round(indi, 2)
    number = text(text=str(fahrenheit_digits), align='center', height=1,
             color=color.black, pos=vector(-4.5,indi+origin_shift,.5),
             shininess=.01)
for  f_ticks in range(-40,121, 10):
    indi = .161*f_ticks + 6.54
    indi = round(indi, 2)
    testing = text(text=str('-'), align='center', height=1,
             color=color.black, pos=vector(-2.75,indi+origin_shift,.5), 
             shininess=.01)
for celsius_ticks in range(-40,51,1):
    indicator = .289*celsius_ticks + 11.6
    indicator = round(indicator, 2)
    tick_marks = text(text=str('-'), align='center', height=1,
                 color=color.black, pos=vector(2.5,indicator+origin_shift,.5), 
                 shininess=.01)    
for  f_ticks in range(-40,121, 2):
    indi = .161*f_ticks + 6.54
    indi = round(indi, 2)
    testing = text(text=str('-'), align='center', height=1,
             color=color.black, pos=vector(-2.5,indi+origin_shift,.5), 
             shininess=.01)
    
def thermo():
    j = (temp)
    merc_val = 0.29*j + 11.56
    merc_thermo_analog = cylinder(size=vector(merc_val,2,1.7), color=color.red,
        axis=vector(0,1,0), pos=vector(0,.5+origin_shift,0))
    display.text=str(temp)
    merc_thermo_analog.visible = True
    time.sleep(1)
    merc_thermo_analog.visible = False  
    time.sleep(.001)
    del merc_thermo_analog   
 
while True:
    while pico_data.in_waiting == 0:
        pass
 
    daata = pico_data.readline()
    temp = float(daata.decode('utf-8'))
    temp = round(temp,2)
    thermo()
    
    







