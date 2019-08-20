# ---------------------------------------------------------------------------------------------------------------------
# Dateiname: plg.py
# Autor: TornaxO7
# Version: 1.0
# Letzte Veränderung: 21.08.2019
# Funktion:
#    Speichert irgendeine Datei mit der Endung ".MNBE"... keine Ahnung was das machen soll.
#    Fragt Dr. Bumm net micht.
# ---------------------------------------------------------------------------------------------------------------------
from tkinter import *
from tkinter import filedialog


class Plg:

    # Master von der GUI
    fenster = Tk()

    # Fenstergröße
    window_width, window_height = 300, 175

    def __init__(self):

        # Fenster wird allgemein vorbereitet
        # zum Beispiel fenster größe
        self.__windowConfig()

        # fenster wird vorbereitet und direkt entpackt
        self.preparePage()
        self.packPage()

        # User kann durch die Esc-Taste das Fenster schließen
        self.fenster.bind("<Escape>", self.quit)

    # ------ Allgemeine Fenster-Optionenen ------

    def __windowConfig(self):
        """
        Hier wird das Fenster in die Mitte des Fensters gepackt,
        sowie die Größe des Fensters festgelegt.
        """

        # obere Ecke des Bildschirmes wird gemessen (x-achse)
        x = (self.fenster.winfo_screenwidth() / 2) - (self.window_width / 2)
        y = (self.fenster.winfo_screenheight() / 2) - (self.window_height / 2)

        self.fenster.geometry("%dx%d+%d+%d" % (self.window_width, self.window_height, x, y))

        # Hintergrundfarbe
        self.fenster.config(bg="white")

        # Überschrift
        self.fenster.title("Modul-Konfiguration")

    def quit(self, event):
        self.fenster.destroy()

    # ----- erste Seite des Fensters -----
    def preparePage(self):
        """
        Hier wird das erste Fenster vorbereitet.
        """
        # Hier werden alle Widgets reingepackt
        self.frame = Frame(self.fenster, relief=RIDGE, bg="white")

        # Titel
        self.title = Label(self.frame,
                           text="Modul-Konfiguration",
                           bg="white",
                           font=("Arial", 20, "italic", "underline", "bold"))

        # Eingabefeld-Art Information
        self.fileNameEntryFunction = Label(self.frame,
                                           text="Dateiname:",
                                           bg="white",
                                           font=("Arial", 12, "normal"))

        # Eingabefeld
        self.fileNameEntry = Entry(self.frame)

        # Eingabefeld-Information
        self.fileNameInfo = Label(self.frame,
                                  text="Datei wird als *.MNBE* gespeichert!",
                                  fg="#555",
                                  bg="white",
                                  font=("Arial", 10, "italic"))

        # Speicher-Button
        self.saveButton = Button(self.frame,
                                 text="Speichern",
                                 command=self.saveFile)

    def packPage(self):
        """
        Hier werden alle Widgets entpackt.
        """
        self.frame.pack(side=TOP)
        self.title.grid(row=0, columnspan=2, pady=15)
        self.fileNameEntryFunction.grid(row=1, column=0, columnspan=2, sticky=W)
        self.fileNameEntry.grid(row=2, column=0, padx=5, pady=5)
        self.saveButton.grid(row=2, column=1, padx=5, pady=5)
        self.fileNameInfo.grid(row=3, column=0, columnspan=2, sticky=W)

        # Wenn der User auf "Enter" drückt, wird er direkt zum Speichern weitergeleietet
        self.fenster.bind("<Return>", self.saveFile)

    def packForgetPage(self):
        """
        Hier werden alle Widgets versteckt.
        """
        self.title.pack_forget()
        self.fileNameEntry.pack_forget()
        self.saveButton.pack_forget()

        # Wenn der User auf "Enter" drückt, wird er direkt zum Speichern weitergeleietet
        self.fenster.unbind("<Return>")

    def saveFile(self, event=None):
        """
        Hier wird der User gefragt, wohin er/sie die Datei speichern will.
        """
        # Hat der User überhaupt einen Namen eingegeben?
        if (len(self.fileNameEntry.get()) > 0) and (self.fileNameEntry.get() != "Insert Filename"):

            # "pfad" ist der Pfad, wo die Datei gespeichert werden soll
            pfad = filedialog.asksaveasfilename(**{"title" : "Speichern unter",
                                                   "initialfile" : self.fileNameEntry.get() + ".MNBE",
                                                   "confirmoverwrite" : False})

            # Hat der User auf das "X" in der Ecke gedrückt, um abzubrechen?
            try:
                with open(pfad, "w+") as file:
                    file.write("Es hat geklappt würde ich jetzt mal sagen :D hehehe...")

            except TypeError:
                pass

        else:
            self.fileNameEntry.delete(0, END)
            self.fileNameEntry.insert(END, "Insert Filename")


if __name__ == '__main__':
    start = Plg()
    mainloop()