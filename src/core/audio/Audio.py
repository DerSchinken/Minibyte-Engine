from threading import Thread

from pydub import AudioSegment
from pydub.playback import play


class Audio:
    def __init__(self, file: str):
        self.file = file
        self.file_name = ".".join(self.file.split(".")[:-1])
        self.file_type = self.file.split(".")[-1]
        self.audio = AudioSegment.from_file(self.file, self.file_type)

        self.__thread = None

    def play(self, overlapping: bool = False, blocking: bool = False) -> None:
        """
        :param overlapping: Make sound overlap-able (multiple instances of the sound playing at the same time)
        :param blocking: Make the sound playing halt execution of calls after this function until the sound has played
        """
        if self.__thread is None or (self.__thread.is_alive() and overlapping) or not self.__thread.is_alive():
            self.__thread = Thread(target=self.__play, args=())
            self.__thread.start()
            if blocking:
                self.__thread.join()

    def __play(self) -> None:
        play(self.audio)

    def convert(self, new_file_type: str) -> None:
        self.audio.export(f"{self.file_name}.{new_file_type}", format=new_file_type)
