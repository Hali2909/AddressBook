import tkinter as tk


class PageAddContact(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure(bg="#fffaf0")
        self.FrameLabels = tk.Frame(self, bg="#fffaf0")
        self.FrameLabels.pack(pady=30)
        #Name
        self.NameLabel = tk.Label(self.FrameLabels, text="Name", fg="#880e4f", bg="#fffaf0", font=("Arial", 12))
        self.NameLabel.grid(row=0, column=0, padx=10, pady=5)
        self.NameEntry = tk.Entry(self.FrameLabels, font=("Arial", 12), bg="#fce4ec", relief="groove", bd=2)
        self.NameEntry.grid(row=0, column=1, padx=10, pady=5)

        #Surname
        self.SurnameLabel = tk.Label(self.FrameLabels, text="Surname", fg="#880e4f", bg="#fffaf0", font=("Arial", 12))
        self.SurnameLabel.grid(row=1, column=0,padx=10, pady= 5, sticky="e")
        self.SurnameEntry = tk.Entry(self.FrameLabels, font=("Arial", 12), bg="#fce4ec", relief="groove", bd=2)
        self.SurnameEntry.grid(row=1, column=1, padx=10, pady=5)
        
        #Number 
        self.NumberLabel = tk.Label(self.FrameLabels, text="Number", fg="#880e4f", bg="#fffaf0", font=("Arial", 12))
        self.NumberLabel.grid(row=2, column=0,padx=10, pady= 5, sticky="e")
        self.NumberEntry = tk.Entry(self.FrameLabels, font=("Arial", 12), bg="#fce4ec", relief="groove", bd=2)
        self.NumberEntry.grid(row=2, column=1, padx=10, pady=5)

        #Button Save
        self.ButtonSave = tk.Button(self, text="Save", bg="#ff69b4", fg="white", font=("Arial", 12, "bold"), relief="flat")
        self.ButtonSave.pack(fill="x", padx=40, pady=10)
        self.ButtonSave.bind("<Button-1>", self.SaveContact)

        #Button Back 
        self.ButtonBack = tk.Button(self,text="Back", bg="#ff69b4", fg="white", font=("Arial", 12, "bold"), relief="flat")
        self.ButtonBack.pack(fill="x", padx=40, pady=10)
        self.ButtonBack.bind("<Button-1>", self.BackPage)


    def BackPage(self, event=None):
         self.master.switch_frame(0)

    

    def SaveContact(self, event=None):
        nome = self.NameEntry.get()
        cognome = self.SurnameEntry.get()
        telefono = self.NumberEntry.get()

        self.master.InsertContact(nome, cognome, telefono)
        self.NameEntry.delete(0, tk.END)
        self.SurnameEntry.delete(0, tk.END)
        self.NumberEntry.delete(0, tk.END)
        print("Contatto salvato con successo!")
        self.master.switch_frame(0)
       