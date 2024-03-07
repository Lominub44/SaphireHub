# sorry for german comments :(

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  # messagebox separat importieren
import requests
import os
import sys
import subprocess

# Funktion zum Herunterladen des Spiels
def download_spiel(spiel):
    try:
        # Bestimmen des Download-Pfads basierend auf dem Betriebssystem
        if sys.platform.startswith('win'):  # Windows
            download_pfad = os.path.join(os.environ['USERPROFILE'], '.saphire_games')
        elif sys.platform.startswith('darwin'):  # macOS
            download_pfad = os.path.join(os.path.expanduser('~'), '.saphire_games')
        elif sys.platform.startswith('linux'):  # Linux
            download_pfad = os.path.join(os.path.expanduser('~'), '.saphire_games')
        else:
            download_pfad = os.path.join(os.path.expanduser('~'), '.saphire_games')  # Standardpfad für unbekannte Systeme
        
        # Überprüfen, ob der versteckte Ordner existiert, und falls nicht, ihn erstellen
        if not os.path.exists(download_pfad):
            os.makedirs(download_pfad, exist_ok=True)

        spiel_name = spiel.url.split("/")[-1]  # Extrahiere den Spielnamen aus der URL

        # Anfrage an die URL senden und den Inhalt speichern
        response = requests.get(spiel.url)
        response.raise_for_status()  # Fehler werfen, wenn die Anfrage nicht erfolgreich ist

        # Spiel herunterladen und speichern
        with open(os.path.join(download_pfad, spiel_name), 'wb') as f:
            f.write(response.content)

        # Erfolgsmeldung anzeigen
        messagebox.showinfo("Download", f"{spiel.name} wurde erfolgreich heruntergeladen nach: {os.path.join(download_pfad, spiel_name)}")
    except Exception as e:
        # Fehlermeldung anzeigen, wenn ein Fehler auftritt
        messagebox.showerror("Fehler", f"Fehler beim Herunterladen von {spiel.name}: {str(e)}")

# Funktion zum Starten eines Spiels
def starte_spiel(spiel):
    try:
        # Pfad zum versteckten Ordner für die installierten Spiele
        if sys.platform.startswith('win'):  # Windows
            zielordner = os.path.join(os.environ['USERPROFILE'], '.saphire_games')
        elif sys.platform.startswith('darwin'):  # macOS
            zielordner = os.path.join(os.path.expanduser('~'), '.saphire_games')
        elif sys.platform.startswith('linux'):  # Linux
            zielordner = os.path.join(os.path.expanduser('~'), '.saphire_games')
        else:
            zielordner = os.path.join(os.path.expanduser('~'), '.saphire_games')  # Standardversteckter Ordner für unbekannte Systeme
        
        spiel_pfad = os.path.join(zielordner, spiel)
        
        if sys.platform.startswith('win'):  # Windows
            os.startfile(spiel_pfad)
        else:
            subprocess.run(spiel_pfad, shell=True)

    except Exception as e:
        # Fehlermeldung anzeigen, wenn ein Fehler auftritt
        messagebox.showerror("Fehler", f"Fehler beim Starten von {spiel}: {str(e)}")

# Klasse für ein Spiel
class Spiel:
    def __init__(self, name, beschreibung, url):
        self.name = name
        self.beschreibung = beschreibung
        self.url = url

# Funktion zum Anzeigen der Produktseite
def zeige_produktseite(spiel):
    produktseite = tk.Toplevel(root)
    produktseite.title(spiel.name)

    # Bildschirmbreite und -höhe ermitteln
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Fensterbreite und -höhe festlegen (etwas kleiner als das Hauptfenster)
    window_width = 600
    window_height = 400

    # x- und y-Koordinaten für das zentrierte Fenster berechnen
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # Produktseite-Einstellungen
    produktseite.geometry(f"{window_width}x{window_height}+{x}+{y}")

    tk.Label(produktseite, text=f"Name: {spiel.name}", font=("Helvetica", 18)).pack(pady=10)
    tk.Label(produktseite, text=f"Beschreibung: {spiel.beschreibung}").pack(pady=5)

    # Download-Button hinzufügen
    download_button = tk.Button(produktseite, text="Download", command=lambda: download_spiel(spiel))
    download_button.pack(pady=10)

# Beispiel-Spiel erstellen
spiel1 = Spiel("Spiel 1", "Eine aufregende Reise in eine fantastische Welt.", "https://github.com/Lominub44/SaphireHub/raw/main/snake_V0.0.3.exe")

