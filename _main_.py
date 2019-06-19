# -*- coding: utf-8 -*-
"""
Created on Fri May 17 23:16:52 2019

@author: User
"""

import tkinter
import time

import file_manager
import home_page
import management_system



class Block(object):
    
    """
    Parent class. 
    Used to create common methods shared by the room's objects .
    
    """

    def __init__(self, can, floor, tag = " "):

        self.floor = floor
        self.can = can
        self.tag = tag
        self.state = 0
        self.consumption = 0
        self.was_overlapped = False
        self.id = None
        self.f_m = File_Manager(self.floor)

        
    def agent_interact(self, consumption):
        
        """    
        Method used to check above the block the presence of an agent. 
    
        """
        
        co_block = self.can.bbox(self.id)
        overlapped = self.can.find_overlapping(*co_block)
        
        if 41 in overlapped:
            self.state = 1
            self.consumption = consumption
            self.can.itemconfig(self.id, fill = "red")
            
            if not self.was_overlapped:
                self.x = time.perf_counter()
            self.was_overlapped = True
        else:    
            self.state = 0
            self.consumption = 0
            self.can.itemconfig(self.id, fill = "yellow")
            self.y = time.perf_counter()
            
            if self.was_overlapped:
                stayed_time = int(abs(self.y-self.x))
                self.was_overlapped = False
                self.f_m.save_time(stayed_time)
            

class Bed(Block):
        
    """    
    Generate an object who represents a room's bed. 
    
    """

    def __init__(self, can, co, tag, floor):
        Block.__init__(self, can, tag, floor)
        self.id = self.can.create_rectangle(*co, tag = tag, fill = "yellow")
        
        
        
class Door(Block):

    """    
    Generate an object who represents a room's door. 
    
    """

    def __init__(self, can, co, tag, floor):
        Block.__init__(self, can, tag, floor)
        self.can = can
        self.id = self.can.create_line(*co,fill= "yellow", tag = tag, dash = (1,4), width= 9)
        return Door.agent_interact(self,self.consumption)
        
class Switch(Block):

    """    
    Generate an object who represents a room's switch. 
    
    """

    def __init__(self, can, co, tag, floor):
        Block.__init__(self, can, tag, floor)
        self.can = can
        self.id = self.can.create_oval(*co, tag = tag,fill= "yellow")
        

class Window(Block):
        
    """    
    Generate an object who represents a room's window. 
    
    """

    def __init__(self, can, co, tag, floor):
        Block.__init__(self, can, tag, floor)
        self.can = can
        self.id = self.can.create_line(*co, tag = tag, dash = (1,4), fill ="yellow")

class Tv(Block):
        
    """    
    Generate an object who represents a room's TV. 
    
    """

    def __init__(self, can, co, tag, floor):
        Block.__init__(self, can, tag, floor)
        self.can = can
        self.id = self.can.create_rectangle(*co, tag = tag, fill = "yellow")
        

class Console(Block):

    """    
    Generate an object who represents a room's bed game console. 
    
    """

    def __init__(self, can, co, tag, floor):
        Block.__init__(self, can, tag, floor)
        self.can = can
        self.id = self.can.create_rectangle(*co, tag = tag, fill = "yellow")


