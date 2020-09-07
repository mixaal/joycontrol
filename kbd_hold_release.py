import tkinter as tk
import threading
import time
from joyapi import JoyApi

class Application(tk.Frame):
    ox = None
    oy = None
    api = JoyApi()
    mouseMotion=False
    mouseMotionTime = time.time()
    JoyConHoriz = 0
    JoyConVert = 0
    SwapLeftRightSticks = True
    Swap_ZRZL_With_UPDOWN = False

    def mouse_motion_monitor(self):
        while True:
            #print("Mouse motion: "+str(Application.mouseMotion))
            #print("Mouse motion time: "+str(Application.mouseMotionTime))
            now = time.time()
            if now - Application.mouseMotionTime > 1 and Application.mouseMotion:
                Application.mouseMotion = False
                print("Mouse motion stopped")
                Application.api.lstick_horiz(2000)
                Application.api.lstick_vert(2000)
            time.sleep(1)


    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.minsize(width=1920, height=1080)
        self.master.config()

        self.master.bind('<KeyPress>', self.key_press)
        self.master.bind('<KeyRelease>', self.key_release)
        self.master.bind('<Button-1>', self.left_button_press)
        self.master.bind('<ButtonRelease-1>', self.left_button_release)
        self.master.bind('<Button-2>', self.right_button_press)
        self.master.bind('<ButtonRelease-2>', self.right_button_release)
