import tkinter as tk

class ContactDetails(tk.Frame):
    def __init__(self,master, name, surname):
        super().__init__(master)
        self.master = master
        self.name = name
        self.surname = surname
        self.FrameLabels = tk.Frame(self)
        self.FrameLabels.pack(pady=20)
        #visualizations details of names
        self.NameLabel = tk.Label(self.FrameLabels, text="Name", fg="black")
        self.NameLabel.grid(row=0, column=0, padx=10, pady=5)
        self.NameDetail = tk.Label(self.FrameLabels, text=self.name, fg="black")
        self.NameDetail.grid(row=0, column=1, padx=10, pady=5)

        #visualizations detaild of surname
        self.SurnameLabel = tk.Label(self.FrameLabels, text="Surname", fg="black")
        self.SurnameLabel.grid(row=1, column=0, padx=10, pady=5)
        self.SurnameDetail = tk.Label(self.FrameLabels, text=self.surname, fg="black")
        self.SurnameDetail.grid(row=1, column=1, padx=10, pady=5)
 #Button Back 
        self.ButtonBack = tk.Button(self,text="Back", bg="red", fg="white")
        self.ButtonBack.pack(fill="both")
        self.ButtonBack.bind("<Button-1>", self.BackPage)


    def BackPage(self, event=None):
         self.master.switch_frame(0)

    