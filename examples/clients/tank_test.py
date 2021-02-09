import webiopi
import time
import wiringpi as GPIO

SERVO_PAN = 26

# SERVO_PAN  (Left)90 ... 0 ... -90(Right)
SERVO_PAN_TRIM = 12 # degree
 
SERVO_PAN_LEFT_LIMIT = 60 # degree
SERVO_PAN_RIGHT_LIMIT = -60 # degree
 
##### SERVO SPECIFICATION #####
SERVO_ANGLE_MIN = -90 # degree
SERVO_ANGLE_MAX =  90 # degree
SERVO_PULSE_MIN = 0.75 # ms
SERVO_PULSE_MAX = 2.4 # ms
SERVO_CYCLE = 50 # ms
###############################
 
#### WIRINGPI SPECIFICATION ####
PWM_WRITE_MIN = 0
PWM_WRITE_MAX = 1024
################################
 
SERVO_DUTY_MIN = SERVO_PULSE_MIN/SERVO_CYCLE
SERVO_DUTY_MAX = SERVO_PULSE_MAX/SERVO_CYCLE
 
SERVO_PAN_DUTY_MIN = (SERVO_DUTY_MAX - SERVO_DUTY_MIN) / (SERVO_ANGLE_MAX - SERVO_ANGLE_MIN) * ((SERVO_PAN_LEFT_LIMIT +SERVO_PAN_TRIM) - SERVO_ANGLE_MIN) + SERVO_DUTY_MIN
SERVO_PAN_DUTY_MAX = (SERVO_DUTY_MAX - SERVO_DUTY_MIN) / (SERVO_ANGLE_MAX - SERVO_ANGLE_MIN) * ((SERVO_PAN_RIGHT_LIMIT+SERVO_PAN_TRIM) - SERVO_ANGLE_MIN) + SERVO_DUTY_MIN

SERVO_PAN_PWM_WRITE_MIN = PWM_WRITE_MAX * SERVO_PAN_DUTY_MIN
SERVO_PAN_PWM_WRITE_MAX = PWM_WRITE_MAX * SERVO_PAN_DUTY_MAX

def getServoPanPWMvalue(val):
    # This function returns 0 ... 1024
    pwm_value = int((SERVO_PAN_PWM_WRITE_MAX - SERVO_PAN_PWM_WRITE_MIN) * val + SERVO_PAN_PWM_WRITE_MIN)
    return pwm_value
 
webiopi.setDebug()

def setup():
    webiopi.debug("Script with macros - Setup")
    GPIO.wiringPiSetupGpio()
    GPIO.pinMode(SERVO_PAN,GPIO.OUTPUT)
    GPIO.softPwmCreate(SERVO_PAN,0,50)

def loop():
    webiopi.sleep(5)

def destroy():
    webiopi.debug("Script with macros - Destroy")

@webiopi.macro
def setHwPWMforPan(duty):
    #GPIO.softPwmWrite(SERVO_PAN, getServoPanPWMvalue(float(duty)))