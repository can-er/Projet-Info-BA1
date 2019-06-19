# -*- coding: utf-8 -*-
"""
Created on Fri May 17 23:16:54 2019

@author: User
"""

class File_Manager(object):

    """"""

    def __init__(self, fichier):
        self.file = fichier

    def create_file(self):
        try : 
            with open(self.file, "r+") as f:
                if f.read() == "": # if files exists and is empty
                    f.write("0")
        except : 
            with open(self.file, "a") as f : # if not exists, creates it
                f.write("0")
                

    def save_time(self, stayed_time):
        
        self.create_file()

        data = 0
        with open(self.file, "r+") as f:

            data = int(f.read())
        open(self.file, "w").close()   # Erase all the content
        with open(self.file, "a") as f: # Write the new content
            valeur = int(data + stayed_time)
            f.write(str(valeur))



if __name__ == '__main__':



    #Programme pincinpal
    
    test = File_Manager()
    