#        self.master.bind('<B1-Motion>', self.left_button_with_motion)
#        self.master.bind('<B2-Motion>', self.right_button_with_motion)
#        self.master.bind('<Motion>', self.motion)

        self.main_frame = tk.Frame()
        self.main_frame.focus_set()
        self.main_frame.pack(fill='both', expand=True)
        self.pack()

    @staticmethod
    def swap_zr_zl_with_up_down():
        if Application.Swap_ZRZL_With_UPDOWN:
            Application.Swap_ZRZL_With_UPDOWN = False
        else:
            Application.Swap_ZRZL_With_UPDOWN = True

    @staticmethod
    def handle_left_stick():
        if Application.JoyConHoriz < 0:
            Application.api.lstick_horiz(0)
        if Application.JoyConHoriz > 0:
            Application.api.lstick_horiz(4000)
        if Application.JoyConHoriz == 0:
            Application.api.lstick_horiz(2000)
        if Application.JoyConVert < 0:
            Application.api.lstick_vert(0)
        if Application.JoyConVert > 0:
            Application.api.lstick_vert(4000)
        if Application.JoyConVert == 0:
            Application.api.lstick_vert(2000)

    @staticmethod
    def is_stick_left(whichone, sym):
        if whichone == 'r' or whichone == 'Right' :
            if sym == 'Left':
                return True
            else:
                return False
        else:
            if sym == 'a' or sym == 'A':
                return True
            else:
                return False

    @staticmethod
    def is_stick_right(whichone, sym):
        if whichone == 'r' or whichone == 'Right' :
            if sym == 'Right':
                return True
            else:
                return False
        else:
            if sym == 'd' or sym == 'D':
                return True
            else:
                return False

    @staticmethod
    def is_stick_up(whichone, sym):
        if whichone == 'r' or whichone == 'Right' :
            if sym == 'Up' and not Application.Swap_ZRZL_With_UPDOWN:
                return True
            else:
                return False
        else:
            if sym == 'w':
                return True
            else:
                return False

    @staticmethod
    def is_stick_down(whichone, sym):
        if whichone == 'r' or whichone == 'Right' :
            if sym == 'Down' and not Application.Swap_ZRZL_With_UPDOWN:
                return True
            else:
                return False
        else:
            if sym == 's':
                return True
            else:
                return False

    @staticmethod
    def is_lstick_left(sym):
        if Application.SwapLeftRightSticks:
            return Application.is_stick_left('r', sym)
        else:
            return Application.is_stick_left('l', sym)

    @staticmethod
    def is_lstick_right(sym):
        if Application.SwapLeftRightSticks:
            return Application.is_stick_right('r', sym)
        else:
            return Application.is_stick_right('l', sym)

    @staticmethod
    def is_lstick_up(sym):
        if Application.SwapLeftRightSticks:
            return Application.is_stick_up('r', sym)
        else:
            return Application.is_stick_up('l', sym)

    @staticmethod
    def is_lstick_down(sym):
        if Application.SwapLeftRightSticks:
            return Application.is_stick_down('r', sym)
        else:
            return Application.is_stick_down('l', sym)

    @staticmethod
    def is_rstick_left(sym):
        if Application.SwapLeftRightSticks:
            return Application.is_stick_left('l', sym)
        else:
            return Application.is_stick_left('r', sym)

    @staticmethod
    def is_rstick_right(sym):
        if Application.SwapLeftRightSticks:
            return Application.is_stick_right('l', sym)
        else:
            return Application.is_stick_right('r', sym)

    @staticmethod
    def is_rstick_up(sym):
        if Application.SwapLeftRightSticks:
            return Application.is_stick_up('l', sym)
        else:
            return Application.is_stick_up('r', sym)

    @staticmethod
    def is_rstick_down(sym):
        if Application.SwapLeftRightSticks:
            return Application.is_stick_down('l', sym)
        else:
            return Application.is_stick_down('r', sym)

    @staticmethod
    def is_zr(sym):
        if Application.SwapLeftRightSticks and Application.Swap_ZRZL_With_UPDOWN:
            return sym == 'Up'
        else:
            return sym == 'W'

    @staticmethod
    def is_zl(sym):
        if Application.SwapLeftRightSticks and Application.Swap_ZRZL_With_UPDOWN:
            return sym == 'Down'
        else:
            return sym == 'S'


    
    @staticmethod
    def key_press(event):
        print (str(event.keysym)+ " key press")
        sym = event.keysym
        char = event.char
        if sym == 'Home':
            Application.api.press_home()
        elif sym == 'minus' or sym == 'KP_Subtract':
            Application.api.press_minus()
        elif sym == 'plus' or sym == 'KP_Add':
            Application.api.press_plus()
        elif Application.is_lstick_left(sym):
            Application.JoyConHoriz = -1
        elif Application.is_lstick_up(sym):
            Application.JoyConVert = 1
        elif Application.is_lstick_down(sym):
            Application.JoyConVert = -1
        elif Application.is_lstick_right(sym):
            Application.JoyConHoriz = 1
        elif Application.is_rstick_left(sym):
            Application.api.rstick_left()
        elif Application.is_rstick_right(sym):
            Application.api.rstick_right()
        elif Application.is_rstick_up(sym):
            Application.api.rstick_up()
        elif Application.is_rstick_down(sym):
            Application.api.rstick_down()
        elif sym == 'x' or sym == 'X':
            Application.api.hold_x()
        elif sym == 'b' or sym == 'B':
            Application.api.hold_b()
        elif sym == 'Return':
            Application.api.hold_a()
        elif sym == 'space':
            Application.api.hold_y()
        elif sym == '8' or sym == 'KP_8':
            Application.api.hold_up()
        elif sym == '2' or sym == 'KP_2':
            Application.api.hold_down()
        elif sym == '4' or sym == 'KP_4':
            Application.api.hold_left()
        elif sym == '6' or sym == 'KP_6':
            Application.api.hold_right()
        elif Application.is_zr(sym):
            Application.api.hold_zr()
        elif Application.is_zl(sym):
            Application.api.hold_zl()
        elif sym == 'KP_Enter':
            Application.swap_zr_zl_with_up_down()
            #print(Application.Swap_ZRZL_With_UPDOWN)

        Application.handle_left_stick()

    @staticmethod
    def key_release(event):
        print (str(event.keysym)+ " key release")
        sym = event.keysym
        char = event.char
        if Application.is_lstick_left(sym):
            Application.JoyConHoriz = 0
        elif Application.is_lstick_up(sym):
            Application.JoyConVert = 0
        elif Application.is_lstick_down(sym):
            Application.JoyConVert = 0
        elif Application.is_lstick_right(sym):
            Application.JoyConHoriz = 0
        elif Application.is_rstick_left(sym):
            Application.api.rstick_center()
        elif Application.is_rstick_right(sym):
            Application.api.rstick_center()
        elif Application.is_rstick_up(sym):
            Application.api.rstick_center()
        elif Application.is_rstick_down(sym):
            Application.api.rstick_center()
        elif sym == 'x' or sym == 'X':
            Application.api.release_x()
        elif sym == 'b' or sym == 'B':
            Application.api.release_b()
        elif sym == 'Return':
            Application.api.release_a()
        elif sym == 'space':
            Application.api.release_y()
        elif sym == '8' or sym == 'KP_8' or sym == 'KP_Up':
            Application.api.release_up()
        elif sym == '2' or sym == 'KP_2' or sym == 'KP_Down':
            Application.api.release_down()
        elif sym == '4' or sym == 'KP_4' or sym == 'KP_Left':
            Application.api.release_left()
        elif sym == '6' or sym == 'KP_6' or sym == 'KP_Right':
            Application.api.release_right()
        elif Application.is_zr(sym):
            Application.api.release_zr()
        elif Application.is_zl(sym):
            Application.api.release_zl()
        Application.handle_left_stick()


    @staticmethod
    def right_button_with_motion(event):
        print (str(event)+ " right button motion")

    @staticmethod
    def left_button_with_motion(event):
        print (str(event)+ " left button motion")
        if Application.ox is not None:
            dx = event.x - Application.ox
            print("DX="+str(dx))
        if Application.oy is not None:
            dy = event.y - Application.oy
            print("DY="+str(dy))
        Application.ox = event.x
        Application.oy = event.y

    @staticmethod
    def right_button_press(event):
        print (str(event)+ " right button pressed")
        Application.api.hold_b()

    @staticmethod
    def right_button_release(event):
        print (str(event)+ " right button released")
        Application.api.release_b()

    @staticmethod
    def left_button_press(event):
        print (str(event)+ " left button pressed")
        Application.api.hold_a()

    @staticmethod
    def left_button_release(event):
        print (str(event)+ " left button released")
        Application.api.release_a()


    @staticmethod
    def motion(event):
        Application.mouseMotion = True
        Application.mouseMotionTime = time.time()
        x, y = event.x, event.y
        dx = 0
        dy = 0
        if Application.ox is not None:
            dx = x - Application.ox
            print("DX="+str(dx))
        if Application.oy is not None:
            dy = y - Application.oy
            print("DY="+str(dy))
        if dx>5:
          Application.api.lstick_horiz(4000)
        if dx<-5:
          Application.api.lstick_horiz(0)
        if dx>=-5 and dx<5:
          Application.api.lstick_horiz(2000)
        if dy>5:
          Application.api.lstick_vert(0)
        if dy<-5:
          Application.api.lstick_vert(4000)
        if dy>=-5 and dy<5:
          Application.api.lstick_vert(2000)
        Application.ox = x
        Application.oy = y
        print('Mouse at {}, {}'.format(x, y))




root = tk.Tk()
app = Application(root)
#mouse motion not working properly so far
#th = threading.Thread(target=app.mouse_motion_monitor)
#th.start()
app.mainloop()
