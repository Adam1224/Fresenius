import RPi.GPIO as GPIO
import time,datetime
GPIO.setmode(GPIO.BOARD)

start_time=datetime.datetime.now().strftime("%H:%M:%S")

port_flowsensor_1=13
port_flowsensor_2=15

GPIO.setup(port_flowsensor_1, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)   #通(port_flowsensor_1号引脚读取左轮脉冲数据
GPIO.setup(port_flowsensor_2, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)   #通(port_flwosensor_2号引脚读取右轮脉冲数据

counter_flowsensor_1=0      #左轮脉冲初值
counter_flowsensor_2=0     #右轮脉冲初值

def my_callback_1(channel):          #边缘检测回调函数，详情在参见链接中
    global counter_flowsensor_1                 #设置为全局变量
    if GPIO.event_detected(port_flowsensor_1):        #检测到一个脉冲则脉冲数加1
        counter_flowsensor_1=counter_flowsensor_1+1

def my_callback_2(chanel):            #这里的channel和channel1无须赋确定值，但笔者测试过，不能不写
    global counter_flowsensor_2
    if GPIO.event_detected(port_flowsensor_2):
        counter_flowsensor_2=counter_flowsensor_2+1

GPIO.add_event_detect(port_flowsensor_1,GPIO.RISING,callback=my_callback_1) #在引脚上添加上升临界值检测再回调
GPIO.add_event_detect(port_flowsensor_2,GPIO.RISING,callback=my_callback_2)

K_factor_1 = 104650
K_factor_2 = 450
calculate_duration=1
seconds_in_one_minute=60
time_new = 0.0

while True:

    last_counter_flowsensor_1=counter_flowsensor_1
    last_counter_flowsensor_2=counter_flowsensor_2

    time.sleep(calculate_duration)

    current_counter_flowsensor_1=counter_flowsensor_1
    current_counter_flowsensor_2=counter_flowsensor_2

    flow_rate_1=round(1000*(current_counter_flowsensor_1-last_counter_flowsensor_1)*seconds_in_one_minute/(K_factor_1*calculate_duration),2)
    total_volume_1=round(counter_flowsensor_1/K_factor_1,2)

    flow_rate_2=round(1000*(current_counter_flowsensor_2-last_counter_flowsensor_2)*seconds_in_one_minute/(K_factor_2*calculate_duration),2)
    total_volume_2=round(counter_flowsensor_2/K_factor_2,2)
    
    print("\nSince",start_time,"Unitl",datetime.datetime.now().strftime("%H:%M:%S"))   
    print("Current Flow Rate #1 =",flow_rate_1,'mL/min','Total Volume #1 =',total_volume_1,"L")
    print("Current Flow Rate #2 =",flow_rate_2,'mL/min','Total Volume #2 =',total_volume_2,"L")
    print(counter_flowsensor_1,counter_flowsensor_2)

GPIO.cleanup()
