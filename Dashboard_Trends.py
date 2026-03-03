import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Pfade definieren
csv_pfad = "/Users/stefanbechthold/Bilanzanalyse/AAPL_KPI_Analyse.csv"
export_ordner = "/Users/stefanbechthold/Bilanzanalyse/Dashboards_Trends"

print("Lese Daten und erstelle Trend-Dashboards...")

# 2. Daten laden
df = pd.read_csv(csv_pfad, index_col=0)

# 3. Spalten (Jahre) bereinigen und chronologisch sortieren
# Aus "2025-09-30 00:00:00" machen wir "2025"
neue_spalten = []
for col in df.columns:
    if "Unnamed" in col:
        continue
    jahr = str(col).split('-')[0]
    neue_spalten.append((col, jahr))

# Nur die relevanten Spalten behalten und umbenennen
df = df[[col[0] for col in neue_spalten]]
df.columns = [col[1] for col in neue_spalten]

# Die Jahre aufsteigend sortieren (z.B. 2021, 2022, 2023, 2024, 2025)
df = df.reindex(sorted(df.columns), axis=1)

# 4. Kategorien für die 4 Dashboards definieren
kategorien = {
    "1_Profitabilitaet": [
        "1. Gross Margin", "2. Operating Margin", "3. Net Profit Margin", 
        "4. Return on Equity (ROE)", "5. Return on Assets (ROA)"
    ],
    "2_Liquiditaet": [
        "6. Current Ratio (Liq. 3. Grades)", "7. Quick Ratio (Liq. 2. Grades)", 
        "8. Cash Ratio (Liq. 1. Grades)", "9. Working Capital"
    ],
    "3_Stabilitaet": [
        "10. Eigenkapitalquote", "11. Fremdkapitalquote", 
        "12. Verschuldungsgrad (Debt-to-Equity)", "13. Net Debt to EBITDA", 
        "14. Zinsdeckungsgrad (Interest Coverage)"
    ],
    "4_Effizienz": [
        "15. Operating Cash Flow Margin", "16. Free Cash Flow Margin", 
        "17. Cash Return on Assets", "18. CAPEX Quote", 
        "19. Anlagenintensität", "20. Kapitalumschlag (Asset Turnover)"
    ]
}

# 5. Export-Ordner erstellen
os.makedirs(export_ordner, exist_ok=True)

# 6. Diagramme zeichnen
for kat_name, kpi_liste in kategorien.items():
    # Nur KPIs nehmen, die auch im Datensatz existieren
    gueltige_kpis = [kpi for kpi in kpi_liste if kpi in df.index]
    anzahl_kpis = len(gueltige_kpis)
    
    if anzahl_kpis == 0:
        continue
        
    # Ein großes Dashboard mit x Unter-Diagrammen erstellen
    fig, axes = plt.subplots(anzahl_kpis, 1, figsize=(10, 3 * anzahl_kpis))
    fig.suptitle(f"DASHBOARD: {kat_name.split('_')[1].upper()} (5-Jahres-Trend)", fontsize=16, fontweight='bold')
    
    if anzahl_kpis == 1:
        axes = [axes]
        
    for i, kpi in enumerate(gueltige_kpis):
        ax = axes[i]
        
        # X-Werte (Jahre) und Y-Werte (KPI-Daten)
        x_werte = df.columns
        y_werte = df.loc[kpi].values
        
        # Liniendiagramm mit Markierungspunkten zeichnen
        ax.plot(x_werte, y_werte, marker='o', linestyle='-', linewidth=2, color='#2980b9', markersize=8)
        
        # Jeden Datenpunkt mit der genauen Zahl beschriften
        for x, y in zip(x_werte, y_werte):
            if not pd.isna(y):
                # Zahl etwas über dem Punkt platzieren
                ax.text(x, y + (max(y_werte)-min(y_werte))*0.05 if max(y_werte) != min(y_werte) else y+0.1, 
                        f"{round(float(y), 2)}", ha='center', va='bottom', fontsize=10, fontweight='bold')
        
        ax.set_title(kpi, fontsize=14, loc='left', color='#2c3e50')
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        # Y-Achse etwas Luft nach oben geben, damit die Zahlen nicht abgeschnitten werden
        y_min, y_max = ax.get_ylim()
        ax.set_ylim(y_min, y_max + (y_max - y_min) * 0.2)

    plt.tight_layout(rect=[0, 0.03, 1, 0.97])
    
    # Dashboard speichern
    dateiname = os.path.join(export_ordner, f"{kat_name}_Trend.png")
    plt.savefig(dateiname, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)

print(f"\nErfolg! Deine 4 Trend-Dashboards wurden hier gespeichert:\n{export_ordner}")