# Funktion zum Anzeigen der Entdecken-Seite
def zeige_entdecken_seite():
    entdecken_frame = ttk.Frame(notebook)
    notebook.add(entdecken_frame, text="Entdecken")

    tk.Label(entdecken_frame, text="Entdecken Sie neue Spiele!", font=("Helvetica", 18)).pack(pady=10)
    tk.Button(entdecken_frame, text=spiel1.name, command=lambda: zeige_produktseite(spiel1)).pack(pady=5)

    # Anzeigen der Bibliothek-Seite nach der Entdecken-Seite
    zeige_bibliothek()

# Funktion zum Erstellen eines versteckten Ordners (nur für Windows)
def create_hidden_directory(directory):
    try:
        # Erstellen des versteckten Ordners
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        # Verstecken des Ordners
        if sys.platform.startswith('win'):  # Nur für Windows
            import ctypes
            FILE_ATTRIBUTE_HIDDEN = 0x02
            ctypes.windll.kernel32.SetFileAttributesW(directory, FILE_ATTRIBUTE_HIDDEN)
    except Exception as e:
        print(f"Fehler beim Erstellen oder Verstecken des Ordners: {str(e)}")

# Funktion zum Anzeigen der installierten Spiele in der Bibliothek
def zeige_bibliothek():
    # Überprüfen, ob die Bibliothek-Seite bereits hinzugefügt wurde
    if len(notebook.tabs()) < 3:
        bibliothek_frame = ttk.Frame(notebook)
        notebook.add(bibliothek_frame, text="Bibliothek")

        # Pfad zum versteckten Ordner für die installierten Spiele
        if sys.platform.startswith('win'):  # Windows
            zielordner = os.path.join(os.environ['USERPROFILE'], '.saphire_games')
        elif sys.platform.startswith('darwin'):  # macOS
            zielordner = os.path.join(os.path.expanduser('~'), '.saphire_games')
        elif sys.platform.startswith('linux'):  # Linux
            zielordner = os.path.join(os.path.expanduser('~'), '.saphire_games')
        else:
            zielordner = os.path.join(os.path.expanduser('~'), '.saphire_games')  # Standardversteckter Ordner für unbekannte Systeme

        # Überprüfen, ob der versteckte Ordner vorhanden ist
        if os.path.exists(zielordner):
            # Spiele im versteckten Ordner auflisten
            spiele = [datei for datei in os.listdir(zielordner) if os.path.isfile(os.path.join(zielordner, datei))]
            if spiele:
                tk.Label(bibliothek_frame, text="Ihre Bibliothek", font=("Helvetica", 18)).pack(pady=10)
                spiele_listbox = tk.Listbox(bibliothek_frame, width=50, height=10)
                for spiel in spiele:
                    spiele_listbox.insert(tk.END, spiel)
                spiele_listbox.pack(pady=5)
                start_button = tk.Button(bibliothek_frame, text="Starten", command=lambda: starte_spiel(spiele_listbox.get(tk.ACTIVE)))
                start_button.pack(pady=5)
            else:
                tk.Label(bibliothek_frame, text="Ihre Bibliothek ist leer!").pack(pady=10)
        else:
            tk.Label(bibliothek_frame, text="Der versteckte Ordner wurde nicht gefunden!").pack(pady=10)
            # Versteckten Ordner erstellen
            create_hidden_directory(zielordner)

# Hauptfenster erstellen
root = tk.Tk()
root.title("Saphire Hub")

# Bildschirmbreite und -höhe ermitteln
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Fensterbreite und -höhe festlegen
window_width = 800
window_height = 600

# x- und y-Koordinaten für das zentrierte Fenster berechnen
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Hauptfenster-Einstellungen
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.resizable(False, False)  # Fenstergröße nicht veränderbar

# Registerkarten erstellen
notebook = ttk.Notebook(root)

# Home-Seite
home_frame = ttk.Frame(notebook)
notebook.add(home_frame, text="Home")

# Packen des Notebook-Widgets
notebook.pack(expand=1, fill="both")

# Schließen des Hauptfensters, wenn das Fenster geschlossen wird
root.protocol("WM_DELETE_WINDOW", root.quit)

# Anzeigen der Entdecken-Seite
zeige_entdecken_seite()

# Hauptloop starten
root.mainloop()