class Room(Block):
    
    """
    Generate objects who represent the rooms. 
    The attributes attached are used to create room's objects. 
    
    """

    def __init__(self, can, co, tag, w, h, floor):
        self.can = can
        self.w, self.h = w, h

        co_bed = [co[0] + self.w*2/6,co[1] + 6 ,co[0] + self.w*2/5.1,self.h/4]
        co_door = [co[0] + self.w/3.5,co[1] + self.h/2,co[0] + self.w/5,co[1] + self.h/2]
        co_switch = [co[0] + self.w*5/300 , self.h/2.1  ,co[0] + self.w*5/300 + 30, self.h/2.1 + 30]
        co_window = [co[0] + self.w/3.5,co[1],co[0] + self.w/4.1,co[1]]
        co_tv = [co[0] + self.w*2/6, self.h/3.77,co[0] + self.w*2/5.1,self.h/3]
        co_console = [co[0] + self.w*2/6 + 15, self.h/3.77 + 15 ,co[0] + self.w*2/5.1 - 15, self.h/3 - 15]

        line_1 = self.can.create_line(co[0],co[1],co[0] + self.w*2/5,co[1], tag = tag +" mur")
        line_2 = self.can.create_line(co[0],co[1],co[0], co[1] + self.h/2, tag = tag +" mur")
        line_3 = self.can.create_line(co[0] + self.w*2/5,co[1],co[0] + self.w*2/5,co[1] + self.h/2, tag = tag +" mur")
        line_4 = self.can.create_line(co[0], co[1] + self.h/2,co[0] + self.w/5,co[1] + self.h/2, tag = tag +" mur")
        line_5 = self.can.create_line(co[0] + self.w*2/5,co[1] + self.h/2,co[0] + self.w/3.5,co[1] + self.h/2, tag = tag +" mur")
        self.walls = [line_1,line_2,line_3,line_4,line_5]

        self.door = Door(self.can, co_door, "floor_"+str(floor)+"_" + tag +"_porte.txt", floor)
        self.bed = Bed(self.can, co_bed,  "floor_"+str(floor)+"_" + tag +"_lit.txt", floor)
        self.tv = Tv(self.can, co_tv,  "floor_"+str(floor)+"_" + tag +"_tv.txt", floor)
        self.console = Console(self.can, co_console,  "floor_"+str(floor)+"_" + tag + "_console.txt",  floor)
        self.window = Window(self.can, co_window,  "floor_"+str(floor)+"_" + tag + "_fenêtre.txt",  floor)
        self.switch = Switch(self.can, co_switch,  "floor_"+str(floor)+"_" + tag + "_interrupteur.txt", floor)

        self.objects = [self.door, self.bed, self.tv, self.console, self.window, self.switch]

        



class Agent(object):
    
    """    
    Generate objects who represent a dynamic agent. 
    The methods attached are used to move and "interact" with room's objects. 
    
    """
    
    def __init__(self,can,co,tag,inter):

        self.can = can

        self.agent_dpx, self.agent_dpy = 5, 5
        

        self.id  = self.can.create_oval(*co, tag = tag, fill = "black")
        self.interface = inter
        
            
    def agent_move_up(self):
    
        coa = self.can.bbox(self.id)
        dpl = True
    
        for m in self.can.find_all():
            if "mur" in self.can.gettags(m) :
                com = self.can.bbox(m)
                if (com[0]<=coa[0]<=com[2] or com[0]<=coa[2]<=com[2]) and com[1] <= coa[1] <= com[1] + self.agent_dpy:
                    dpl = False
                    break
        if dpl:
            self.can.move(self.id, 0 , - self.agent_dpy)


    
    def agent_move_down(self):
        
        coa = self.can.bbox(self.id)
        dpl = True
        
        for m in self.can.find_all():
            if "mur" in self.can.gettags(m) :
                com = self.can.bbox(m)
                if (com[0]<=coa[0]<=com[2] or com[0]<=coa[2]<=com[2]) and com[3] <= coa[3] <= com[3] +  self.agent_dpy:
                    dpl = False
                    break
        if dpl:
            self.can.move(self.id, 0 , self.agent_dpy)
      
        
    def agent_move_left(self):
    
        coa = self.can.bbox(self.id)
        dpl = True
    
        for m in self.can.find_all():
            if "mur" in self.can.gettags(m) :
                com = self.can.bbox(m)
                if (com[1]<=coa[1]<=com[3] or com[1]<=coa[3]<=com[3]) and com[0] <= coa[0] <= com[0] + self.agent_dpx :
                    dpl = False
                    break
        if dpl:
            self.can.move(self.id, -self.agent_dpx , 0)
      
    
    def agent_move_right(self):
        
        coa = self.can.bbox(self.id)
        dpl = True
        
        for m in self.can.find_all():
            if "mur" in self.can.gettags(m) :
                com = self.can.bbox(m)
                if (com[1]<=coa[1]<=com[3] or com[1]<=coa[3]<=com[3]) and com[2] <= coa[2] <= com[2] + self.agent_dpy:
                    dpl = False
                    break
        if dpl:
            self.can.move(self.id, self.agent_dpx , 0)
        

    
    def agent_move(self, direction):
    
        if direction == "Up":
            self.agent_move_up()
    
        elif direction == "Down":
            self.agent_move_down()
            
        elif direction == 'Left':
            self.agent_move_left()
            
        elif direction == 'Right':
            self.agent_move_right()
     
        
    
    
    def block_interact(self):
        
        """    
        Method used to check below the agent the presence of a block. 
    
        """

        overlapped = self.can.find_overlapping(*self.can.bbox(self.id))
        if self.interface.agent.id in overlapped:
            
            
            for elem in self.interface.room1.objects + self.interface.room2.objects:
                elem.agent_interact(consumption = self.interface.consumption)
                

        
