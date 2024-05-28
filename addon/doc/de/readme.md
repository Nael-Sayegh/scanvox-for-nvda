# Scanvox für NVDA

* Autor: Nael Sayegh
* URL: [infos@nael-accessvision.com](mailto:infos@nael-accessvision.com)
* Laden Sie die [stabile Version][1] herunter;
* NVDA-Kompatibilität: 2021.3 und höher;
* [Quellcode auf GitHub][2];

# Präsentation

Dieses Add-on nutzt die Scanvox-Software zum Lesen Ihrer Papierdokumente. Es wurde mit Hilfe des Softwareentwicklers erstellt und erfordert keine zusätzliche Installation.

## Voraussetzungen

Um dieses Add-on nutzen zu können, müssen Sie einen USB-Scanner an Ihren Computer angeschlossen haben, der mit TWAIN oder WIA kompatibel ist, was bei den meisten Scannern der Fall ist.

## Wie es funktioniert

Um dieses Add-on zu verwenden, gehen Sie zum NVDA-Menü und wählen Sie dann Scanvox. In diesem Dialog können Sie einen Scan starten, indem Sie auf die Schaltfläche „Scannen“ klicken. Der Start des Scanvorgangs dauert einige Sekunden und am Ende des Scanvorgangs wird der gescannte Text automatisch vorgelesen. Sie können die automatische Wiedergabe deaktivieren, indem Sie zum NVDA-Einstellungsmenü und dann zur Kategorie „Scanvox für NVDA“ gehen. 

Drücken Sie alt+s, bis alle Seiten gescannt wurden. Sobald Sie fertig sind, können Sie die verschiedenen gescannten Seiten lesen, indem Sie Umschalt+Tab auf der Schaltfläche „Scannen“ drücken oder indem Sie Alt+T drücken, um auf einen Bearbeitungsbereich mit dem Inhalt aller Seiten zuzugreifen. Sie können die Datei auch speichern.
 
Wenn Sie die gescannten Seiten löschen möchten, um ein neues Dokument zu scannen, können Sie die Taste alt+l drücken, um alle gescannten Seiten abzubrechen.

Wenn Sie Scanvox beenden, werden alle gescannten Seiten verworfen.

### Tastaturkürzel

Das Add-on „Scanvox for NVDA“ kann von überall auf Ihrem Computer durch Drücken von nvda+alt+s gestartet werden. Diese Geste kann im Eingabegestendialog geändert werden.

## Änderungen

### Version 2024.05.07

  * Hinzufügung eines Entwickler-Update-Kanals für Übersetzer und zum Testen neuer Funktionen
  * Türkische Übersetzung hinzugefügt
  * Beim Speichern eines Word-Dokuments wird jede Seite als neue Seite in der Datei hinzugefügt.
  * Hinzufügen einer Nachricht im NVDA-Protokoll, um anzuzeigen, dass Scanvox geladen ist

### Version 2024.05.04

  * Verbesserung des Update-Systems
  * Aktualisierung der russischen Übersetzung
  * Korrektur der französischen Übersetzung
  * Es wurde ein Fehler behoben, der dazu führte, dass der Inhalt des Bearbeitungsbereichs beim Klicken auf die Schaltfläche „Löschen“ nicht gelöscht wurde
  * Platzieren Sie den Cursor automatisch am Anfang der gescannten Seite im Bearbeitungsbereich.
  * Hinzufügung der Seitenzahl oben auf jeder gescannten Seite im Bearbeitungsbereich
  * Verschieben des Scanvox-Menüs vom Werkzeugmenü in das Hauptmenü

### Version 2024.03.20

  * Hinzufügung einer tschechischen Übersetzung
  * Hinzufügung einer portugiesischen Übersetzung
  * Hinzufügung eines Bearbeitungsbereichs vor der Scan-Schaltfläche, der es ermöglicht, den gerade gescannten Text sofort zu lesen
  * Fügen Sie einen Parameter hinzu, um das automatische Lesen eines Dokuments zu deaktivieren/aktivieren. Gehen Sie zum NVDA-Einstellungsmenü und dann zu Scanvox für NVDA
  * Hinzufügung einer russischen Übersetzung

### Version 2024.01.10

  * Aktualisieren Sie die Systemmodifikation, um eine Schaltfläche „Was ist neu“ hinzuzufügen, die die Hilfe zu den neuen Funktionen der Version öffnet
  * Automatisches Lesen der gescannten Seite nach dem Scannen hinzugefügt
  * Hinzufügung eines Seitentrennzeichens in der Datei (20 Sternchen), um anzuzeigen, wann sich die Seite ändert

### Version 2024.01.03

  * Aktualisierte französische Hilfe

### Version 2023.12.29

  * Erste Version

[1]: https://github.com/Nael-Sayegh/scanvox-for-nvda/releases/download/2024.05.04/scanvox-2024.05.04.nvda-addon

[2]: https://github.com/Nael-Sayegh/scanvox-for-nvda