import tkinter as tk

class ContactDetails(tk.Frame):
    def __init__(self,master, name, surname, number):
        super().__init__(master)
        self.master = master
        self.name = name
        self.surname = surname
        self.number = number
        self.configure(bg="#fffaf0")  

        self.FrameLabels = tk.Frame(self, bg="#fffaf0")
        self.FrameLabels.pack(pady=20)
        #visualizations details of names
        self.NameLabel = tk.Label(self.FrameLabels, text="Name", fg="#880e4f", bg="#fffaf0", font=("Arial", 12))
        self.NameLabel.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.NameDetail = tk.Label(self.FrameLabels, text=self.name, fg="#333", bg="#fffaf0", font=("Arial", 12))
        self.NameDetail.grid(row=0, column=1, padx=10, pady=5)

        #visualizations detaild of surname
        self.SurnameLabel = tk.Label(self.FrameLabels, text="Surname", fg="#880e4f", bg="#fffaf0", font=("Arial", 12))
        self.SurnameLabel.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.SurnameDetail = tk.Label(self.FrameLabels, text=self.surname, fg="#333", bg="#fffaf0", font=("Arial", 12))
        self.SurnameDetail.grid(row=1, column=1, padx=10, pady=5)

         #visualizations detaild of number
        self.NumberLabel = tk.Label(self.FrameLabels, text="Number", fg="#880e4f", bg="#fffaf0", font=("Arial", 12))
        self.NumberLabel.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.NumberDetail = tk.Label(self.FrameLabels, text=self.number, fg="#333", bg="#fffaf0", font=("Arial", 12))
        self.NumberDetail.grid(row=2, column=1, padx=10, pady=5)

        #Button Back 
        self.ButtonBack = tk.Button(self,text="Back", bg="#ff69b4", fg="white", font=("Arial", 12, "bold"), relief="flat")
        self.ButtonBack.pack(fill="x", padx=40, pady=10)
        self.ButtonBack.bind("<Button-1>", self.BackPage)

        #ButtonDelete
        self.ButtonDelete = tk.Button(self,text="delete",  bg="#ff69b4", fg="white", font=("Arial", 12, "bold"), relief="flat")
        self.ButtonDelete.pack(fill="x", padx=40, pady=10)
        self.ButtonDelete.bind("<Button-1>", self.DeleteContact)

        #Button modify
        self.ButtonModify = tk.Button(self,text="Modify",  bg="#ff69b4", fg="white", font=("Arial", 12, "bold"), relief="flat")
        self.ButtonModify.pack(fill="x", padx=40, pady=10)
        self.ButtonModify.bind("<Button-1>", self.Modify)
        
        
        
    def Modify(self, event=None):

        self.NameDetail.destroy()
        self.NameDetailEntry = tk.Entry(self.FrameLabels, font=("Arial", 12), bg="#fce4ec", relief="groove", bd=2)
        self.NameDetailEntry.insert(0, self.name)
        self.NameDetailEntry.grid(row=0, column=1, padx=10, pady=5)

        self.SurnameDetail.destroy()
        self.SurnameDetailEntry = tk.Entry(self.FrameLabels, font=("Arial", 12), bg="#fce4ec", relief="groove", bd=2)
        self.SurnameDetailEntry.insert(0,self.surname)
        self.SurnameDetailEntry.grid(row=1, column=1, padx=10, pady=5)

        self.NumberDetail.destroy()
        self.NumberDetailEntry = tk.Entry(self.FrameLabels, font=("Arial", 12), bg="#fce4ec", relief="groove", bd=2)
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
