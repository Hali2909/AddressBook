import tkinter as tk



class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        #frame on the top
        self.rowbtn = tk.Frame(self)
        self.rowbtn.configure(bg="#fffaf0")
        self.rowbtn.pack(side="top",padx=10, fill="x", pady=10) 
        #btn on the top-right
        self.addbtn = tk.Button(self.rowbtn, text="+", bg="#ff69b4", fg ="white", font=("Arial",16, "bold"), width=2, heigh=1, relief="flat", bd=0)
        self.addbtn.pack(side="right", ipadx=10, ipady=10)
        self.addbtn.bind("<Button-1>", self.BtnAddContact)

        #ResearchBar
        self.input_text = tk.StringVar()
        self.ResearchBar = tk.Entry(self, textvariable=self.input_text,  font=("Arial", 14), justify="left", bg="#e0f7fa", relief="groove", bd=2)
        self.ResearchBar.pack(fill="x", padx=20, pady=10, ipady=8)

        
        #Canvas for scrolling contact 
        self.canvas = tk.Canvas(self,  bg="#fffaf0")
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)        
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        #frame inside the canvas
        self.Contacts_Frame = tk.Frame(self.canvas, bg="#fffaf0")
        
        self.canvas_window = self.canvas.create_window((0, 0), window=self.Contacts_Frame, anchor="nw")
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        self.Contacts_Frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.VisualizeContact()
        self.Contacts_Frame.configure(bg="#fffaf0")
        
    def BtnAddContact(self, event):
            self.master.switch_frame(1)

    def VisualizeContact(self):
         self.ContactButtonList = []

         for widget in self.Contacts_Frame.winfo_children():
              widget.destroy()

         self.ContactList = self.master.ListOfContact()
         for nome, cognome, numero in self.ContactList:
              full_name = f"{nome} {cognome}"
              btn = tk.Button(self.Contacts_Frame,text=full_name, font=("Arial", 12), bg="#fce4ec", fg="#880e4f", relief="ridge", bd=2, anchor="center")
              btn.numero = numero
              btn.bind("<Button-1>", self.CallContactDetails)
              btn.pack(fill="x", pady=5) 
              self.ContactButtonList.append(btn)              
              
             
    def on_canvas_configure(self, event):
         self.canvas.itemconfig(self.canvas_window, width=event.width)

    def CallContactDetails(self, event):
         getNameSurname = event.widget.cget("text")
         name, surname = getNameSurname.split(" ",1)
         number = event.widget.numero
         self.master.switch_frame(2, name, surname, number)
