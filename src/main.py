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

# Brain should be defined by default
brain=Brain()

# Robot configuration code
controller=Controller()
class sirClank:
    def __init__(self):
       self.right_motors=MotorGroup(Ports.PORT1,Ports.PORT8)
       self.left_motors=MotorGroup(Ports.PORT19,Ports.PORT11)#directions are based from the back
       self.intake=Motor(Ports.PORT20,Ports.PORT9)
    def drive(self,pos):
        self.right_motors.spin(FORWARD,pos*2)
        self.left_motors.spin(FORWARD,pos*2)

    def turn(self,pos):
        self.right_motors.spin(FORWARD,pos*-2)
        self.left_motors.spin(FORWARD,pos*-2)

    def intake_object(self,pos):
       self.intake.spin(pos,200)
       return None
    
bot=sirClank()
def autonomous():
    pass

def user_control():
    brain.screen.print('DRIVING')

    while True:
        driving = controller.axis3.position() > 15 or controller.axis3.position() < -15
        turning = controller.axis1.position() > 15 or controller.axis1.position() < -15

        if controller.buttonR1.pressing(): bot.intake_object(FORWARD)
        elif controller.buttonL1.pressing(): bot.intake_object(REVERSE)
        else:
            bot.intake.stop()
        if driving:
            if controller.buttonR1.pressing(): bot.intake_object(FORWARD)
            elif controller.buttonL1.pressing(): bot.intake_object(REVERSE)
            else: bot.intake.stop()
        elif turning:
            # Checks for other button inputs allows for motion on wheels and for other components to move simultaneously
            
            if controller.buttonR1.pressing(): bot.intake_object(FORWARD)
            elif controller.buttonL1.pressing(): bot.intake_object(REVERSE)
            else: bot.intake.stop()
            
            # Check for driving while turning allows for smooth transitions between modes
            if driving: bot.drive(controller.axis3.position())
            else: bot.turn(controller.axis1.position())
        else:
            bot.right_motors.stop()
            bot.left_motors.stop()
comp = Competition(user_control, autonomous)
        

           

    


