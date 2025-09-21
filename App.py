import tkinter as tk

from home_page import HomePage


class App(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("AddressBook")
        self.geometry("600x600")
        self.current_frame = None

        self.switch_frame(HomePage)


    def  switch_frame(self, frame_class, *args):
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = frame_class(self, *args)
        self.current_frame.pack(fill="both", expand=True)



if __name__== "__main__":
    app = App()
    app.mainloop()