# -*- coding: utf-8 -*-
"""
Created on Fri May 17 23:16:53 2019

@author: User
"""

class Management_System(object):

    """
    Generate a root who enables to view the floor's rooms.
    The methods and the attributes attached are used to create widgets.

    """


    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Home Page / Management System")

        self.h = 500
        self.w = 1.6 * self.h

        self.frame = tkinter.Frame(self.root)
        self.frame.pack()

        self.can = tkinter.Canvas(self.frame, bg="white", width=self.w, height=self.h)
        self.can.grid(row=0, column=0, rowspan=10, columnspan=9)

        self.image = tkinter.PhotoImage(file='bg.gif', master=self.root)

        self.can.create_image((self.h / 3.5 * 2.5, self.w / 3.5), image=self.image)

        self.widgets_generator()

        self.root.mainloop()


    def canvas_generator(self):
        return tkinter.Canvas(self.frame, bg="dark grey", width=self.w, height=self.h)


    def widgets_generator(self):
        self.floor_1_button = tkinter.Button(self.frame, text="Floor 1", command=self.extra_window)
        self.floor_1_button.grid(row=6, column=3)

        self.floor_2_button = tkinter.Button(self.frame, text="Floor 2", command=self.extra_window_2)
        self.floor_2_button.grid(row=7, column=3)

        self.floor_3_button = tkinter.Button(self.frame, text="Floor 3", command=self.extra_window_3)
        self.floor_3_button.grid(row=8, column=3)

        self.floor_4_button = tkinter.Button(self.frame, text="Floor 4", command=self.extra_window_4)
        self.floor_4_button.grid(row=9, column=3)

        self.floor_5_button = tkinter.Button(self.frame, text="Floor 5", command=self.extra_window_5)
        self.floor_5_button.grid(row=6, column=5)

        self.floor_6_button = tkinter.Button(self.frame, text="Floor 6", command=self.extra_window_6)
        self.floor_6_button.grid(row=7, column=5)

        self.floor_7_button = tkinter.Button(self.frame, text="Floor 7", command=self.extra_window_7)
        self.floor_7_button.grid(row=8, column=5)

        self.floor_8_button = tkinter.Button(self.frame, text="Floor 8", command=self.extra_window_8)
        self.floor_8_button.grid(row=9, column=5)

        self.quit_button = tkinter.Button(self.frame, text="QUIT", command=self.root.destroy)
        self.quit_button.grid(row=10, column=2, columnspan=5)

        self.label = tkinter.Label(self.frame, text="ISAT All rights reserved ©")
        self.label.grid(row=11, column=4, rowspan=10)


    def extra_window(self):
        interface = Interface(1)


    def extra_window_2(self):
        interface_2 = Interface(2)


    def extra_window_3(self):
        interface_3 = Interface(3)


    def extra_window_4(self):
        interface_4 = Interface(4)


    def extra_window_5(self):
        interface_5 = Interface(5)


    def extra_window_6(self):
        interface_6 = Interface(6)


    def extra_window_7(self):
        interface_7 = Interface(7)


    def extra_window_8(self):
        interface_8 = Interface(8)


if __name__ == '__main__':



    #Programme pincinpal
    
    test = Management_System()
    
