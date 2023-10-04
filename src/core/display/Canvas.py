from tkinter import Canvas as tkCanvas


class Canvas(tkCanvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(expand=True, fill="both")
