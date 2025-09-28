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

        self.input_text = tk.StringVar()
        self.ResearchBar = tk.Entry(self, textvariable=self.input_text, font="arial", justify="right", bg="lightblue")
        self.ResearchBar.pack(fill=tk.BOTH,ipadx=20, ipady=20, pady=10)


    def BtnAddContact(self, event):
            self.master.switch_frame(1)

    def VisualizeContact(self):
         self.ContactList = self.master.ListOfContact()
         for nome, cognome in self.ContactList:
              full_name = f"{nome} {cognome}"
              self.ContactNamebtn = tk.Button(self,text=full_name)
              self.ContactNamebtn.pack(side="bottom",padx=10, fill="x", pady=10)               



       