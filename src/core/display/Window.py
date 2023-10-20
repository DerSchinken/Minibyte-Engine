from tkinter import Tk, PhotoImage, Label
from time import time, sleep


class Window(Tk):
    ROOT = None

    def __init__(self, *args, **kwargs):
        self.__display_fps = kwargs.pop("display_fps")
        title = kwargs.pop("title", None)

        super().__init__(*args, **kwargs)

        if title is not None:
            self.title(title)
        else:
            self.title("Minibyte-Engine Default Title")

        self.frame_count = 0
        self.start_time = time()
        self.fps_label = None
        self.running = True

        self.__sleep_time = 0
        self.__fps = 0  # 0 = Infinity

        if not Window.ROOT:
            Window.ROOT = self

    def display_fps(self) -> None:  # I think this still capping yo
        current_time = time()
        elapsed_time = current_time - self.start_time
        self.frame_count += 1

        # Update FPS every second
        if elapsed_time >= 1.0:
            fps = self.frame_count / elapsed_time
            self.frame_count = 0
            self.start_time = current_time

            # If the FPS label is not created, create it
            if self.fps_label is None:
                self.fps_label = Label(self, text=f"FPS: {fps:.2f}")
                self.fps_label.place(x=0, y=0)
            else:
                self.fps_label.config(text=f"FPS: {fps:.2f}")

            self.fps_label.lift()

    @property
    def fps(self) -> int | float:
        return self.__fps   # Fixme: fps are apparently halved

    @fps.setter
    def fps(self, fps: int):   # Fixme: fps are apparently halved
        if not isinstance(fps, int):
            raise TypeError("'fps' needs to be of type 'int'")

        self.__sleep_time = 1/fps
        self.__fps = fps

    def set_icon(self, icon_path: str) -> None:
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

    def mainloop(self, fps: int = 0) -> None:
        """
        Be aware that this function uses time.sleep to achieve the given fps, this can, on some versions of Python, \
        lead to inaccurate fps.
        :param fps:
        :return:
        """
        self.protocol("WM_DELETE_WINDOW", self.close)

        if fps:
            self.__fps = fps
            self.__sleep_time = 1/fps
            print(self.__sleep_time, 1/fps)
        try:
            while self.running:
                self.update()
                self.update_idletasks()
                if self.__display_fps and self.running:
                    self.display_fps()
                if fps:
                    sleep(self.__sleep_time)
        except Exception as e:
            self.close()
            raise e

    def close(self) -> None:
        """
        Safely destroys all .afters and children of this window
        """
        self.running = False
        for after_event_id in self.call("after", "info"):
            self.after_cancel(after_event_id)
        for child in self.winfo_children():
            child.destroy()
        self.destroy()
