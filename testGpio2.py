import RPi.GPIO as GPIO

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(4, GPIO.RISING)

    def my_callback(self):
        print "Touch"

    GPIO.add_event_callback(4, my_callback)

if __name__ == '__main__': 
    main()
