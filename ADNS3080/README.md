# ADNS-3080 example code
For ADNS-3080, the function of capturing speed and picture is realised.

===========================================
# Setup
1 speed 
1.1 wire connection

GND ==> GND 
5V ==> 5V
NCS ==> 2
MISO ==> 12
MOSI ==> 11
SCLK ==> 13
RST ==> 3

arduino connects to mac/pc via USB

1.2 upload Speed.ino => turn on serial monitor

2 picture 
2.1 wire connection

GND ==> GND 
5V ==> 5V
NCS ==> 10
MISO ==> 12
MOSI ==> 11
SCLK ==> 13
RST ==> 9

arduino connects to mac/pc via USB

2.2 upload Picture.ino => run ADNS3080ImageGrabber on mac/pc


