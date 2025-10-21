import tkinter as tk
from home_page import HomePage
from PageAddContact import PageAddContact
from db_manager import DbManager
from ContactDetails import ContactDetails

class App(tk.Tk):
    
    def __init__(self,):
        super().__init__()
        self.title("AddressBook")
        self.geometry("600x600")
        self.current_frame = None
        self.db = DbManager()
        # show the first page (HomePage) by index
        self.switch_frame(0)


    def switch_frame(self, index, *args):
        pages_dict = {0: HomePage, 1: PageAddContact, 2: ContactDetails}
        if self.current_frame is not None:
            self.current_frame.destroy()

        page_class = pages_dict.get(index)
        if page_class is None:
            raise ValueError(f"No page found for index: {index}")

        self.current_frame = page_class(self, *args)
        self.current_frame.pack(fill="both", expand=True)

    def InsertContact(self, nome, cognome, telefono):
        self.db.InsertContact(nome, cognome, telefono)
        self.ListOfContact()

    def DeleteContact(self, nome, cognome, telefono):
        self.db.DeleteContact(nome, cognome, telefono)
    

    def ListOfContact(self):
        self.NameAndSurname = self.db.ListOfContact()
        return self.NameAndSurname



if __name__== "__main__":
    app = App()
    app.mainloop()