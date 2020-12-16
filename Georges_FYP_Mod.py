# AC App Template by Hunter Vaners
# ------------------------------
#
# Don't forget to rename assettocorsa\apps\python\Template_Assetto_Corsa_App
#           by assettocorsa\apps\python\[Your_App_Name_Without_Spaces]
#  and
# the file Template_Assetto_Corsa_App.py
#           by Your_App_Name_Without_Spaces.py
#
# ------------------------------

import ac
import acsys
from third_party.sim_info import *




appName = ">George's FYP Mod Test<"
width, height = 800 , 800 # width and height of the app's window

simInfo = SimInfo()

l_lapcount=0
lapcount=0

def acMain(ac_version):#----------------------------- App window Init

    # Don't forget to put anything you'll need to update later as a global variables
    global appWindow # <- you'll need to update your window in other functions.
    global l_lapcount
    global testButton, buttonPress, buttonLabel

    appWindow = ac.newApp(appName)
    ac.setTitle(appWindow, appName)
    ac.setSize(appWindow, width, height)

    ac.addRenderCallback(appWindow, appGL) # -> links this app's window to an OpenGL render function

    testButton = ac.addButton(appWindow,"Add Text Below")
    ac.setSize(testButton,700,300)
    ac.setPosition(testButton,50,200)
    ac.setFontSize(testButton,30)
    ac.addOnClickedListener(testButton,buttonPress)


    l_lapcount = ac.addLabel(appWindow, "Laps: 0")
    ac.setPosition(l_lapcount, 3, 30)

    return appName



def buttonPress(val1,val2):

    global testButton, buttonPress, buttonLabel

    buttonLabel = ac.addLabel(appWindow,"Added by button")
    ac.setPosition(buttonLabel,50,550)
    ac.setFontSize(buttonLabel,30)



# def buttonToggle(value):
#     global testButton, buttonToggle

#     if buttonToggle == 0:
#        ac.settext(testButton,"ON")
#        return 1
#     else:
#        ac.setText(testButton,"OFF")
#        return 0



def appGL(deltaT):#-------------------------------- OpenGL UPDATE
    """
    This is where you redraw your openGL graphics
    if you need to use them .
    """
    pass # -> Delete this line if you do something here !




def acUpdate(deltaT):#-------------------------------- AC UPDATE
    """
    This is where you update your app window ( != OpenGL graphics )
    such as : labels , listener , ect ...
    """
    global l_lapcount, lapcount

    laps = ac.getCarState(0, acsys.CS.LapCount)
    if laps > lapcount:
        lapcount = laps
        ac.setText(l_lapcount, "Laps: {}".format(lapcount))
