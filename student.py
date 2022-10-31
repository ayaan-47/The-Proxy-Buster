from tkinter import *
from tkinter import ttk
from tkinter import font
from turtle import right, width
from PIL import Image,ImageTk 

class Student:
    def __init__(self,root):


        self.root = root
        self.root.geometry("1530x710+0+0") 
        self.root.title("Student-Details") 
        
        myColor = 'cornsilk3'                 # Its a light blue color
        root.configure(bg=myColor)          # Setting color of main window to myColor

        s = ttk.Style()                     # Creating style element
        s.configure('Wild.TRadiobutton',    # First argument is the name of style. Needs to end with: .TRadiobutton
        background=myColor,         # Setting background to our specified color above
        foreground='black',
        font=("consolas",12,"bold",))
        
        backimage = Image.open(r"Icons and Images\background.jpg")
        backimage = backimage.resize((1530,710),Image.ANTIALIAS)
        self.backimages = ImageTk.PhotoImage(backimage)
        
        # canvas1= Canvas(root,width = 1530,height = 710)
        # canvas1.pack(fill="both",expand= True)
        # canvas1.create_image(0,0,image=self.backimages,anchor = "nw")
        # canvas1.create_text(700,25,text="Student-Details",font=("times new roman",35,"bold"))

        
        label_bg = Label(self.root,image=self.backimages)
        label_bg.place(x=0,y=0,width = 1530, height = 710)
        
        #Creating a New Blank Frame
        
        main_frame=Frame(label_bg, bd=2,bg="cornsilk2")
        main_frame.place(x=0,y=50,width=1400,height=600)
        
        # Creating Left Frame
        left_frame = LabelFrame(main_frame,bd=4,bg="cornsilk3",text="Student Details",font=("consolas",15,"bold"))
        left_frame.place(x=0,y=0,width=650,height=550)
        
        # current_frame = LabelFrame(left_frame,bd=4,bg="cornsilk3",text="Department",font=("consolas",12,"bold"))
        # current_frame.place(x=10,y=0,width=600,height=300)
        # Branch Selection
        branch_label = Label(left_frame,bg="cornsilk3",text="Branch",font=("consolas",15,"bold"))
        branch_label.grid(row=0,column=0,sticky="w",padx=2,pady=10)
        
        branch_com = ttk.Combobox(left_frame,font=("consolas",12,"bold"),state="readonly")
        branch_com["values"] = ("Select Branch","Computer Science Engineering","Electronics")
        branch_com.current(0)
        branch_com.grid(row=0,column=1,sticky="w")
        
        ##
        # Semester Selection
        semester_label = Label(left_frame,bd=2,bg="cornsilk3",text="Semester",font=("consolas",15,"bold"))
        semester_label.grid(row=0,column=2,sticky="w",padx=2,pady=10)
        
        semester_com = ttk.Combobox(left_frame,font=("consolas",12,"bold"),state="readonly",width=15)
        semester_com["values"] = ("Select Semester","1","2","3","4","5","6","7","8")
        semester_com.current(0)
        semester_com.grid(row=0,column=3,sticky="w",padx=2,pady=10)
        
       
        # Student Name
        name_label = Label(left_frame,bd=2,bg="cornsilk3",text="Student Name",font=("consolas",15,"bold"))
        name_label.grid(row=1,column=0,sticky="w",padx=2,pady=10)
        
        name_input = ttk.Entry(left_frame,font=("consolas",12,"bold"))
        name_input.grid(row=1,column=1,padx=2,pady=10,sticky="w")
        # Roll Selection
        roll_label = Label(left_frame,bd=2,bg="cornsilk3",text="Roll No",font=("consolas",15,"bold"))
        roll_label.grid(row=1,column=2,sticky="w",padx=2,pady=10)
        
        roll_input = ttk.Entry(left_frame,font=("consolas",12,"bold"))
        roll_input.grid(row=1,column=3,padx=2,pady=10,sticky="w")
        # Phone Selection
        phone_label = Label(left_frame,bd=2,bg="cornsilk3",text="Phone",font=("consolas",15,"bold"))
        phone_label.grid(row=2,column=0,sticky="w",padx=2,pady=10)
        
        phone_input = ttk.Entry(left_frame,font=("consolas",12,"bold"))
        phone_input.grid(row=2,column=1,padx=2,pady=10,sticky="w")
        # email Selection
        email_label = Label(left_frame,bd=2,bg="cornsilk3",text="Email",font=("consolas",15,"bold"))
        email_label.grid(row=2,column=2,sticky="w",padx=2,pady=10)
        
        email_input = ttk.Entry(left_frame,font=("consolas",12,"bold"))
        email_input.grid(row=2,column=3,padx=2,pady=10,sticky="w")
        # dob Selection
        dob_label = Label(left_frame,bd=2,bg="cornsilk3",text="DOB",font=("consolas",15,"bold"))
        dob_label.grid(row=3,column=0,sticky="w",padx=2,pady=10)
        
        dob_input = ttk.Entry(left_frame,font=("consolas",12,"bold"))
        dob_input.grid(row=3,column=1,padx=2,pady=10,sticky="w")
        # Year Selection
        year_label = Label(left_frame,bd=2,bg="cornsilk3",text="Year",font=("consolas",15,"bold"))
        year_label.grid(row=3,column=2,sticky="w",padx=2,pady=10)
        
        year_input = ttk.Entry(left_frame,font=("consolas",12,"bold"))
        year_input.grid(row=3,column=3,padx=2,pady=10,sticky="w")
        
       
        
        # Creating Radio Buttons
        radio_button_label = Label(left_frame,bg="cornsilk3",text="Photo Sample",font=("consolas",15,"bold"))
        radio_button_label.grid(row=4,column=0)
        radio_button1= ttk.Radiobutton(left_frame,text="Yes",value="Yes",style="Wild.TRadiobutton")
        radio_button1.grid(row=4,column=1)
        radio_button2= ttk.Radiobutton(left_frame,text="No",value="No",style="Wild.TRadiobutton")
        radio_button2.grid(row=4,column=2)
        # #
        
        # Creating Save Button
        
        save_button = Button(left_frame,bg="cornsilk2",cursor="hand1",text="Save",font=("consolas",15,"bold"),width=50)
        save_button.place(x=50,y=400,width=550,height=70)
        
        
        # Creating Right Frame
        right_frame = LabelFrame(main_frame,bd=4,bg="cornsilk3",text="Details Display",font=("consolas",12,"bold"))
        right_frame.place(x=690,y=0,width=650,height=550)
        
        # Search Options in Right Frame
        
        # search_frame = LabelFrame(right_frame,bd=4,bg="cornsilk3",text="Search System",font=("consolas",15,"bold"))
        # search_frame.place(x=0,y=0,width=650,height=550)
        search_label = Label(right_frame,bd=2,bg="cornsilk3",text="Search By:",font=("consolas",15,"bold"))
        search_label.grid(row=0,column=0,sticky="w",padx=2,pady=10)
        
        
        
        search_comb = ttk.Combobox(right_frame,font=("consolas",12,"bold"),state="readonly",width=6)
        search_comb["values"] = ("Select","Roll Number","Name","Phone Number")
        search_comb.current(0)
        search_comb.grid(row=0,column=1,sticky="w")
        
        search_input = ttk.Entry(right_frame,font=("consolas",12,"bold"))
        search_input.grid(row=0,column=2,padx=2,pady=10,sticky="w")
        
        search_button = Button(right_frame,bg="cornsilk2",cursor="hand1",text="Search",font=("consolas",12,"bold"))
        search_button.grid(row=0,column=3)
        
        # table frame
        table_frame = Frame(right_frame,bd=2,bg="cornsilk3",relief=RIDGE)
        table_frame.place(x=5,y=110,width=625,height=350)
        
        scroll_x= ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame,column = ("branch","name","roll Number","email","phone number","semester"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll Number",text="Roll Number")
        self.student_table.heading("email",text="Email Id")
        self.student_table.heading("phone number",text="Phone Number")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("branch",text="Branch")
        
        # For changing Width of Each and Every Column
        self.student_table.column("branch",width=50)
        
        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH,expand=1)
        
        
        

        


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
    

