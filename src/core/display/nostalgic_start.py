# ruff: noqa
# ---------------------------------------------------------------------------------------------------------------------
# Dateiname: main.py
# Autor: TornaxO7
# Version: 1.3
# Letzte Veränderung: 20.08.2019
# Funktion:
#    Erstellt die GUI welches das Startmenü des Spiels sein wird.
# ---------------------------------------------------------------------------------------------------------------------

from tkinter import *


class GUI:
    def __init__(self):
        # Ansprechpartner der ganzen GUI
        self.fenster = Tk()

        # Standard - Fenstergröße
        self.window_height, self.window_width = 350, 400
        # User kann nicht die Fenstergröße verändern
        self.fenster.resizable(False, False)

        # Variable, um zu gucken, ob die Maus über einen Button ist
        self.mouseOverButton = False

        # Fenster wird platziert, sowie Hintergrund wird angepasst
        self.__windowConfig()

        # Die restlichen Fenster werden schonmal geladen
        self.prepareMainPage()
        self.prepareInstruction()
        self.prepareSelectOpponentPage()

        # erstes Fenster wird geladen
        self.packMainPage()

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
        self.fenster.config(bg="#444")

        # Überschrift
        self.fenster.title("Minibyte-Engine")

    def resetWindowSize(self):
        """
        Hier wird das Fenster zurück auf ihre Standard Fenstergröße zurückgebracht.
        """
        self.fenster.geometry("%dx%d" % (self.window_width, self.window_height))

    def prepareMainPage(self):
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
                                  command=self.selectOpponentPage,
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

    def packMainPage(self):
        """
        Hier werden alle Widgets entpackt,
        die auf der ersten Seite sein sollen.
        """
        self.titleName.pack(anchor=N, padx=5, pady=5)
        self.textInhalt.pack(anchor=CENTER, padx=5, pady=10)

        # Buttons
        self.firstButtonFrame.pack(anchor=CENTER, padx=5, pady=10, ipadx=0)
        self.spielButton.grid(row=1, column=0, padx=5, pady=5)
        self.verlassenButton.grid(row=1, column=1, padx=5, pady=5)
        self.anleitungButton.grid(row=2, columnspan=2, sticky=N+E+S+W, padx=5, pady=5)

    def packForgetMainPage(self):
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
        self.packForgetMainPage()

        # Spielerauswahl == 2. Fenster
        self.selectOpponent()

    def close(self):
        """
        User möchte das Fenster schließen. ("Verlasen"-Button wird betätigt)
        """
        self.fenster.destroy()

    def startInstruction(self):
        """
        Zeigt die Anleitung an, wenn der User auf "Anleitung" drücktt.
        """
        self.packForgetMainPage()
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
        self.packMainPage()

    # --------------------------- Gegnerauswahl ---------------------------

    def selectOpponentPage(self):
        """
        Hier kann der Spieler entscheiden, ob er gegen den Computer spielen möchte
        oder gegen einen anderen Spieler.
        """
        self.packForgetMainPage()
        self.packOpponentPage()

    def prepareSelectOpponentPage(self):
        """
        Hier werden die Widgets vorbereitet, sodass sie nur noch aufgerufen werden müssen.
        Wichtige Variablen:
        - opponentText (Überschrift)        type: Label
        - singlePlayer                      type: Button
        - twoPlayers                        type: Button
        - backFromSelectOpponentButton      type: Button
        """
        self.opponentText = Label(self.fenster,
                                  text="Wie viele Spieler?",
                                  bg="#444",
                                  fg="#55CC05",
                                  font=("Arial", 20, "italic"))

        self.opponentSelectButtonFrame = Frame(self.fenster,
                                               relief=RIDGE,
                                               bd=3,
                                               bg="#444")

        self.singlePlayer = Button(self.opponentSelectButtonFrame,
                                   text="1 Spieler",
                                   bg="#888",
                                   width=14,
                                   command=self.close)

        self.twoPlayers = Button(self.opponentSelectButtonFrame,
                                 text="2 Spieler",
                                 bg="#888",
                                 width=14,
                                 state="disabled",
                                 command=None)

        self.backFromSelectOpponentButton = Button(self.opponentSelectButtonFrame,
                                                   text="Zurück",
                                                   bg="#888",
                                                   width=10,
                                                   command=self.backFromOpponentPage)

    def backFromOpponentPage(self):
        """
        Bringt den User zurück zum Hauptmenü, von der Gegner-Auswahl-Seite.
        """
        self.packForgetOpponenPage()
        self.resetWindowSize()
        self.packMainPage()

    def packOpponentPage(self):
        """
        Hier werden die Widgets sichtbar gemacht, die zum Fenster für die
        Gegnerauswahl bestimmt sind.
        """
        self.fenster.geometry("%dx%d" % (320, 145))
        self.opponentText.pack(anchor=N, pady=5, padx=5, fill=X)
        self.opponentSelectButtonFrame.pack(anchor=CENTER, pady=5, padx=5, ipadx=0)
        self.singlePlayer.grid(row=1, column=0, padx=5, pady=5)
        self.twoPlayers.grid(row=1, column=1, padx=5, pady=5)
        self.backFromSelectOpponentButton.grid(row=2, columnspan=2, pady=5)

    def packForgetOpponenPage(self):
        """
        Die Widgets vom Fenster für die Gegnerauswahl werden unsichtbar gemacht.
        """
        self.opponentText.pack_forget()
        self.opponentSelectButtonFrame.pack_forget()


if __name__ == '__main__':
    start = GUI()
    mainloop()
