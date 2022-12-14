
from tkinter import*

class main:
    def __init__(self, master):
        #Local Variables
        terrainx=0
        terrainy=screenh/1.5
        terrainx1=app.winfo_screenwidth()
        terrainy2=app.winfo_screenheight()
        self.gravity=10
        #Drawings
        self.canvas=Canvas(width=screenw, height=screenh)
        self.canvas.pack()
        
        self.player=self.canvas.create_rectangle(5,5,20,50,fill="green")
        self.monster=self.canvas.create_rectangle(405,5,420,50,fill="red")
        self.terrain=self.canvas.create_rectangle(terrainx,terrainy,terrainx1,terrainy2,fill="black")
        self.plataform=self.canvas.create_rectangle(terrainx+200,terrainy-30,terrainx+250,terrainy-20,fill="black")
        self.plataform_1=self.canvas.create_rectangle(terrainx+300,terrainy-50,terrainx+350,terrainy-40,fill="black")

        self.update_player()
        
        
    def update_player(self):
        #Boundaries to make collision based on border of the drawnings
        self.player_bbox=self.canvas.bbox(self.player)
        self.terrain_bbox=self.canvas.bbox(self.terrain)
        self.plataform_bbox=self.canvas.bbox(self.plataform)
        self.plataform_1_bbox=self.canvas.bbox(self.plataform_1)
        #Gravity and velocity control
        velocity=0
        velocity += self.gravity
        
        #Method to stop player if the down border of player encounter top border of terrain
        if self.player_bbox[3] >= self.terrain_bbox[1]:
            velocity=0
        
        elif self.player_bbox[3] >= self.plataform_bbox[1]:
            if self.player_bbox[2] >= self.plataform_bbox[0] and self.player_bbox[0] <= self.plataform_bbox[2] :
                velocity=0
        
        elif self.player_bbox[3] >= self.plataform_1_bbox[1]:
            if self.player_bbox[2] >= self.plataform_1_bbox[0] and self.player_bbox[0] <= self.plataform_1_bbox[2]  :
                velocity=0
        
        #Move the player based on gravity to make player come back to plataform
        self.canvas.move(self.player, 0, velocity)
        
        #Keep calling the update_player Function to make things *WORK*
        self.canvas.after(100, self.update_player)

    #Method to move player as the correspondent key is pressed
    def move_player(self, event):

        key = event.keysym
        #Move to left
        if key == "Left":
            #"Trying" to delimitate the extent it can move, in this case, the border of screen
            if self.player_bbox[0] >= 15:
                if self.player_bbox[3] >= self.terrain_bbox[1] or self.player_bbox[2] >= self.plataform_bbox[0] and self.player_bbox[0] <= self.plataform_bbox[2] or self.player_bbox[2] >= self.plataform_1_bbox[0] and self.player_bbox[0] <= self.plataform_1_bbox[2]:
                    self.canvas.move(self.player, -5,0)
                    print("Left")
                    app.update()
            else:
                print("Cant Move")
        #Move Up(Aka:Jump)
        if key == "Up":
            #Only allow "jumping" if the
            if self.player_bbox[3] >= self.terrain_bbox[1] or self.player_bbox[3] >= self.plataform_bbox[1] and self.player_bbox[2] >= self.plataform_bbox[0] and self.player_bbox[0] <= self.plataform_bbox[2] or self.player_bbox[3] >= self.plataform_1_bbox[1] and self.player_bbox[2] >= self.plataform_1_bbox[0] and self.player_bbox[0] <= self.plataform_1_bbox[2]:
                self.canvas.move(self.player, 0,-50)
                print("Up")
                self.canvas.after(150)
            else:
                print("Cant Move")

        #Move Right
        elif key == "Right":
            #"Trying" to delimitate the extent it can move, in this case, the border of screen
            if self.player_bbox[2] <= screenw-15:
                if self.player_bbox[3] >= self.terrain_bbox[1] or self.player_bbox[2] >= self.plataform_bbox[0] and self.player_bbox[0] <= self.plataform_bbox[2] or self.player_bbox[2] >= self.plataform_1_bbox[0] and self.player_bbox[0] <= self.plataform_1_bbox[2]:
                    self.canvas.move(self.player, 5,0)
                    print("Right")
                    app.update()
            else:
                print("Cant Move")
        

#Main Program
app=Tk()

#Global Variables
screenw=app.winfo_screenwidth()/2
screenh=app.winfo_screenheight()/2

#Screen Settings
app.geometry("%dx%d+%d+%d"%(screenw,screenh,screenw/2,screenh/2))
app.resizable(0,0)

#Call-out
root=main(app)

root.canvas.bind_all("<KeyPress>",root.move_player)





#Main Loop
app.mainloop()
