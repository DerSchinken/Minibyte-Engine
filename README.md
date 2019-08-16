===============================================================================
# Minibyte-Engine  
By Dr.Bumm  
Die main.exe ist das spiel nur in einer einzigen Datei   
Kompiliert mit pyinstaller  
Virus Scann zu der main.exe: https://www.virustotal.com/gui/file/ae8c30479109540271c43cb4287c07a3cfbbfc7a97692bed9a75fe7e1fcca5bf/detection  
  
Released:   
-  
16.08.2019    
  
Bedienung  
-  
Für das benutzen muss m,an erst mal mnlp importieren mit `from src import mnlp`  
mnlp ist die abkürzung für mainloop  
  
Das was wir als nächtes brauchen ist ein level auf dem man spielen kann  
Das erstellen wir so:  
`lvl = [`     
       `'XXXXXX',`      
       `'XF  PX',`   
       `'XXXXXX'`    
       `]`    
  
  
X = Wand   
P = Spieler  
F = Ziel  
Und space ist space (wow xD)  
was noch beachtet werden muss ist das:  
-die Zahl der elemente in einer reihe gleich viele wie sein   
müssen wie bei den anderen  
-Es muss eine gerade anzahl an elementen in einer reihe sein also  
keine 3 elemente sondern 4 keine 5 elemente sondern 6 usw.  
  
um dann der engine den befehl zu geben starte das Spiel müssen wir nur  
noch `mnlp.start(lvl)` Eingeben und schon kannst du dein erstes lvl spielen  
Ein kleines bsp. ist die main.py  
Viel spaß  
  
Falls du dein eigenes Spiel auch zu einer Exe kompilieren willst:  
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
irgendwann 2019 - Gegner/Monster  
irgendwann 2019 - Mehrere Spiele hinter einander  
