import RPi.GPIO as GPIO
import time
import extended_command
import logging
log = logging.getLogger('RemoTV.hardware.l298n')

sleeptime=None 
rotatetimes=None

StepPinForward=None
StepPinBackward=None
StepPinLeft=None
StepPinRight=None

def set_rotate_time(command, args):
    global rotatetimes
    if extended_command.is_authed(args['sender']) == 2: # Owner
        if len(command) > 1:
            rotatetimes=float(command[1])
            log.info("rotate time multiplier set to : %f", float(command[1]))

def set_sleep_time(command, args):
    global sleeptime
    if extended_command.is_authed(args['sender']) == 2: # Owner
        if len(command) > 1:
            sleeptime=float(command[1])
            log.info("sleep time set to : %f", float(command[1]))


def setup(robot_config):
    global StepPinForward
    global StepPinBackward
    global StepPinLeft
    global StepPinRight
    global sleeptime
    global rotatetimes
    
    sleeptime = robot_config.getfloat('l298n', 'sleeptime')
    rotatetimes = robot_config.getfloat('l298n', 'rotatetimes')
    
    log.debug("GPIO mode : %s", str(GPIO.getmode()))

    GPIO.setwarnings(False)
    GPIO.cleanup()
    
    if robot_config.getboolean('tts', 'ext_chat'): #ext_chat enabled, add motor commands
        extended_command.add_command('.set_rotate_time', set_rotate_time)
        extended_command.add_command('.set_sleep_time', set_sleep_time)

# TODO passing these as tuples may be unnecessary, it may accept lists as well. 
    StepPinForward = int(robot_config.get('l298n', 'StepPinForward'))
    StepPinBackward = int(robot_config.get('l298n', 'StepPinBackward'))
    StepPinLeft = int(robot_config.get('l298n', 'StepPinLeft'))
    StepPinRight = int(robot_config.get('l298n', 'StepPinRight'))
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(StepPinForward, GPIO.OUT)
    GPIO.setup(StepPinBackward, GPIO.OUT)
    GPIO.setup(StepPinLeft, GPIO.OUT)
    GPIO.setup(StepPinRight, GPIO.OUT)

def move(args):
    direction = args['button']['command']
    if direction == 'f':
        GPIO.output(StepPinForward, GPIO.LOW)
        GPIO.output(StepPinBackward, GPIO.HIGH)
        GPIO.output(StepPinLeft, GPIO.HIGH)
        GPIO.output(StepPinRight, GPIO.LOW)
        time.sleep(sleeptime)
        GPIO.output(StepPinForward, GPIO.LOW)
        GPIO.output(StepPinBackward, GPIO.LOW)
        GPIO.output(StepPinLeft, GPIO.LOW)
        GPIO.output(StepPinRight, GPIO.LOW)
    if direction == 'b':
        GPIO.output(StepPinForward, GPIO.HIGH)
        GPIO.output(StepPinBackward, GPIO.LOW)
        GPIO.output(StepPinLeft, GPIO.LOW)
        GPIO.output(StepPinRight, GPIO.HIGH)
        time.sleep(sleeptime)
        GPIO.output(StepPinForward, GPIO.LOW)
        GPIO.output(StepPinBackward, GPIO.LOW)
        GPIO.output(StepPinLeft, GPIO.LOW)
        GPIO.output(StepPinRight, GPIO.LOW)
    if direction == 'l':
        GPIO.output(StepPinForward, GPIO.HIGH)
        GPIO.output(StepPinBackward, GPIO.LOW)
        GPIO.output(StepPinLeft, GPIO.HIGH)
        GPIO.output(StepPinRight, GPIO.LOW)
        time.sleep(sleeptime)
        GPIO.output(StepPinForward, GPIO.LOW)
        GPIO.output(StepPinBackward, GPIO.LOW)
        GPIO.output(StepPinLeft, GPIO.LOW)
        GPIO.output(StepPinRight, GPIO.LOW)
    if direction == 'r':
        GPIO.output(StepPinForward, GPIO.LOW)
        GPIO.output(StepPinBackward, GPIO.HIGH)
        GPIO.output(StepPinLeft, GPIO.LOW)
        GPIO.output(StepPinRight, GPIO.HIGH)
        time.sleep(sleeptime)
        GPIO.output(StepPinForward, GPIO.LOW)
        GPIO.output(StepPinBackward, GPIO.LOW)
        GPIO.output(StepPinLeft, GPIO.LOW)
        GPIO.output(StepPinRight, GPIO.LOW)
    if direction == 'x':
        GPIO.output(StepPinForward, GPIO.LOW)
        GPIO.output(StepPinBackward, GPIO.LOW)
        GPIO.output(StepPinLeft, GPIO.LOW)
        GPIO.output(StepPinRight, GPIO.LOW)
        
        
        
               
