import tkinter as tk

class ContactDetails(tk.Frame):
    def __init__(self,master, name, surname, number):
        super().__init__(master)
        self.master = master
        self.name = name
        self.surname = surname
        self.number = number
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
         #visualizations detaild of number
        self.NumberLabel = tk.Label(self.FrameLabels, text="Number", fg="black")
        self.NumberLabel.grid(row=2, column=0, padx=10, pady=5)
        self.NumberDetail = tk.Label(self.FrameLabels, text=self.number, fg="black")
        self.NumberDetail.grid(row=2, column=1, padx=10, pady=5)
        #Button Back 
        self.ButtonBack = tk.Button(self,text="Back", bg="red", fg="white")
        self.ButtonBack.pack(fill="both")
        self.ButtonBack.bind("<Button-1>", self.BackPage)

        #ButtonDelete
        self.ButtonDelete = tk.Button(self,text="delete", bg="red", fg="white")
        self.ButtonDelete.pack(fill="both")
        self.ButtonDelete.bind("<Button-1>", self.DeleteContact)

        #Button modify
        self.ButtonModify = tk.Button(self,text="Modify", bg="red", fg="white")
        self.ButtonModify.pack(fill="both")
        self.ButtonModify.bind("<Button-1>", self.Modify)
        
        
        
    def Modify(self, event=None):

        self.NameDetail.destroy()
        self.NameDetailEntry = tk.Entry(self.FrameLabels)
        self.NameDetailEntry.insert(0, self.name)
        self.NameDetailEntry.grid(row=0, column=1, padx=10, pady=5)

        self.SurnameDetail.destroy()
        self.SurnameDetailEntry = tk.Entry(self.FrameLabels)
        self.SurnameDetailEntry.insert(0,self.surname)
        self.SurnameDetailEntry.grid(row=1, column=1, padx=10, pady=5)

        self.NumberDetail.destroy()
        self.NumberDetailEntry = tk.Entry(self.FrameLabels)
        self.NumberDetailEntry.insert(0, self.number)
        self.NumberDetailEntry.grid(row=2, column=1, padx=10, pady=5)

        self.ButtonModify.config(text="Save")
        self.ButtonModify.bind("<Button-1>", self.SaveModifiedContact)


    def SaveModifiedContact(self, event=None):
        new_name = self.NameDetailEntry.get()
        new_surname = self.SurnameDetailEntry.get()
        new_number = self.NumberDetailEntry.get()
        self.master.ModifyContact(new_name, new_surname, new_number, self.name, self.surname, self.number)
        self.master.switch_frame(0)


    def BackPage(self, event=None):
         self.master.switch_frame(0)

    def DeleteContact(self, event=None):
        self.master.DeleteContact(self.name, self.surname, self.number)
        self.master.switch_frame(0)
