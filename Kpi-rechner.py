import sqlite3
import pandas as pd
import numpy as np

# 1. Daten laden und vorbereiten
db_pfad = "/Users/stefanbechthold/Bilanzanalyse/AAPL_Finanzdaten.db"
conn = sqlite3.connect(db_pfad)

print("Lade Daten und berechne Kennzahlen...")

bilanz = pd.read_sql_query("SELECT * FROM BILANZ", conn).set_index('Unnamed: 0').T
guv = pd.read_sql_query("SELECT * FROM GUV", conn).set_index('Unnamed: 0').T
cf = pd.read_sql_query("SELECT * FROM CASHFLOW", conn).set_index('Unnamed: 0').T

conn.close()

bilanz = bilanz.apply(pd.to_numeric, errors='coerce')
guv = guv.apply(pd.to_numeric, errors='coerce')
cf = cf.apply(pd.to_numeric, errors='coerce')

kpi = pd.DataFrame(index=bilanz.index)
kpi.index.name = "Geschäftsjahr"

# --- PROFITABILITÄT ---
kpi['1. Gross Margin'] = guv['Gross Profit'] / guv['Total Revenue']
kpi['2. Operating Margin'] = guv['Operating Income'] / guv['Total Revenue']
kpi['3. Net Profit Margin'] = guv['Net Income'] / guv['Total Revenue']
kpi['4. Return on Equity (ROE)'] = guv['Net Income'] / bilanz['Stockholders Equity']
kpi['5. Return on Assets (ROA)'] = guv['Net Income'] / bilanz['Total Assets']

# --- LIQUIDITÄT ---
kpi['6. Current Ratio (Liq. 3. Grades)'] = bilanz['Current Assets'] / bilanz['Current Liabilities']
kpi['7. Quick Ratio (Liq. 2. Grades)'] = (bilanz['Current Assets'] - bilanz['Inventory']) / bilanz['Current Liabilities']
kpi['8. Cash Ratio (Liq. 1. Grades)'] = bilanz['Cash And Cash Equivalents'] / bilanz['Current Liabilities']
kpi['9. Working Capital'] = bilanz['Working Capital']

# --- STABILITÄT & VERSCHULDUNG ---
kpi['10. Eigenkapitalquote'] = bilanz['Stockholders Equity'] / bilanz['Total Assets']
kpi['11. Fremdkapitalquote'] = bilanz['Total Liabilities Net Minority Interest'] / bilanz['Total Assets']
kpi['12. Verschuldungsgrad (Debt-to-Equity)'] = bilanz['Total Liabilities Net Minority Interest'] / bilanz['Stockholders Equity']
kpi['13. Net Debt to EBITDA'] = bilanz['Net Debt'] / guv['EBITDA']
kpi['14. Zinsdeckungsgrad (Interest Coverage)'] = guv['EBIT'] / abs(guv['Interest Expense'])

# --- EFFIZIENZ & CASHFLOW ---
kpi['15. Operating Cash Flow Margin'] = cf['Operating Cash Flow'] / guv['Total Revenue']
kpi['16. Free Cash Flow Margin'] = cf['Free Cash Flow'] / guv['Total Revenue']
kpi['17. Cash Return on Assets'] = cf['Operating Cash Flow'] / bilanz['Total Assets']
kpi['18. CAPEX Quote'] = abs(cf['Capital Expenditure']) / guv['Total Revenue']
kpi['19. Anlagenintensität'] = bilanz['Net PPE'] / bilanz['Total Assets']
kpi['20. Kapitalumschlag (Asset Turnover)'] = guv['Total Revenue'] / bilanz['Total Assets']

# 3. Ergebnisse bereinigen und exportieren
kpi = kpi.round(4)
kpi_final = kpi.T

# --- NEU: CSV EXPORT ---
export_pfad = "/Users/stefanbechthold/Bilanzanalyse/AAPL_KPI_Analyse.csv"

# Wir nutzen to_csv. Wenn du die CSV in einem deutschen Excel öffnen willst, 
# könntest du hier sep=';' und decimal=',' hinzufügen. 
# Für die meisten Daten-Tools ist der Standard aber am besten.
kpi_final.to_csv(export_pfad)

print(f"Erfolg! Deine professionelle Analyse mit 20 KPIs wurde hier als CSV gespeichert:\n{export_pfad}")