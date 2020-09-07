from evdev import InputDevice, categorize, ecodes

from joyapi import JoyApi
import glob

gamepads = glob.glob("/dev/input/by-id/*gamepad-event*")
if len(gamepads)<1:
    raise "No gamepad found"
gamepad_dev = gamepads[0]
print("Using " + gamepad_dev)

api = JoyApi()

#cree un objet gamepad | creates object gamepad
gamepad = InputDevice(gamepad_dev)

#affiche la liste des device connectes | prints out device info at start
print(gamepad)

aBtn = 289
bBtn = 290
xBtn = 288
yBtn = 291
lBtn = 292
rBtn = 293
selBtn = 296
staBtn = 297

#affiche les codes interceptes |  display codes
for event in gamepad.read_loop():
    #Boutons | buttons 
    if event.type == ecodes.EV_KEY:
        #print(event)
        if event.value == 1:
            if event.code == xBtn:
                api.hold_x()
            elif event.code == bBtn:
                api.hold_b()
            elif event.code == aBtn:
                api.hold_a()
            elif event.code == yBtn:
                api.hold_y()
            elif event.code == lBtn:
                api.hold_zl()
            elif event.code == rBtn:
                api.hold_zr()
            elif event.code == selBtn:
                api.hold_l()
                print("Select")
            elif event.code == staBtn:
                api.hold_r()
        elif event.value == 0:
          if event.code == xBtn:
              api.release_x()
          elif event.code == bBtn:
              api.release_b()
          elif event.code == aBtn:
              api.release_a()
          elif event.code == yBtn:
              api.release_y()
          elif event.code == lBtn:
              api.release_zl()
          elif event.code == rBtn:
              api.release_zr()
          elif event.code == selBtn:
              api.release_l()
          elif event.code == staBtn:
              api.release_r()


    #Gamepad analogique | Analog gamepad
    elif event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        #print ecodes.bytype[absevent.event.type][absevent.event.code], absevent.event.value
        if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
             if absevent.event.value == 0:
                api.lstick_left()
             elif absevent.event.value == 255:
                api.lstick_right()
             elif absevent.event.value == 127:
                api.lstick_center()
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":
             if absevent.event.value == 0:
                api.lstick_up()
             elif absevent.event.value == 255:
                api.lstick_down()
             elif absevent.event.value == 127:
                api.lstick_center()
