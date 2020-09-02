import tkinter as tk
from joyapi import JoyApi

class Application(tk.Frame):
    ox = None
    oy = None
    api = JoyApi()

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.minsize(width=1920, height=1080)
        self.master.config()

        self.master.bind('<KeyPress>', self.key_press)
        self.master.bind('<KeyRelease>', self.key_release)
        self.master.bind('<Button-1>', self.left_button)
        self.master.bind('<Button-2>', self.right_button)
        self.master.bind('<B1-Motion>', self.left_button_with_motion)
        self.master.bind('<B2-Motion>', self.right_button_with_motion)

        self.main_frame = tk.Frame()
        self.main_frame.focus_set()
        self.main_frame.pack(fill='both', expand=True)
        self.pack()

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
        elif sym == 'a' or sym == 'A':
            Application.api.lstick_left()
        elif sym == 'w':
            Application.api.lstick_up()
        elif sym == 's':
            Application.api.lstick_down()
        elif sym == 'd' or sym == 'D':
            Application.api.lstick_right()
        elif sym == 'Left':
            Application.api.rstick_left()
        elif sym == 'Right':
            Application.api.rstick_right()
        elif sym == 'Up':
            Application.api.rstick_up()
        elif sym == 'Down':
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
        elif sym == 'W':
            Application.api.hold_zr()
        elif sym == 'S':
            Application.api.hold_zl()

    @staticmethod
    def key_release(event):
        print (str(event.keysym)+ " key release")
        sym = event.keysym
        char = event.char
        if sym == 'a' or sym == 'A':
            Application.api.lstick_center()
        elif sym == 'w':
            Application.api.lstick_center()
        elif sym == 's':
            Application.api.lstick_center()
        elif sym == 'd' or sym == 'D':
            Application.api.lstick_center()
        elif sym == 'Left':
            Application.api.rstick_center()
        elif sym == 'Right':
            Application.api.rstick_center()
        elif sym == 'Up':
            Application.api.rstick_center()
        elif sym == 'Down':
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
        elif sym == 'W':
            Application.api.release_zr()
        elif sym == 'S':
            Application.api.release_zl()


    @staticmethod
    def right_button_with_motion(event):
        print (str(event)+ " right button motion")
        if Application.ox is not None:
            dx = event.x - Application.ox
            print("DX="+str(dx))
        if Application.oy is not None:
            dy = event.y - Application.oy
            print("DY="+str(dy))
        Application.ox = event.x
        Application.oy = event.y

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
    def right_button(event):
        print (str(event)+ " right button pressed")
        Application.api.press_b()

    @staticmethod
    def left_button(event):
        print (str(event)+ " left button pressed")
        Application.api.press_a()

root = tk.Tk()
app = Application(root)
app.mainloop()
