from tkinter import *

class main():
    def __init__(self,parent):
        super().__init__()
        self.SP()
    
    def SP(self):
        
        def playbtn(event):
            print("play pressed")
            w.delete("all")
            CC()
        def quitbtn(event):
            root.destroy()

        w = Canvas(width= 800, height=600)
        
        w.grid(row=0,column=0)
        
        play = w.create_image(60,500, image=playimg)

        w.tag_bind(play, "<Button-1>",playbtn)

        quit=w.create_image(57,555, image=quitimg)
        w.tag_bind(quit, "<Button-1>", quitbtn)

    
def CC(): 
    w = Canvas(width= 800, height=600)
    w.grid(row=0,column=0)
    
if __name__ == '__main__':
    root=Tk()
    playimg = PhotoImage(file="images/playmain.png")
    quitimg = PhotoImage(file="images/quitmain.png")
    ccimage = PhotoImage(file="images/cc.png")
    main=main(root)
    root.mainloop()