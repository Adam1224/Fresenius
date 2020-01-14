import RPi.GPIO as GPIO
import time,datetime
GPIO.setmode(GPIO.BOARD)

start_time=datetime.datetime.now().strftime("%H:%M:%S")

port_flowsensor_1=13
port_flowsensor_2=15

GPIO.setup(port_flowsensor_1, GPIO.IN,pull_up_down=GPIO.PUD_UP)   #通(port_flowsensor_1号引脚读取左轮脉冲数据
# GPIO.setup(port_flwosensor_2, GPIO.IN,pull_up_down=GPIO.PUD_UP)   #通(port_flwosensor_2号引脚读取右轮脉冲数据

counter_flowsensor_1=0      #左轮脉冲初值     

def my_callback(channel):          
    global counter_flowsensor_1                 
    if GPIO.event_detected(port_flowsensor_1):        
        counter_flowsensor_1=counter_flowsensor_1+1


GPIO.add_event_detect(port_flowsensor_1,GPIO.RISING,callback=my_callback) #在引脚上添加上升临界值检测再回调
# GPIO.add_event_detect(port_flwosensor_2,GPIO.RISING,callback=my_callback1)

K_factor_1 = 98160
calculate_duration=1
seconds_in_one_minute=60
time_new = 0.0

while True:

    last_counter_flowsensor_1=counter_flowsensor_1
    time.sleep(calculate_duration)
    current_counter_flowsensor_1=counter_flowsensor_1
    flow_rate=round(1000*(current_counter_flowsensor_1-last_counter_flowsensor_1)*seconds_in_one_minute/(K_factor_1*calculate_duration),2)
    total_volume=round(counter_flowsensor_1/K_factor_1,2)
    
    
    print("\nSince",start_time,"Unitl",datetime.datetime.now().strftime("%H:%M:%S"))   
    print("Current Flow Rate =",flow_rate,'mL/min','Total Volume =',total_volume,"L")
    
GPIO.cleanup()