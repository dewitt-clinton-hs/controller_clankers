# ----------------------------------------------------------------------------- #
#                                                                               #        
#    Project:        Right Arcade Control                                       #
#    Module:         main.py                                                    #
#    Author:         Camila Rodriguez                                           #
#    Created:        Fri Feb 06 2025                                            #
#                                                                               #                                                                       
# ----------------------------------------------------------------------------- #

# Library imports
from vex import *

class SirClank:
    def __init__(self):
        self.right_front = Motor(Ports.PORT1, True)
        self.right_back = Motor(Ports.PORT8, True)

        self.left_front = Motor(Ports.PORT11, True)
        self.left_back = Motor(Ports.PORT19, True)
       
        self.right_wheels = [self.right_front, self.right_back]
        self.left_wheels = [self.left_front, self.left_back]
       
        self.intake=MotorGroup(Ports.PORT20,Ports.PORT9)

    def drive(self,pos):
        for i in self.right_wheels: i.spin(FORWARD, pos * 2)
        for i in self.left_wheels: i.spin(FORWARD, pos * 2)

    def turn(self,pos):
        for i in self.right_wheels: i.spin(FORWARD, pos * -2)
        for i in self.left_wheels: i.spin(FORWARD, pos * 2)

    def intake_object(self,direction):
       self.intake.spin(direction,200)
       return None

brain=Brain()
controller=Controller()
bot=SirClank()

def autonomous():
    for i in bot.right_wheels: i.spin_for(FORWARD, 2, INCHES)
    for i in bot.left_wheels: i.spin_for(FORWARD, 2, INCHES)


def check_intake():
    if controller.buttonR1.pressing(): bot.intake_object(FORWARD)
    elif controller.buttonL1.pressing(): bot.intake_object(REVERSE)
    else: bot.intake.stop()

def user_control():
    brain.screen.print('DRIVING')

    while True:
        driving = controller.axis1.position() > 15 or controller.axis1.position() < -15
        turning = controller.axis3.position() > 15 or controller.axis3.position() < -15

        check_intake()

        if driving:
            check_intake()

            if turning: bot.turn(controller.axis3.position())
            else: bot.drive(controller.axis1.position())
        elif turning:
            check_intake()

            if driving: bot.drive(controller.axis1.position())
            else: bot.turn(controller.axis3.position())
        else:
            for i in bot.right_wheels: i.stop()
            for i in bot.left_wheels: i.stop()
comp = Competition(user_control, autonomous)
        

           

    


