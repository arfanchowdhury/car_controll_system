#import the USB and Time librarys into Python
import usb.core, usb.util, time, sys
import logging
log = logging.getLogger('RemoTV.hardware.owi_arm')


# led pesistence variable
led = 0
RoboArm = 0

def setup(robot_config):

    #Allocate the name 'RoboArm' to the USB device
    global RoboArm
    RoboArm = usb.core.find(idVendor=0x1267, idProduct=0x000)
 
    #Check if the arm is detected and warn if not
    if RoboArm is None:
        log.critical("USB Arm not found")
        sys.exit()
     

def CtrlTransfer(a, b, c, d, e, f):
    global led
    error = 0
    while True :
        try:
            e[2] = led
            RoboArm.ctrl_transfer(a, b, c, d, e, f)
            break
        except:
            error += 1
            log.error("USB timeout!")
            time.sleep(0.1)
            if error == 5:
               sys.exit()
            pass
 
#Define a procedure to execute each movement
def MoveArm(Duration, ArmCmd):
    #Start the movement
#    RoboArm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,3)
    CtrlTransfer(0x40,6,0x100,0,ArmCmd,3)
    #Stop the movement after waiting a specified duration
    time.sleep(Duration)
    ArmCmd=[0,0,0]
#    RoboArm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,3)
    CtrlTransfer(0x40,6,0x100,0,ArmCmd,3)

def move(args):
    global led
    command = args['button']['command']
    
    if command == 'l':
        MoveArm(0.15, [0,2,0]) # Rotate counter-clockwise
    if command == 'r':
        MoveArm(0.15, [0,1,0]) # Rotate clockwise
    if command == 'b':
        MoveArm(0.15, [128,0,0]) # Rotate Shoulder down
    if command == 'f':
        MoveArm(0.15, [64,0,0]) # Rotate Shoulder up
    if command == 'u':
        MoveArm(0.15, [16,0,0]) # Rotate Elbow up
    if command == 'd':
        MoveArm(0.15, [32,0,0]) # Rotate Elbow down
    if command == 'w':
        MoveArm(0.15, [4,0,0]) # Rotate Wrist Up
    if command == 's':
        MoveArm(0.15, [8,0,0]) # Rotate Wrist Down
    if command == 'c':
        MoveArm(0.15, [2,0,0]) # Open Gripper
    if command == 'v':
        MoveArm(0.15, [1,0,0]) # Close Gripper
    if command == '1':
        led = 1;
        MoveArm(0.15, [0,0,1]) # LED On
    if command == '0':
        led = 0;
        MoveArm(0.15, [0,0,0]) # LED Off

