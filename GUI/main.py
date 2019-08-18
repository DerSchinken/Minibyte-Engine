# ---------------------------------------------------------------------------------------------------------------------
# Dateiname: main.py
# Autor: TornaxO7
# Version: 1.0
# Letzte Veränderung: 18.08.2019
# Funktion:
#    Erstellt die GUI welches das Startmenü des Spiels sein wird.
# ---------------------------------------------------------------------------------------------------------------------

from tkinter import *


class GUI:

    def __init__(self):

        self.fenster = Tk()

        # Variable, um zu gucken, ob die Maus über einen Button ist
        self.mouseOverButton = False

        # Fenster wird platziert, sowie Hintergrund wird angepasst
        self.__windowConfig()

        # erstes Fenster wird geladen
        self.firstPage()
        self.packFirstPage()

        # Die restlichen Fenster werden schonmal geladen
        self.prepareInstruction()

    def __windowConfig(self):
        """
        Hier wird das Fenster in die Mitte des Fensters gepackt,
        sowie die Größe des Fensters festgelegt.
        """

        # höhe und breite des Fensters
        window_height, window_width = 350, 400

        # obere Ecke des Bildschirmes wird gemessen (x-achse)
        x = (self.fenster.winfo_screenwidth() / 2) - (window_width / 2)
        y = (self.fenster.winfo_screenheight() / 2) - (window_height / 2)

        self.fenster.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y))

        # Hintergrundfarbe
        self.fenster.config(bg="#444")

    def firstPage(self):
        """
        Hier wird die erste Seite erstellt.
        Inhalt:
            - Name des Spiels
            - Teilnehmer dieses Projektes
            - Begrüßung
            - Spielanleitung
            - "Play Game"

        Neue Variablen:
        - titleName: Titel auf der ersten Seite     type: Label
        - vorlage (für self.textInhalt)             type: String
        - textInhalt                                type: Label
        - firstButtonFrame                          type: Frame
        - spielButton                               type: Button
        - anleitungButton                           type: Button
        - verlassenButton                           type: Button
        """

        # Name des Spiels
        self.titleName = Label(self.fenster,
                               text="Minibyte-Engine",
                               bg="#444",
                               fg="#55CC05",
                               font=("Helvetica", 20, "italic", "bold", "underline"))

        # Kurzer Text
        vorlage = "Herzlich Willkommen zur Minibyte-Engine!\n" \
                  "Wir wünschen dir viel Spaß c(^-^)c\n\n" \
                  "- Dr.Bumm (Projektleiter und Entwickler) \n & TornaxO7(Entwickler)"

        self.textInhalt = Label(self.fenster,
                                text=vorlage,
                                bg="#444",
                                fg="#55CCAA",
                                font=("Arial", 15, "normal"))

        # ---------- Buttons: Spielen und Anleitung ----------

        # Dafür wird spieziell ein Frame erstellt
        self.firstButtonFrame = Frame(self.fenster,
                                      relief=RIDGE,
                                      bd=3,
                                      bg="#444")

        self.spielButton = Button(self.firstButtonFrame,
                                  text="Spielen",
                                  command=None,
                                  width=19,
                                  height=2,
                                  bg="#888")

        self.anleitungButton = Button(self.firstButtonFrame,
                                      text="Anleitung",
                                      command=self.startInstruction,
                                      width=6,
                                      height=2,
                                      bg="#888")

        self.verlassenButton = Button(self.firstButtonFrame,
                                text="Verlassen",
                                command=self.close,
                                width=19,
                                height=2,
                                bg="#888")

    def packFirstPage(self):
        """
        Hier werden alle Widgets entpackt,
        die auf der ersten Seite sein sollen.
        """
        self.titleName.pack(anchor=N, padx=5, pady=5)
        self.textInhalt.pack(anchor=CENTER, padx=5, pady=10)

        # Buttons
        self.firstButtonFrame.pack(anchor=CENTER, padx=5, pady=10, fill=X)
        self.spielButton.grid(row=0, column=0, padx=5, pady=5)
        self.verlassenButton.grid(row=0, column=1, padx=5, pady=5)
        self.anleitungButton.grid(row=1, columnspan=2, sticky=N+E+S+W, padx=5, pady=5)

    def packForgetFirstPage(self):
        """
        Hier werden alle Widgets von der ersten Seite weggemacht,
        bzw. unsichtbar gemacht.
        """
        self.titleName.pack_forget()
        self.textInhalt.pack_forget()

        # Buttons
        self.firstButtonFrame.pack_forget()

    # ---------- Button Funktionen von der ersten Seite ----------
    def spielerAuswahl(self):
        """
        Wird verwendet, wenn der Spieler auf "Spielen" gedrückt hat.
        """
        self.packForgetFirstPage()

        # Spielerauswahl == 2. Fenster
        self.selectOpponent()

    def close(self):
        """
        User möchte das Fenster schließen. ("Verlasen"-Button wird betätigt)
        """
        self.fenster.quit()

    def startInstruction(self):
        """
        Zeigt die Anleitung an, wenn der User auf "Anleitung" drücktt.
        """
        self.packForgetFirstPage()
        self.packInstruction()

    def packInstruction(self):
        """
        Lässt die Widgets vom Anleitungsfenster erscheinen.
        """
        self.anleitungText.pack(anchor=N, padx=5, pady=5)
        self.backToMenuButton.pack(anchor=S, padx=20, pady=5, fill=X)

    # ----------- Anleitungsfenster -----------

    def prepareInstruction(self):
        """
        Fenster wird für die Anleitung angepasst.

        Wichtige Variabeln:
        - vorlage (Beinhaltet den Text der Anleitung)       type: String
        - anleitungText                                     type: Label
        - backToMenuButton (füht User zurück zum Hauptmenü) type: Button
        """
        vorlage = "(Kommt im nächstem Update...)"

        self.anleitungText = Label(self.fenster,
                                   text=vorlage,
                                   font=("Arial", 20, "italic"),
                                   bg="#444",
                                   fg="#55CCAA")

        # Button, um zurück zum Menu zu kommen
        self.backToMenuButton = Button(self.fenster,
                                 text="Zurück",
                                 command=self.backFromInstruction)

    # Buttons - Funktionen
    def packForgetInstruction(self):
        """
        Lässt alle Widgets für das Anleitungsfenster verschwinden.
        """
        self.anleitungText.pack_forget()
        self.backToMenuButton.pack_forget()

    def backFromInstruction(self):
        """
        User wird zurück zum Hauptmenü gebracht. (von der Anleitungseite aus)
        """
        self.packForgetInstruction()
        self.packFirstPage()

    def selectOpponent(self):
        """
        Hier kann der Spieler entscheiden, ob er gegen den Computer spielen möchte
        oder gegen einen anderen Spieler.
        """
        self.packForgetFirstPage()


if __name__ == '__main__':
    start = GUI()
    mainloop()
