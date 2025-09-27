import tkinter as tk
from db_manager import DbManager



class PageAddContact(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.db = DbManager()
        self.master = master
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
        self.ButtonSave.bind("<Button-1>", self.SaveContact)

    def SaveContact(self, event=None):
        nome = self.NameEntry.get()
        cognome = self.SurnameEntry.get()
        telefono = self.NumberEntry.get()

        self.db.InsertContact(nome, cognome, telefono)
        self.NameEntry.delete(0, tk.END)
        self.SurnameEntry.delete(0, tk.END)
        self.NumberEntry.delete(0, tk.END)
        print("Contatto salvato con successo!")
        self.master.switch_frame(0)