class Interface(object):
    
    """
    Generate a root and objects who represent the geometry of a floor. 
    The methods and the attributes attached are used to create widgets. 
    The canvas is bounded with key events.
    
    """
    
    def __init__(self, floor, consumption = 25):
        
        self.root = tkinter.Tk()
        self.root.title("Floor View")
                
        self.h = 500 
        self.w = 1.6 * self.h 
    
        self.floor = floor

        self.frame = tkinter.Frame(self.root)
        self.frame.pack()
        self.consumption = consumption
                
        self.widgets_generator()
        self.can = self.canvas_generator()
        self.can.grid(row = 0, column = 0, columnspan = 15, rowspan = 10)
                
        self.pos_x_room_1, self.pos_y_room_1 = 0.10 * self.w, 0.04 * self.h 
        self.pos_x_room_2, self.pos_y_room_2 = 0.5 * self.w, 0.04 * self.h
            
        
        self.room1 = Room(self.can,(self.pos_x_room_1, self.pos_y_room_1), 'chambre1', self.w, self.h, self.floor)
        self.room2 = Room(self.can,(self.pos_x_room_2, self.pos_y_room_2), 'chambre2', self.w, self.h,  self.floor)
        
        self.rooms = [self.room1, self.room2]
                
        self.pos_x_steps_1, self.pos_y_steps_1 = 0.02 * self.w, self.h * 0.04
        self.pos_x_steps_2, self.pos_y_steps_2 = 0.92 * self.w, self.h * 0.04
                
        self.steps_1 = self.steps_generator(self.pos_x_steps_1, self.pos_y_steps_1)
        self.steps_2 = self.steps_generator(self.pos_x_steps_2, self.pos_y_steps_2)
                
        self.agent = Agent(self.can, [self.h + 10, self.pos_y_room_2 + 10, self.h + 20, self.pos_y_room_2 + 20]
, "Agent1",self)
                
        
        
        self.root.bind('<Key>', self.keyboard)
        self.root.mainloop()
            
        
    def canvas_generator(self):
        return tkinter.Canvas(self.frame, bg = "dark grey",  width = self.w, height = self.h)
        
    
    def widgets_generator(self):
        
  
        
        self.label = tkinter.Label(self.frame, text = "Bienvenue à mon projet")
        self.label.grid(row = 12, column = 3)
        
        
      

        self.extra_window_button = tkinter.Button(self.frame, text='Données', command = self.extra_window) 
        self.extra_window_button.grid(row = 0, column = 16)


        self.quit_button = tkinter.Button(self.frame, text = "Quitter (et sauvegarder)", command = self.quitter)
        self.quit_button.grid(row = 1, column = 16)
    

    def step_generator(self, coord_x, coord_y):
        bed = self.can.create_rectangle(coord_x + self.w*2/6,coord_y,coord_x + self.w*2/5,self.h/3)

        

    def steps_generator(self, coord_x, coord_y):
        for i in range(8):
            self.can.create_line(coord_x, i * 0.07 * self.h, coord_x +  self.w*0.06, self.h * 0.07 * i ,dash = (4,4))
        return self.can.create_rectangle(coord_x, coord_y, coord_x +  self.w*0.06, coord_y + self.h * 0.5)     

    
    def keyboard(self, event):
        
        authorized_moves = ["Up", "Down", "Left", "Right"]
        quit_button = ["Escape","q"]
        
        if event.keysym in authorized_moves:
                    
            self.agent.agent_move(event.keysym)
            self.agent.block_interact()
    
        
        elif event.keysym in quit_button:
            
            self.quitter()
        
    
    def quitter(self):
        self.root.destroy()
        
    def extra_window(self):
        extra_window = tkinter.Toplevel(self.root)

       
    


if __name__ == '__main__':



    #Programme pincinpal
    
    home_page = Home_Page()
    
