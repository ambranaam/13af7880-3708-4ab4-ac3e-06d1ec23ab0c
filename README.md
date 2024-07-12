# GCode Converter für die Mobi-C

Dies ist eine neu-Implementierung in Python des GCode-Converters des Mobi-C-Projekts.

Projektseite von Mobi-C: [https://github.com/MakeMagazinDE/Mobi-C](https://github.com/MakeMagazinDE/Mobi-C).

Der Original-Code ist ein "Autohotkey"-Skript, siehe [https://github.com/MakeMagazinDE/Mobi-C/tree/main/src](https://github.com/MakeMagazinDE/Mobi-C/tree/main/src).

Getestet mit Python 3.8 unter Windows.

Installation:
1. Alle Dateien dieses Projekts in einen Ordner kopieren.
2. Pfad zum Python-Interpreter in `TransformGCode.cmd` anpassen.
3. Im `SendTo`-Ordner (normalerweise `%APPDATA%\Microsoft\Windows\SendTo`) einen Link zur `TransformGCode.cmd` erzeugen, Name des Links z.B. `TransformGCode.lnk`.

Aufruf:
* Rechts-Click auf die zu konvertierende Datei
* `Send to` -> `TransformGCode` auswählen.

Das Ergebnis ist die konvertierte Datei (z.B. `orig.nc` wird zu `orig_manual.nc`), welche dann im selben Ordner liegt wie die Originaldatei.

