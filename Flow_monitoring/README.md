Flow_monitoring Project document
In the project, DS18B20(temperature sensor)\equflow0045(flowsensor)\waveshare2.13d(E-paper) are used to monitor flow parameters.

===========================================
# Setup

1 temperature sensor(DS18B20)
1.1 wire connection

Sensor side ==> raspberry side
VCC ==> Ground
GND ==> 3.3V/5V
signal ==> BOARD #7 (BCM #4)

Notice: A pull-up resistor(4.7K) is required between the signal wire and power wire.

1.2 purchase link 

【防水 DS18b20温度探头 水温探头 不锈钢封装 传感器 适用于树莓派】https://m.tb.cn/h.VaPPxJZ?sm=3f9441

1.3 help link 
https://www.jianshu.com/p/1aeed4cfd431

2 flow sensor(equflow0045)
2.1 wire connection

Sensor side ==> raspberry side
GND ==> Ground
VCC ==> 5V
signal ==> BOARD #13 (BCM #27)

Notice: Please notice that the sensor has A certain flow direction.
DO NOT throw away the tag on which "K-factor" is written. 'K-factor' means how many pulses the sensor sends when 1 Liter of water is passed through this particular sensor.

2.2 purchase link
ask James

2.3 help link
https://www.equflow.com/products/flowmeters/non-disposable-flowmeters/pvdf-turbine-flowmeter

3 E-paper(waveshare 2.13d inch )
3.1 wire connection
Sensor side ==> raspberry side
VCC ==> 3.3V
GND ==> GND
DIN ==> BOARD #19 (BCM #10)
CLK ==> BOARD #23 (BCM #11)
CS ==> BOARD #24 (BCM #8)
DC ==> BOARD #22 (BCM #25)
RST ==> BOARD #11 (BCM #17)
BUSY ==> BOARD #18 (BCM #24)

Notice: Be very gentle when handle the E-paper, because the wire fibre is very fragile

3.2 purchase link
【微雪 e-paper 墨水屏 电子纸 显示模块 局部刷新 适用于树莓派4代】https://m.tb.cn/h.eAYhCml?sm=e27eb0

3.3 help link
http://www.waveshare.net/wiki/2.13inch_e-Paper_HAT_(D)

===========================================
# Program execution

1 SSH the raspberry pi 4B
1.1 help link 
https://www.raspberrypi.org/documentation/remote-access/ssh/

2 run vncserver(optional)
2.1 help link 
https://www.realvnc.com/en/connect/download/vnc/

3 in terminal: cd /home/pi/Projects/Flow_monitoring/python/examples

Notice: this is the location 'flow_monitoring.py' is stored.
DO NOT recommand move it to another locaiton, which will cause 'ModuleNotFoundError' error.
If you insist, make sure all the modules required to be imported are able to be found by compiler after you relocate 'flow_monitoring.py'.

4 in terminal: python3 flow_monitoring.py ls > XX.csv
Notice: 'flow_monitoring.py' will start to run after 'return' is pressed, and the monitor data file will generate automatically named as'XX.csv'
Make sure the flow starts after there is data shown on E-paper, and 'ctrl+c' to stop the program after the date on E-paper no longer changes.

5 open **.csv
use "text to data" function to Convert single row of text into 6 rows of data
row #1: programme start time 
row #2: the time when present data is captured
row #3: total volume
row #4: current flow rate
row #5: current temperature
row #6:  total pulses flow sensor detected 

