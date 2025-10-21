import tkinter as tk


class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        #frame on the top
        self.rowbtn = tk.Frame(self)
        self.rowbtn.pack(side="top",padx=10, fill="x", pady=10) 
        #btn on the top-right
        self.addbtn = tk.Button(self.rowbtn, text="+", bg="pink")
        self.addbtn.pack(side="right", ipadx=10, ipady=10)
        self.addbtn.bind("<Button-1>", self.BtnAddContact)

        #ResearchBar
        self.input_text = tk.StringVar()
        self.ResearchBar = tk.Entry(self, textvariable=self.input_text, font="arial", justify="right", bg="lightblue")
        self.ResearchBar.pack(fill=tk.BOTH,ipadx=20, ipady=20, pady=10)
        
        #Canvas for scrolling contact 
        self.canvas = tk.Canvas(self)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)        
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        #frame inside the canvas
        self.Contacts_Frame = tk.Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.Contacts_Frame, anchor="nw")
        self.VisualizeContact()
        
    def BtnAddContact(self, event):
            self.master.switch_frame(1)

    def VisualizeContact(self):
         self.ContactButtonList = []

         for widget in self.Contacts_Frame.winfo_children():
              widget.destroy()

         self.ContactList = self.master.ListOfContact()
         for nome, cognome in self.ContactList:
              full_name = f"{nome} {cognome}"
              btn = tk.Button(self.Contacts_Frame,text=full_name)
              btn.bind("<Button-1>", self.CallContactDetails)
              btn.pack(padx=40, fill="x", pady=10) 
              self.ContactButtonList.append(btn)              
              
    
    def CallContactDetails(self, event):
         getNameSurname = event.widget.cget("text")
         name, surname = getNameSurname.split(" ",1)
         self.master.switch_frame(2, name, surname)
    

       