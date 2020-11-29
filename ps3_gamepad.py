from evdev import InputDevice, categorize, ecodes

from joyapi import JoyApi
import glob
import pprint
pp= pprint.PrettyPrinter(indent=4)
#gamepads = glob.glob("/dev/input/by-id/*gamepad-event*")
gamepads = glob.glob("/dev/input/by-id/usb-ShanWan_PC_PS3_Android-event-joystick")
if len(gamepads)<1:
    raise "No gamepad found"
gamepad_dev = gamepads[0]
print("Using " + gamepad_dev)

api = JoyApi()

#cree un objet gamepad | creates object gamepad
gamepad = InputDevice(gamepad_dev)

#affiche la liste des device connectes | prints out device info at start
print(gamepad)

#affiche les codes interceptes |  display codes
for event in gamepad.read_loop():
    #print("======")
    #print(event)
    #print("======")
    #Boutons | buttons 
    if event.type == ecodes.EV_KEY:
        #print(event)
        if event.value == 1:
            if event.code == 304:
                #print("X")
                api.hold_x()
            if event.code == 305:
                #print("A")
                api.hold_a()
            if event.code == 306:
                #print("B")
                api.hold_b()
            if event.code == 307:
                #print("Y")
                api.hold_y()
            if event.code == 308:
                #print("L")
                api.hold_l()
            if event.code == 309:
                #print("R")
                api.hold_r()
            if event.code == 310:
                #print("ZL")
                api.hold_zl()
            if event.code == 311:
                #print("ZR")
                api.hold_zr()
            if event.code == 312:
                api.press_minus()
            if event.code == 313:
                api.press_plus()
        elif event.value == 0:
            if event.code == 304:
                #print("X")
                api.release_x()
            if event.code == 305:
                #print("A")
                api.release_a()
            if event.code == 306:
                #print("B")
                api.release_b()
            if event.code == 307:
                #print("Y")
                api.release_y()
            if event.code == 308:
                #print("L")
                api.release_l()
            if event.code == 309:
                #print("R")
                api.release_r()
            if event.code == 310:
                #print("ZL")
                api.release_zl()
            if event.code == 311:
                #print("ZR")
                api.release_zr()
            if event.code == 312:
                print("-")
            if event.code == 313:
                print("+")
    elif event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        #pp.pprint(absevent.event)
        #print(absevent)
        value = 16 * absevent.event.value
        if absevent.event.code == ecodes.ABS_HAT0X:
            if absevent.event.value<0:
                print("left down")
                api.press_left()
            elif absevent.event.value>0:
                print("right down")
                api.press_right()
            else:
                print("left and right up")
        elif absevent.event.code == ecodes.ABS_HAT0Y:
            if absevent.event.value<0:
                print("up down")
                api.press_up()
            elif absevent.event.value>0:
                print("down down")
                api.press_down()
            else:
                print("up and down up")
        elif absevent.event.code == ecodes.ABS_X:
            #print("Left X-Axis: "+str(value))
            api.lstick_horiz(value)
        elif absevent.event.code == ecodes.ABS_Y:
            #print("Left Y-Axis: "+str(value))
            api.lstick_vert(4096-value)
        elif absevent.event.code == ecodes.ABS_Z:
            #print("Right X-Axis: "+str(value))
            api.rstick_horiz(value)
        elif absevent.event.code == ecodes.ABS_RZ:
            #print("Right Y-Axis: "+str(value))
            api.rstick_vert(4096-value)

