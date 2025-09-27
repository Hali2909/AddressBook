import sqlite3


class DbManager():
    def __init__(self):
        self.cx = sqlite3.connect("AddressBook.db")
        self.cu = self.cx.cursor()
        self.cu.execute("CREATE TABLE IF NOT EXISTS Contact(nome TEXT, cognome TEXT, telefono TEXT)")
       
    def InsertContact(self, nome, cognome, telefono):
        self.cu.execute("INSERT INTO Contact(nome, cognome, telefono) VALUES(?,?,?)", (nome, cognome, telefono))
        self.cx.commit()

    def DeleteContact(self, nome, cognome, telefono):
        self.cu.execute("DELETE FROM Contact Where nome= ? AND cognome = ? AND telefono = ?", (nome, cognome, telefono))
        self.cx.commit()

    