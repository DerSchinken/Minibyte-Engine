import os


def compiler(pfad, icon_pfad, onefile=True, icon=False):
    if onefile and bool(icon):
        os.system("pyinstaller -y -F " + icon_pfad + " " + pfad)
    elif onefile:
        os.system("pyinstaller -y -F " + pfad)
    elif not onefile and bool(icon):
        os.system("pyinstaller -y -i " + icon_pfad + " " + pfad)
    else:
        os.system("pyinstaller -y -F -i " + icon_pfad + " " + pfad)


pfad = str(input("Pfad zur datei (Wenn dieser compiler im selben\nordner"
                 " ist einfach nur datei name + endung eingeben)\n"
                 "und bitte bei jedem backslash noch eines dran hängen!! "))
icon = str(input("Icon? Wenn ja bitte pfad eintragen und wenn nicht einfach leer lassen "))
onefile = bool(input("Soll alles in nur eine Datei compiled werden? [True/False] "))
if onefile and bool(icon):
    compiler(pfad, icon, True, True)
elif not onefile and bool(icon):
    compiler(pfad, icon, False, True)
elif onefile:
    compiler(pfad, icon)
else:
    compiler(pfad, icon, False)
