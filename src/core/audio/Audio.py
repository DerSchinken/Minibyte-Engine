from threading import Thread

from pydub import AudioSegment
from pydub.playback import play


class Audio:
    def __init__(self, file: str, blocking: bool = False):
        self.file_name = ".".join(file.split(".")[:-1])
        self.file_type = file.split(".")[-1]
        self.audio = AudioSegment.from_file(file, file.split(".")[-1])
        self.blocking = blocking
        self.__thread = None

    def play(self) -> int:
        if self.__thread is None or not self.__thread.is_alive():
            self.__thread = Thread(
                target=self.__play,
                args=()
            )
            self.__thread.start()
            return 1
        else:
            return -1

    def __play(self) -> None:
        play(self.audio)

    def convert(self, new_file_type: str):
        self.audio.export(f"{self.file_name}.{new_file_type}", format=new_file_type)
