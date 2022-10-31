from tkinter import *
from turtle import color # Library for Importing GUI Application in Python 
from PIL import Image,ImageTk # Pillow library for working with Images in Python

class proxy_system:
    def __init__(self,root):
        #####################################################################################################
        # FOR DEFAULT WINDOW FORMATION AND IMAGES PLACEMENT 
        
        self.root = root
        self.root.geometry("1530x710+0+0") # To set up the Window Geometry 
        self.root.title("The Proxy Buster") # Sets up the Title for our Gui Window
        #Adding transparent background property
 #      root.wm_attributes('-transparentcolor', '#ab23ff') # For Making transparent 
        # # First Image
        # img1 = Image.open(r"Icons and Images\Nsut_Logo.png")
        # img1 = img1.resize((150,150),Image.ANTIALIAS) # For Converting  (High Level Image to Low Level)
        # #img = img.resize # For Converting hli to lli
        # self.photoimage1 = ImageTk.PhotoImage(img1)
        # label_1 = Label(self.root,image=self.photoimage1)
        # label_1.place(x=0,y=0,width=150,height=150)

        
        # Background Image 
        # backimage = Image.open(r"Icons and Images\background.jpg")
        # backiamge = backimage.resize((1530,710),Image.ANTIALIAS)
        # self.backimages = ImageTk.PhotoImage(backimage)
        
        # label_bg = Label(self.root,image=self.backimages)
        # label_bg.place(x=0,y=0,width = 1530, height = 710)
        
        # Background Image 2nd Method
        backimage = Image.open(r"Icons and Images\background2.jpg")
        backimage = backimage.resize((1530,710),Image.ANTIALIAS)
        self.backimages = ImageTk.PhotoImage(backimage)
        
        canvas1= Canvas(root,width = 1530,height = 710,bg="black")
        canvas1.pack(fill="both",expand= True,)
        canvas1.create_image(0,0,image=self.backimages,anchor = "nw")
        canvas1.create_text(700,25,text="The Proxy Buster",font=("Castellar",35,"bold"))
        
        # Title for the Window 
        # title_label = Label(label_bg,text = "Anti-Proxy",font=("times new roman", 35,"bold"))
        # title_label.place(x=0,y=0)
        
        #Creating Buttons for Various Functions
        
        #Button 1 Student Details
        button1_image = Image.open(r"Icons and Images\button1.jpg")
        button1_image = button1_image.resize((220,220),Image.ANTIALIAS)
        self.button_image1 = ImageTk.PhotoImage(button1_image)
        
        button1 = Button(canvas1,image=self.button_image1,cursor="hand2")
        button1.place(x=200,y=100,width=220,height=220)
        
        #For Creating Text Buttons
        button1_text = Button(canvas1,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"))
        button1_text.place(x=200,y=300,width=220,height=40)
        
        ######################################################################
        # Button2 Face Detection
        button2_image = Image.open(r"Icons and Images\facedetection.jpg")
        button2_image = button2_image.resize((220,220),Image.ANTIALIAS)
        self.button_image2 = ImageTk.PhotoImage(button2_image)
        
        button2 = Button(canvas1,image=self.button_image2,cursor="hand2")
        button2.place(x=500,y=100,width=220,height=220)
        
        #For Creating Text Buttons
        button2_text = Button(canvas1,text="Face Detection",cursor="hand2",font=("times new roman",15,"bold"))
        button2_text.place(x=500,y=300,width=220,height=40)
        ######################################################################
        
        # Button3 Attendance
        button3_image = Image.open(r"Icons and Images\attendance.jpg")
        button3_image = button3_image.resize((220,220),Image.ANTIALIAS)
        self.button_image3 = ImageTk.PhotoImage(button3_image)
        
        button3 = Button(canvas1,image=self.button_image3,cursor="hand2")
        button3.place(x=800,y=100,width=220,height=220)
        
        #For Creating Text Buttons
        button3_text = Button(canvas1,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"))
        button3_text.place(x=800,y=300,width=220,height=40)
        ######################################################################
        
        # Button4 Support
        button4_image = Image.open(r"Icons and Images\support.jpg")
        button4_image = button4_image.resize((220,220),Image.ANTIALIAS)
        self.button_image4 = ImageTk.PhotoImage(button4_image)
        
        button4 = Button(canvas1,image=self.button_image4,cursor="hand2")
        button4.place(x=1100,y=100,width=220,height=220)
        
        #For Creating Text Buttons
        button4_text = Button(canvas1,text="Support",cursor="hand2",font=("times new roman",15,"bold"))
        button4_text.place(x=1100,y=300,width=220,height=40)
        
        ####################################################################################################
        #Button 5 Train Data 
        button5_image = Image.open(r"Icons and Images\traindata.jpg")
        button5_image = button5_image.resize((220,220),Image.ANTIALIAS)
        self.button_image5 = ImageTk.PhotoImage(button5_image)
        
        button5 = Button(canvas1,image=self.button_image5,cursor="hand2")
        button5.place(x=200,y=400,width=220,height=220)
        
        #For Creating Text Buttons
        button5_text = Button(canvas1,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"))
        button5_text.place(x=200,y=600,width=220,height=40)
        
        ######################################################################
        # Button 6 Exit
        button6_image = Image.open(r"Icons and Images\exit.jpg")
        button6_image = button6_image.resize((220,220),Image.ANTIALIAS)
        self.button_image6 = ImageTk.PhotoImage(button6_image)
        
        button6 = Button(canvas1,image=self.button_image6,cursor="hand2")
        button6.place(x=500,y=400,width=220,height=220)
        
        #For Creating Text Buttons
        button6_text = Button(canvas1,text="Exit",cursor="hand2",font=("times new roman",15,"bold"))
        button6_text.place(x=500,y=600,width=220,height=40)
        ######################################################################
        
        


























if __name__ == "__main__":
    root = Tk()
    obj = proxy_system(root)
    root.mainloop()
    

