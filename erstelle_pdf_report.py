import os

# Pfade zu deinen Dashboards
pfad_profitabilitaet = "/Users/stefanbechthold/Bilanzanalyse/Dashboards_Trends/1_Profitabilitaet_Trend.png"
pfad_liquiditaet = "/Users/stefanbechthold/Bilanzanalyse/Dashboards_Trends/2_Liquiditaet_Trend.png"
pfad_stabilitaet = "/Users/stefanbechthold/Bilanzanalyse/Dashboards_Trends/3_Stabilitaet_Trend.png"
pfad_effizienz = "/Users/stefanbechthold/Bilanzanalyse/Dashboards_Trends/4_Effizienz_Trend.png"
export_pfad = "/Users/stefanbechthold/Bilanzanalyse/AAPL_Analyst_Report.html"

# HTML Template mit modernem, cleanem CSS
html_content = f"""
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>AAPL Financial Due Diligence</title>
    <style>
        body {{
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1000px;
            margin: 0 auto;
            padding: 40px 20px;
            background-color: #f9f9f9;
        }}
        .container {{
            background-color: #fff;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }}
        h1 {{
            color: #003366;
            border-bottom: 2px solid #003366;
            padding-bottom: 10px;
            font-size: 28px;
        }}
        h2 {{
            color: #003366;
            margin-top: 40px;
            font-size: 22px;
        }}
        .executive-summary {{
            background-color: #eef2f5;
            padding: 20px;
            border-left: 4px solid #003366;
            margin-bottom: 40px;
        }}
        .chart-container {{
            text-align: center;
            margin: 30px 0;
            background: #fff;
            padding: 20px;
            border: 1px solid #eee;
        }}
        img {{
            max-width: 100%;
            height: auto;
            max-height: 600px;
        }}
        .analysis-box {{
            margin-top: -10px;
            margin-bottom: 40px;
        }}
        ul {{
            margin-top: 5px;
        }}
        li {{
            margin-bottom: 10px;
        }}
    </style>
</head>
<body>

<div class="container">
    <h1>INSTITUTIONAL EQUITY RESEARCH: APPLE INC. (AAPL)</h1>
    <p><strong>Fokus:</strong> 5-Jahres-Trendanalyse (FY 2021-2025) | <strong>Klassifizierung:</strong> Asset-Light Monopol</p>

    <div class="executive-summary">
        <strong>Executive Summary:</strong> Die traditionelle Bilanzlehre greift bei Apple nicht. Optische Warnsignale (niedrige Liquiditätsgrade, scheinbare Überschuldung) sind hier Beweise extremer Marktdominanz. Apple nutzt ein strukturell negatives Working Capital, um sein operatives Geschäft von Zulieferern zinslos finanzieren zu lassen, während enorme Free Cashflows in die aggressive Reduktion von Eigenkapital (Buybacks) fließen. 
    </div>

    <h2>1. Profitabilität: Absolute Preissetzungsmacht</h2>
    <div class="chart-container">
        <img src="{pfad_profitabilitaet}" alt="Profitabilität Trend">
    </div>
    <div class="analysis-box">
        <ul>
            <li><strong>Margen-Expansion:</strong> Ein stetiger Anstieg der Gross Margin auf fast 47% belegt, dass Inflation und Lieferkettenkosten problemlos an Kunden weitergegeben werden.</li>
            <li><strong>ROA statt ROE:</strong> Der astronomische ROE (>150%) ist durch Aktienrückkäufe künstlich verzerrt. Maßgeblich ist der Return on Assets (ROA), der mit 31,1% in 2025 eine herausragende Verzinsung des Gesamtkapitals zeigt.</li>
        </ul>
    </div>

    <h2>2. Liquidität: Lieferantenfinanzierung als Waffe</h2>
    <div class="chart-container">
        <img src="{pfad_liquiditaet}" alt="Liquidität Trend">
    </div>
    <div class="analysis-box">
        <ul>
            <li><strong>Dominanz statt Illiquidität:</strong> Eine Current Ratio unter 1.0 ist hier kein Risiko, sondern ein Machtbeweis.</li>
            <li><strong>Negatives Working Capital:</strong> Mit bis zu -23 Mrd. USD (2024) Unterdeckung beweist Apple, dass es Cash von Kunden vereinnahmt, lange bevor es Lieferanten bezahlen muss. Das Tagesgeschäft bindet kein eigenes Kapital.</li>
        </ul>
    </div>

    <h2>3. Stabilität: Optische Überschuldung durch Financial Engineering</h2>
    <div class="chart-container">
        <img src="{pfad_stabilitaet}" alt="Stabilität Trend">
    </div>
    <div class="analysis-box">
        <ul>
            <li><strong>Die Eigenkapital-Illusion:</strong> Die geringe Eigenkapitalquote (~20%) ist das gewollte Resultat maximaler Kapitalrückführung an Aktionäre, keine operative Schwäche.</li>
            <li><strong>Wahre Schuldentragfähigkeit:</strong> Der "Net Debt to EBITDA" fiel auf 0.43x (2025). Apple könnte alle Nettoschulden aus dem operativen Gewinn von 5 Monaten vollständig tilgen. Ausfallrisiko: nahe Null.</li>
        </ul>
    </div>

    <h2>4. Effizienz: Die Asset-Light Maschine</h2>
    <div class="chart-container">
        <img src="{pfad_effizienz}" alt="Effizienz Trend">
    </div>
    <div class="analysis-box">
        <ul>
            <li><strong>Geringe Kapitalbindung:</strong> Die CAPEX-Quote liegt historisch bei winzigen 2,5% bis 3,0%. Kapitalintensive Produktion wird ausgelagert, das margenstarke IP verbleibt bei Apple.</li>
            <li><strong>Cash Conversion:</strong> Eine Free Cash Flow Margin von fast 24% (2025) verdeutlicht, dass fast ein Viertel jedes eingenommenen Dollars als reines, frei verfügbares Cash im Unternehmen landet.</li>
        </ul>
    </div>

</div>

</body>
</html>
"""

# Datei schreiben
with open(export_pfad, "w", encoding="utf-8") as file:
    file.write(html_content)

print(f"Erfolg! Der kompakte HTML-Report wurde erstellt:\n{export_pfad}")
print("Tipp: Gehe im Finder/Explorer einfach zu der Datei und mache einen Doppelklick darauf, um sie im Browser zu öffnen!")