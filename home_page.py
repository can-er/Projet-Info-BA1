# -*- coding: utf-8 -*-
"""
Created on Fri May 17 23:16:52 2019

@author: User
"""



class Home_Page(object):
    """
    Generate a root who enables to access tho the floor's choice.
    The methods and the attributes attached are used to create widgets.

    """

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Home Page")

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
        self.extra_window_button = tkinter.Button(self.frame, text='Management sytem', command=self.extra_window)
        self.extra_window_button.grid(row=6, column=4)

        self.credits_button = tkinter.Button(self.frame, text="Credits", command=self.extra_window_2)
        self.credits_button.grid(row=7, column=4)

        self.quit_button = tkinter.Button(self.frame, text="QUIT", command=self.root.destroy)
        self.quit_button.grid(row=8, column=4)

        self.label = tkinter.Label(self.frame, text="ISAT All rights reserved ©")
        self.label.grid(row=10, column=4, rowspan=10)

    def extra_window(self):
        """
        Creating of a new manager instance.
        """
        management_system = Management_System()

    def extra_window_2(self):
        extra_window = tkinter.Toplevel(self.root)
        extra_window.title("Credits")

        msg = tkinter.Message(extra_window, text=" Framed by: CORDIER Jean-François \n Authors: HEMELERS Emile, IDRISSI Sami, KORKUT Caner, ZEUKENG Ronald")

        msg.pack()

        button = tkinter.Button(extra_window, text="QUIT", command=extra_window.destroy)
        button.pack()


if __name__ == '__main__':


    test = Home_Page()
    
