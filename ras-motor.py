import RPi.GPIO as GPIO
import pigpio
import time


def main():
    pin=24
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin,GPIO.IN,GPIO.PUD_UP)
    GPIO.add_event_detect(pin,GPIO.RISING,bouncetime=1200)
    GPIO.add_event_callback(pin,my_callback)
    try:
        while(True):
            time.sleep(1)
    except KeyboardInterrupt:
        print("break")
        GPIO.cleanup()

def my_callback(channel):
    servo = 18
    servo0 = 27
    servo1 = 17
    pi = pigpio.pi()
    # ピンを出力に設定
    pi.set_mode(servo, pigpio.OUTPUT)
    # 0.15秒間正転 (FS90Rは1msのパルスで正転)
    pi.set_servo_pulsewidth(servo, 1000)
    time.sleep(0.15)
    #5秒間停止#
    pi.set_servo_pulsewidth(servo, 1500)
    time.sleep(5)
    # 0.15秒間逆転 (FS90Rは2msのパルスで逆転)
    pi.set_servo_pulsewidth(servo, 2000)
    time.sleep(0.15)
    # 停止 (FS90Rは1.5msのパルスで停止)
    pi.set_servo_pulsewidth(servo, 1500)
    # ピンを出力に設定
    pi.set_mode(servo0, pigpio.OUTPUT)
    # 120秒間正転 (FS90Rは1msのパルスで正転)
    pi.set_servo_pulsewidth(servo0, 1000)
    time.sleep(120)
    # 停止 (FS90Rは1.5msのパルスで停止)
    pi.set_servo_pulsewidth(servo0, 1500)
    # ピンを出力に設定
    pi.set_mode(servo1, pigpio.OUTPUT)
    # 0.15秒間正転 (FS90Rは1msのパルスで正転)
    pi.set_servo_pulsewidth(servo1, 2000)
    time.sleep(0.15)
    #5秒間停止#
    pi.set_servo_pulsewidth(servo1, 1500)
    time.sleep(5)
    # 0.15秒間逆転 (FS90Rは2msのパルスで逆転)
    pi.set_servo_pulsewidth(servo1, 1000)
    time.sleep(0.15)
    # 停止 (FS90Rは1.5msのパルスで停止)
    pi.set_servo_pulsewidth(servo1, 1500)
    # ピンを出力に設定
    pi.set_mode(servo0, pigpio.OUTPUT)
    #  180秒間正転 (FS90Rは1msのパルスで正転)
    pi.set_servo_pulsewidth(servo0, 1000)
    time.sleep(180)
    # 停止 (FS90Rは1.5msのパルスで停止)
    pi.set_servo_pulsewidth(servo0, 1500)
    # 終了
    pi.stop()

if __name__=="__main__":
    main()

