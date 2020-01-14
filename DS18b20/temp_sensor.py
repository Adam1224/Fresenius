import glob
import time

#RATE = 30

#time.sleep(RATE)

tfile=open("/sys/bus/w1/devices/28-011453440eaa/w1_slave")

text=tfile.read()

#tfile.close()

secondline=text.split("\n")[1]

temperaturedata=secondline.split(" ")[9]

temperature=float(temperaturedata[2:])

temperature=temperature/1000
#打印值
print(temperature)
