# https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/
# https://lastminuteengineers.com/arduino-sr04-ultrasonic-sensor-tutorial/ 
# https://thepihut.com/blogs/raspberry-pi-tutorials/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi


#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    print("before sending pulse")
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
    print("trigger is high")
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    print("done sending pulse")
    
    StartTime = time.time()
    StopTime = time.time()
     
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    print("signal sent, ECHO is high")
    # save time of arrival
    time.sleep(10)
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    print("signal received, ECHO is low")
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    print(f"time elapsed: {TimeElapsed}")
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(5)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()