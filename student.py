from tkinter import *  
from PIL import Image,ImageTk 

class Student:
    def __init__(self,root):

        
        self.root = root
        self.root.geometry("1530x710+0+0") 
        self.root.title("Student-Details") 
        
        backimage = Image.open(r"Icons and Images\background.jpg")
        backimage = backimage.resize((1530,710),Image.ANTIALIAS)
        self.backimages = ImageTk.PhotoImage(backimage)
        
        canvas1= Canvas(root,width = 1530,height = 710)
        canvas1.pack(fill="both",expand= True)
        canvas1.create_image(0,0,image=self.backimages,anchor = "nw")
        canvas1.create_text(700,25,text="Student-Details",font=("times new roman",35,"bold"))





if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
    

