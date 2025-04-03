"""
This working code was found at https://stackoverflow.com/questions/61513791/passing-a-tkinter-canvas-between-classes-without-calling-the-child-from-within-t

I will be reviewing this and writing my own in another file in order to apply my knowledge.
"""

from tkinter import *
from time import sleep


class mainWindow():
    def __init__(self):
            #Setup the GUI
            self.jump_gap = 25
            root = Tk()
            root.geometry('800x600')
            # Setup the canvas within the GUI (master)
            self.world = Canvas(root, height = 600, width = 800, bg = "#FFFFFF")
            self.world.place(relx = 0.5, rely = 0.5, anchor = CENTER)

            self.hero = Hero(self.world)
            self.world.pack()
            root.bind("<space>",self.jump) # -> [1] Binds the SPACE BAR Key to the function jump 
            root.mainloop()

    def jump(self,event):
        gaps = list(range(self.jump_gap))
        for i in gaps:
            self.world.after(1,self.hero.moveHeroJump(h=i))  # [2] -> Binds the moveHeroJump method with the window action to a queue of updates
            self.world.update() #[2] updates the canvas
            sleep(0.01*i) # Added some linear wait time to add some look to it
        gaps.reverse()
        for i in gaps:
            self.world.after(1,self.hero.moveHeroJump(h=-i))
            self.world.update()
            sleep(0.01*i)


class Hero():
    def __init__(self,world):
        #Initial creation of hero at coordinates
        self.world = world
        self.x1 = 10
        self.y1 = 410
        self.x2 = 70
        self.y2 = 470
        self.heroBody = self.world.create_oval(self.x1,self.y1,self.x2,self.y2, fill = "#FF0000", outline = "#FF0000")

    #Move the hero
    def moveHeroJump(self,h):
        print("moveHeroBody")
        self.y1 -= h
        self.y2 -= h
        self.world.delete(self.heroBody)
        self.heroBody = self.world.create_oval(self.x1,self.y1,self.x2,self.y2, fill = "#FF0000", outline = "#FF0000")