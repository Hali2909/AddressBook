import tkinter as tk

class PageAddContact(tk.Frame):
    def __init__(self, master):
        super().__init__(master)


        self.FrameLabels = tk.Frame(self)
        self.FrameLabels.pack(pady=20)
        #Name
        self.NameLabel = tk.Label(self.FrameLabels, text="Name", fg="black")
        self.NameLabel.grid(row=0, column=0, padx=10, pady=5)
        self.NameEntry = tk.Entry(self.FrameLabels)
        self.NameEntry.grid(row=0, column=1, padx=10, pady=5)

        #Surname
        self.SurnameLabel = tk.Label(self.FrameLabels, text="Surname", fg="black")
        self.SurnameLabel.grid(row=1, column=0,padx=10, pady= 5)
        self.SurnameEntry = tk.Entry(self.FrameLabels)
        self.SurnameEntry.grid(row=1, column=1, padx=10, pady=5)
        
        #Number 
        self.NumberLabel = tk.Label(self.FrameLabels, text="Number", fg="black")
        self.NumberLabel.grid(row=2, column=0,padx=10, pady= 5)
        self.NumberEntry = tk.Entry(self.FrameLabels)
        self.NumberEntry.grid(row=2, column=1, padx=10, pady=5)

        #Button Save
        self.ButtonSave = tk.Button(self, text="Save", bg="red", fg="white")
        self.ButtonSave.pack(fill="both")
        #self.ButtonSave.bind("<Button-1>", SaveContact)
