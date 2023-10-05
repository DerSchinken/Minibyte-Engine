from tkinter import Tk, PhotoImage, Label
from time import time


class Window(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Minibyte-Engine Default Title")

    def set_icon(self, icon_path: str):
        """
        Sets the icon of the window, will not update when icon file changes
        Supported formats: png, jpg, ico, gif (On macOS only ico is supported)
        :param icon_path: Path to the icon bitmap file
        :return:
        """
        if not icon_path.endswith(".ico"):
            img = PhotoImage(icon_path)
            self.wm_iconphoto(True, img)
        else:
            self.wm_iconbitmap(icon_path, True)
