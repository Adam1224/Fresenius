import RPi.GPIO as GPIO
import time,datetime
GPIO.setmode(GPIO.BOARD)
inpt = 13
GPIO.setup(inpt,GPIO.IN)
rate_cnt = 0
total_cnt = 0
my_total_cnt=0
K_factor = 98160
rate_calculate_duration=1
seconds_in_one_minute=60
time_new = 0.0

flow_rate=0
total_volume=0
start_time=datetime.datetime.now().strftime("%H:%M:%S")

#print('Start_time:',start_time)

def my_callback(channel):
    my_rate_cnt+=1
    my_total_cnt+=1
    
while True:
    time_new = time.time()+rate_calculate_duration
    rate_cnt = 0
    my_rate_cnt=0
    while time.time() <= time_new:
        if GPIO.input(inpt)!=0:
            rate_cnt += 1
            total_cnt += 1
        if GPIO.wait_for_edge(inpt, GPIO.RISING,timeout=rate_calculate_duration*1000):
            my_rate_cnt+=1
            my_total_cnt+=1

    
  
    GPIO.add_event_detect(channel, GPIO.RISING, callback=my_callback)

    flow_rate=round(my_rate_cnt*seconds_in_one_minute/(K_factor*rate_calculate_duration),2)
    total_volume=round(my_total_cnt/K_factor,2)
    
    print("\nCurrent Flow Rate =",flow_rate,'Liter/min')
    print("Since",start_time,"Unitl",datetime.datetime.now().strftime("%H:%M:%S"))
    print('Total Volume =',total_volume,"L")
    
    
    
#     print('\n Liter / min =',round(rate_cnt*seconds_in_one_minute/(K_factor*rate_calculate_duration),2))
#     print(' Total Liter =',round(total_cnt/(K_factor),2))
        # print('time (min & clock',minutes,'\t',time.asctime(time_new))
GPIO.cleanup()
print('Done')



