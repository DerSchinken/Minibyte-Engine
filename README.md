===============================================================================
# Minibyte-Engine  
By Dr.Bumm  
Webseite: http://index12.bplaced.net/  Ist in bearbeitung also bitte nicht so viel erwarten  
Dieses Projekt hat mir 1 Woche meiner Lebens zeit geraubt ich hoffe dieses Projekt gefällt dir   
___Die GUI ist in Entwicklung **!**___

Die main.exe ist ein Test spiel zur Demonstration nur in einer einzigen Datei   
Kompiliert mit pyinstaller  
Virus Scann zu der main.exe: https://www.virustotal.com/gui/file/ae8c30479109540271c43cb4287c07a3cfbbfc7a97692bed9a75fe7e1fcca5bf/detection  
  
Released:   
-  
Für Windows: 16.08.2019   
Für Linux: 24.08.2019   
Für Mac: Nicht getestet   
Für das Handy sollte es mit Android 5 und QPython3  
funktionieren. 
  
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
      'XF  PX',   
      'XXXXXX'    
      ]    
```
  
X = Wand   
P = Spieler  
F = Ziel  
Und space ist space (wow xD)  
was noch beachtet werden muss ist das:  
-die Zahl der elemente in einer reihe müssen gleich viele wie sein   
wie bei den anderen  
-Es muss eine gerade anzahl an elementen in einer reihe sein also  
keine 3 elemente sondern 4 keine 5 elemente sondern 6 usw.  
  
um dann der engine den befehl zu geben starte das Spiel müssen wir nur  
noch 
```python 
mnlp.start(lvl)
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
Irgendwann 2019 - Ki die das Level spielt                   
Auch irgendwann 2019 nur später als die KI - Gegner/Monster und GUI mit Multiplayer und Mehreren spielen insklusive rätsel (The very Big update)    
