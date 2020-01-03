===============================================================================
# Minibyte-Engine  
By Dr.Bumm  
Webseite: http://index12.bplaced.net/  Ist in bearbeitung also bitte nicht so viel erwarten  
Dieses Projekt hat mir 2 Woche meiner Lebens zeit geraubt ich hoffe dieses Projekt gefällt dir   
~~___Die GUI ist in Entwicklung **!**___~~ **Wurde fürs erste aufs eisgelegt!!!**

Die main.exe ist ein Test spiel zur Demonstration nur in einer einzigen Datei   
Kompiliert mit pyinstaller  
Virus Scann zu der main.exe: 
https://www.virustotal.com/gui/file/f6341134069b2336e09160237e7b3e2fa0b1f84fda5df540fa13bcb32385214b/detection
Virus scann zu der Compiler.exe:
https://www.virustotal.com/gui/file/b710e8631bb5d252c535fa17b39c239284e3ceee8e83c0c9f5c1cd447614f0f5/details    
Der uncompilierte Compiler ist unter ´src´ zu finden
  
Released:   
-  
Für Windows: 16.08.2019   
Für Linux: 24.08.2019   
Für Mac: Nicht getestet   
Für das Handy sollte es mit Android 5 und QPython3  
funktionieren. Wobei ich das nicht empfehlen kann es sei denn ihr habt eine Tastatur angeschlossen
Last update: 27.12.2019 02:18
  
Bedienung  
-  
Für das benutzen muss man erst mal mnlp importieren mit 
```python
from src import mnlp
```  
mnlp ist die abkürzung für mainloop  
  
Das was wir als nächtes brauchen ist ein level auf dem man spielen kann  
Das erstellen wir so:  
```python
lvl = [     
      'XXXXXX',      
      'X   PX',     
      'XF  GX',     
      'XXXXXX'    
      ]    
```
  
X = Wand (wird als X dargestellt)  
P = Spieler (wird als + dargestellt)   
G = Monster/Gegner (wird als M dargestellt)      
Das Monster hat 4 leben und ist nicht veränderbar!    
F = Ziel (wird als : dargestellt) 
Und space ist space (wow xD)  
was noch beachtet werden muss ist das:  
-die Zahl der elemente in einer reihe müssen gleich viele wie sein   
wie bei den anderen  
-Es muss eine gerade anzahl an elementen in einer reihe sein also  
keine 3 elemente sondern 4 keine 5 elemente sondern 6 usw.  
Das wird allerdings bald gefixt!
  
um dann der engine den befehl zu geben starte das Spiel müssen wir nur  
noch 
```python 
mnlp.start(lvl) # Um bestimmte anzahl an leben hinzuzufügen einfach nach lvl die leben schreiben
# bsp:
#mnlp.start(lvl, 3) 
# Der default wert is 6
# wenn ihr die Ki euer lvl spielen lassen wollt dann macht einfach:
#mnlp.start(lvl, True)
# Die ki ist standart mässig deaktiviert!
```
Eingeben und schon kannst du dein erstes lvl spielen  
Ein kleines bsp. ist die main.py  
Viel spaß  
   
Falls du dein eigenes Spiel auch zu einer Exe kompilieren willst:    
Mach sicher das du pyinstaller hast wenn nicht dann öffne die     
Konsole indem du die Windows taste und r gleich zeitig drückst      
in dem Fenster was erscheint `cmd` tippst und danach Enter drückst   
Nun solltest du die CMD vor dir haben und dort führst du dann    
```python
pip install pyinstaller
``` 
oder
```python
pip3 install pyinstaller
```
aus. Nun solltest du die folgenden befehle   
ausführen können  
   
Für ein eine Datei:  
`pyinstaller -y -F  "Dateipfad zu der .py Datei"`  
Für mehrere Dateien:  
`pyinstaller -y  "Dateipfad zu der .py Datei"`  
Mit Mehreren Dateien und Icon:  
`pyinstaller -y -i "Dateipfad zu der .ico Datei" "Dateipfad zu der .py Datei"`  
Mit einer Datei und Icon:   
`pyinstaller -y -F -i "Dateipfad zu der .ico Datei"  "Dateipfad zu der .py Datei"`  

Geplante Updates
-                 
~~Auch irgendwann 2019 nur später als die KI - GUI mit Multiplayer und Mehreren spielen hintereinander insklusive rätsel (The very Big update)~~ ***Wurde aufs eisgelegt fürs erste***       
