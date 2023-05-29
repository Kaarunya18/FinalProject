import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 18
ECHO = 24
buzzer = 3
led1 = 2
led2 = 4

print("Distance measurement in progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(buzzer,GPIO.OUT)

while True:
        GPIO.output(TRIG, False)
        time.sleep(1)
        GPIO.output(TRIG, True)
        time.sleep(0.01)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
                pulse_start=time.time()

        while GPIO.input(ECHO) == 1:
                pulse_end=time.time()

        pulse_duration=pulse_end-pulse_start
        distance = pulse_duration*11150
        distance = round(distance,2)

        if distance > 15:
                GPIO.output(led1, GPIO.LOW)
                GPIO.output(led2, GPIO.LOW)
                GPIO.output(buzzer, GPIO.LOW)
                print("BUZZER OFF/LED OFF")
        elif distance <= 15 and distance > 10:
                GPIO.output(led1, GPIO.HIGH)
                GPIO.output(led2, GPIO.LOW)
                GPIO.output(buzzer, GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(buzzer, GPIO.LOW)
                print("Buzzer ON (Short beep) / YELLOW LED ON")
        else:
                GPIO.output(led1, GPIO.LOW)
                GPIO.output(led2, GPIO.HIGH)
                GPIO.output(buzzer, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(buzzer, GPIO.LOW)
                print("Buzzer ON (Long beep)/ RED LED ON")
