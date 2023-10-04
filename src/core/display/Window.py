from tkinter import Tk


class Window(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Minibyte-Engine Default Title")
