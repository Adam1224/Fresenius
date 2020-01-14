#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys,threading
import RPi.GPIO as GPIO
import time,datetime
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13d
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import glob

GPIO.setmode(GPIO.BCM)
flowsensor_pin = 27
GPIO.setup(flowsensor_pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

rate_cnt = 0
flowsensor_counter = 0
K_factor = 88300
flowrate_calculate_duration=1
seconds_in_one_minute=60
time_new = 0.0

flow_rate=0
total_volume=0
start_time=datetime.datetime.now().strftime("%H:%M:%S")

def flowsensor_callback(channel):          #边缘检测回调函数，详情在参见链接中
    global flowsensor_counter                 #设置为全局变量
    if GPIO.event_detected(flowsensor_pin):        #检测到一个脉冲则脉冲数加1
        flowsensor_counter=flowsensor_counter+1

GPIO.add_event_detect(flowsensor_pin,GPIO.RISING,callback=flowsensor_callback)

logging.basicConfig(level=logging.DEBUG)

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13d
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

#Set output log level
logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd2in13d Demo")
    
    epd = epd2in13d.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear(0xFF)
    
    font11 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 11)
    font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
    font20 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 20)
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)

    epd.init()    
    epd.Clear(0xFF)
    
    time_image = Image.new('1', (epd.width, epd.height), 255)
    time_draw = ImageDraw.Draw(time_image)

    while (True):

        #flowrate stars here
        last_flowsensor_counter=flowsensor_counter
        time.sleep(flowrate_calculate_duration)
        current_flowsensor_counter=flowsensor_counter

        flow_rate=round(1000*(current_flowsensor_counter-last_flowsensor_counter)*seconds_in_one_minute/(K_factor*flowrate_calculate_duration),2)
        total_volume=round(flowsensor_counter/K_factor,2)
        #flowrate ends here


        #temp stars here
        
        #tempsensor_pin=7(board)
        tfile=open("/sys/bus/w1/devices/28-011453440eaa/w1_slave")
        text=tfile.read()
        tfile.close()
        secondline=text.split("\n")[1]

        temperaturedata=secondline.split(" ")[9]
        temperature=round((float(temperaturedata[2:]))/1000,1)

        #temp ends here

        def epaper_display():

            print(start_time,datetime.datetime.now().strftime("%H:%M:%S"),total_volume,flow_rate,temperature,flowsensor_counter)
#             print(start_time,datetime.datetime.now(),total_volume,flow_rate,temperature)
        
            
            Himage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
            draw = ImageDraw.Draw(Himage)
            
            draw.text((25, 10), u'温度:', font = font15, fill = 0)
            draw.text((65, 10), str(temperature), font = font15, fill = 0)
            draw.text((95, 10), u'摄氏度', font = font15, fill = 0)
            
            draw.text((25, 25), u'流速:', font = font15, fill = 0)
            draw.text((65, 25), str(flow_rate), font = font15, fill = 0)
            draw.text((95, 25), u'毫升/分钟', font = font15, fill = 0)
            
            draw.text((25, 40), u'流量:', font = font15, fill = 0)
            draw.text((65, 40), str(total_volume), font = font15, fill = 0)
            draw.text((95, 40), u'升', font = font15, fill = 0)
            
            draw.text((100, 55), time.strftime('%H:%M:%S'), font = font15, fill = 0)
            draw.text((30, 55), start_time,font = font15, fill = 0)
            
            draw.text((5, 75), u'Fresenius Medical Care', font = font20, fill = 0)
            epd.display(epd.getbuffer(Himage))       

        t = threading.Thread(target=epaper_display)
        t.start()

    logging.info("Clear...")
    epd.Clear(0xFF)
    
    logging.info("Goto Sleep...")
    epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in13d.epdconfig.module_exit()
    exit()

