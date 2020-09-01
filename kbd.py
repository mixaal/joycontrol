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

        self.master.bind('<Left>', self.left_key)
        self.master.bind('<Right>', self.right_key)
        self.master.bind('<Up>', self.up_key)
        self.master.bind('<Down>', self.down_key)
        self.master.bind('<Return>', self.enter_key)
        self.master.bind('<space>', self.space_key)
        self.master.bind('<Button-1>', self.left_button)
        self.master.bind('<Button-2>', self.right_button)
        self.master.bind('<B1-Motion>', self.left_button_with_motion)
        self.master.bind('<B2-Motion>', self.right_button_with_motion)
        self.master.bind('x', self.x_character)
        self.master.bind('b', self.b_character)

        self.main_frame = tk.Frame()
        self.main_frame.focus_set()
        self.main_frame.pack(fill='both', expand=True)
        self.pack()

    @staticmethod
    def b_character(event):
        print (str(event)+ " B character")
        Application.api.press_b()

    @staticmethod
    def x_character(event):
        print (str(event)+ " X character")
        Application.api.press_x()

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

    @staticmethod
    def enter_key(event):
        print (str(event)+ " key pressed")
        Application.api.press_a()

    @staticmethod
    def space_key(event):
        print (str(event)+ " key pressed")
        Application.api.press_y()
 
    @staticmethod
    def up_key(event):
        print (str(event)+ " key pressed")
        Application.api.press_up()

    @staticmethod
    def down_key(event):
        print (str(event)+ " key pressed")
        Application.api.press_down()

    @staticmethod
    def left_key(event):
        print (str(event)+ " key pressed")
        Application.api.press_left()

    @staticmethod
    def right_key(event):
        print (str(event) + " key pressed")
        Application.api.press_right()

root = tk.Tk()
app = Application(root)
app.mainloop()
