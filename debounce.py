import RPi.GPIO as GPIO

def main():   
    gpio_setup(4, 10)
    gpio_setup(5, 11)
    gpio_setup(6, 12)
    gpio_setup(7, 13)
    gpio_setup(8, 14)
    gpio_setup(9, 15)
    
    callback_setup(4, button_one_callback)
    callback_setup(5, button_two_callback)
    callback_setup(6, button_three_callback)
    callback_setup(7, button_four_callback)
    callback_setup(8, button_five_callback)
    callback_setup(9, button_six_callback)
    # Add gpio_setup and callback_setup for other buttons
    # still need to connect other outputs physically on the Raspberry Pi


def gpio_setup(gpio_input, gpio_output):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpio_input, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(gpio_output, GPIO.OUT, initial=GPIO.LOW)
    GPIO.add_event_detect(gpio_input, GPIO.RISING)
        
def callback_setup(gpio_input, button_callback):
    GPIO.add_event_callback(gpio_input, button_callback)

def button_one_callback(self):
    print "Touch button 1"
    GPIO.output(10, GPIO.input(4))

def button_two_callback(self):
    print "Touch button 2"
    GPIO.output(11, GPIO.input(5))

def button_three_callback(self):
    print "Touch button 3"
    GPIO.output(12, GPIO.input(6))

def button_four_callback(self):
    print "Touch button 4"
    GPIO.output(13, GPIO.input(7))

def button_five_callback(self):
    print "Touch button 5"
    GPIO.output(14, GPIO.input(8))

def button_six_callback(self):
    print "Touch button 6"
    GPIO.output(15, GPIO.input(9))
        
if __name__ == '__main__':
    main()
