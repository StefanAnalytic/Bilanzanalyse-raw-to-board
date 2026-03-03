import subprocess
import sys
import time

print("="*60)
print("🚀 STARTE AUTOMATISIERTE BILANZANALYSE-PIPELINE")
print("="*60)

# Hier definieren wir die exakte chronologische Reihenfolge der Skripte
skripte = [
    "Kpi-rechner.py",           # Schritt 1: CSV-Daten berechnen
    "Dashboard_Trends.py",      # Schritt 2: Dashboards (PNGs) aus CSV zeichnen
    "erstelle_pdf_report.py"    # Schritt 3: PDF-Report aus den PNGs zusammenbauen
]

for skript in skripte:
    print(f"\n⏳ Führe aus: {skript} ...")
    time.sleep(1) # Kleine Pause für die Lesbarkeit im Terminal
    
    try:
        # sys.executable nutzt exakt dein aktives virtuelles Environment (venv)
        ergebnis = subprocess.run(
            [sys.executable, skript], 
            check=True, 
            capture_output=True, 
            text=True
        )
        
        # Gibt die originalen Erfolgsmeldungen deiner Skripte aus
        print(f"✅ ERFOLG: {skript} abgeschlossen.")
        # Wenn du die print-Ausgaben der Unterskripte sehen willst, entferne das '#' in der nächsten Zeile:
        # print(ergebnis.stdout.strip()) 
        
    except subprocess.CalledProcessError as e:
        # Falls ein Skript abstürzt, stoppt die Pipeline sofort und zeigt dir den Fehler
        print(f"❌ FEHLER in {skript}! Pipeline wird abgebrochen.")
        print(f"Fehlermeldung:\n{e.stderr}")
        sys.exit(1)

print("\n" + "="*60)
print("🎯 PIPELINE ERFOLGREICH BEENDET!")
print("Alle Daten, Dashboards und der Report sind auf dem neuesten Stand.")
print("="*60)