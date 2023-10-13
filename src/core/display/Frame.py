from tkinter import Frame as tkFrame


class Frame(tkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.pack()
