#!/usr/bin/env python
# coding: utf-8

# Die Datei mit Coronazahlen aus dem Jahr 2020 öffnen

# In[8]:


import os
print(os.getcwd())


# In[39]:


filename = "/Users/kamillalauter/Datenanalyse/COVID-19-Todesfaelle_Deutschland.csv"
# Öffnen und Lesen der Datei
try:
    with open(filename, 'r') as file:
        for line in file:
            print(line)
except FileNotFoundError:
    print(f"Die Datei {filename} wurde nicht gefunden.")
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")


# In[40]:


import csv
with open("/Users/kamillalauter/Datenanalyse/COVID-19-Todesfaelle_Deutschland.csv") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)


# Nach der Ausgabe der Spaltenüberschriften wird deutlich, dass die Überschriften nicht mit einem KOmma, sondern einem Semikolon getrennt sind. Der Code wird angepasst

# In[41]:


import csv
with open("/Users/kamillalauter/Datenanalyse/COVID-19-Todesfaelle_Deutschland.csv") as f:
    reader = csv.reader(f, delimiter=',')  # Setzt das Trennzeichen auf Semikolon
    header = next(reader)
    for index, column_name in enumerate(header, start=1):
        print(f"{index}. {column_name}")


# Es gibt 5 Spalten in der  CSV-Datei. Wieviele Zeilen sind enthalten?

# In[42]:


import csv

# Pfad zur Datei
file_path = "/Users/kamillalauter/Datenanalyse/COVID-19-Todesfaelle_Deutschland.csv"

# Datei öffnen und Zeilen zählen
with open(file_path) as f:
    reader = csv.reader(f, delimiter=';')  
    next(reader)  # Überspringt den Header, um nur die Datenzeilen zu zählen
    row_count = sum(1 for row in reader)  # Zählt jede Zeile

print(f"Anzahl der Zeilen (ohne Header): {row_count}")


# Sind in allen Zellen Werte enthalten?

# In[43]:


import csv

# Pfad zur Datei
file_path = "/Users/kamillalauter/Datenanalyse/COVID-19-Todesfaelle_Deutschland.csv"

# Datei öffnen und jede Zelle prüfen
with open(file_path) as f:
    reader = csv.reader(f, delimiter=';')  # Achten Sie darauf, dass das richtige Trennzeichen verwendet wird
    header = next(reader)  # Liest den Header
    empty_cells = 0
    line_number = 1  # Startet die Zeilennummerierung nach dem Header
    for row in reader:
        line_number += 1
        for index, cell in enumerate(row):
            if cell == "":  # Überprüft, ob die Zelle leer ist
                print(f"Leere Zelle gefunden in Zeile {line_number}, Spalte {index + 1} ({header[index]})")
                empty_cells += 1

print(f"Überprüfung abgeschlossen. {empty_cells} leere Zellen gefunden.")


# In[55]:


import csv
import matplotlib.pyplot as plt

# Pfad zur CSV-Datei
file_path = "/Users/kamillalauter/Datenanalyse/COVID-19-Todesfaelle_Deutschland.csv"

# Listen für die Daten der Fälle und Todesfälle
faelle_gesamt = []
todesfaelle_gesamt = []

# CSV-Datei öffnen und Daten lesen
with open(file_path) as f:
    reader = csv.reader(f, delimiter=',')  # Verwendung von Komma als Trennzeichen
    header = next(reader)  # Header überspringen, um an die Daten zu gelangen
    for row in reader:
        if row[1] and row[2]:  # Prüft, ob die Zellen in Spalte 1 und 2 nicht leer sind
            faelle_gesamt.append(int(row[1]))  # Hinzufügen der Fallzahlen zur Liste
            todesfaelle_gesamt.append(int(row[2]))  # Hinzufügen der Todesfälle zur Liste

# Datenprüfung
print("Einige Datenpunkte für Fälle:", faelle_gesamt[:5])
print("Einige Datenpunkte für Todesfälle:", todesfaelle_gesamt[:5])

# Erstellen eines Liniendiagramms mit zwei Y-Achsen
fig, ax1 = plt.subplots(figsize=(10, 5))

color = 'tab:red'
ax1.set_xlabel('Zeit (Index der Datenpunkte)')
ax1.set_ylabel('Bestätigte Fälle', color=color)
ax1.plot(faelle_gesamt, color=color, label='Bestätigte Fälle gesamt')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # Zweite Y-Achse
color = 'tab:blue'
ax2.set_ylabel('Todesfälle', color=color)
ax2.plot(todesfaelle_gesamt, color=color, label='Todesfälle gesamt', linestyle='--')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # Layout anpassen, um Überlappungen zu vermeiden
plt.title('Verlauf der COVID-19 Fälle und Todesfälle in Deutschland')
fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
plt.show()




# In[56]:


# CSV-Datei öffnen und den spezifischen Wert lesen
with open(file_path) as f:
    reader = csv.reader(f, delimiter=',')  # Achten Sie darauf, das richtige Trennzeichen zu verwenden
    next(reader)  # Überspringt den Header
    first_row = next(reader)  # Liest die erste Zeile der Daten
    first_column_value = first_row[0]  # Erster Wert der ersten Zeile
    last_row =next(reader)
   

print(f"Der Wert der ersten Zeile und ersten Spalte ist: {first_column_value}")


# In[57]:


with open(file_path) as f:
    reader = csv.reader(f, delimiter=',')  # Stellen Sie sicher, dass das korrekte Trennzeichen verwendet wird
    next(reader)  # Überspringt den Header
    for row in reader:
        if row:  # Stellen Sie sicher, dass die Zeile nicht leer ist
            last_value_first_column = row[0]  # Aktualisiert den letzten Wert der ersten Spalte

print(f"Der Wert der letzten Zelle in der ersten Spalte ist: {last_value_first_column}")


# Den kompletten Zeitraum erfassen: Datumsangaben ausgeben 

# In[4]:


import csv

# Pfade zur CSV-Datei
file_path = '/Users/kamillalauter/Datenanalyse/COVID-19-Todesfaelle_Deutschland.csv'  # Ersetzen Sie dies mit dem tatsächlichen Dateipfad

# Listen zum Speichern der Werte der ersten und dritten Spalte
first_column_values = []
third_column_values = []

# CSV-Datei öffnen und Werte der ersten und dritten Spalte lesen
with open(file_path) as f:
    reader = csv.reader(f, delimiter=',')  # Achten Sie darauf, das richtige Trennzeichen zu verwenden
    next(reader)  # Überspringt den Header
    for row in reader:
        if row:  # Stellen Sie sicher, dass die Zeile nicht leer ist
            first_column_values.append(row[0])  # Fügt den Wert der ersten Spalte der Liste hinzu
            if len(row) >= 3:  # Überprüft, ob die dritte Spalte existiert
                third_column_values.append(row[2])  # Fügt den Wert der dritten Spalte der Liste hinzu

combined_columns = []

# CSV-Datei öffnen und Werte der ersten und dritten Spalte lesen und kombinieren
with open(file_path) as f:
    reader = csv.reader(f, delimiter=',')  # Achten Sie darauf, das richtige Trennzeichen zu verwenden
    next(reader)  # Überspringt den Header
    for row in reader:
        if row:  # Stellen Sie sicher, dass die Zeile nicht leer ist
            if len(row) >= 3:  # Überprüft, ob die dritte Spalte existiert
                combined_columns.append((row[0], row[2]))  # Fügt ein Tupel mit Werten aus der ersten und dritten Spalte hinzu

# Ausgabe aller kombinierten Werte
for first, third in combined_columns:
    print(f"{first}, {third}")


# In[ ]:


Die Daten sind für den Zeitraum 09.03.2020 bis 25.04.2024


# In[15]:


import csv
from datetime import datetime

# Pfade zur CSV-Datei
file_path = '/Users/kamillalauter/Datenanalyse/COVID-19-Todesfaelle_Deutschland.csv'  # Ersetzen Sie dies mit dem tatsächlichen Dateipfad

# Liste zum Speichern der kombinierten Werte der ersten und dritten Spalte am 31. März
march_31_data = []

# CSV-Datei öffnen und Werte der ersten und dritten Spalte lesen und kombinieren, wenn das Datum der 31. März ist
with open(file_path) as f:
    reader = csv.reader(f, delimiter=',')  # Achten Sie darauf, das richtige Trennzeichen zu verwenden
    next(reader)  # Überspringt den Header
    for row in reader:
        if row:  # Stellen Sie sicher, dass die Zeile nicht leer ist
            try:
                date = datetime.strptime(row[0], '%Y-%m-%d')
                if date.month == 12 and date.day == 31:
                    if len(row) >= 3:
                        march_31_data.append((row[0], row[2]))
            except ValueError as e:
                print(f"Fehler beim Parsen des Datums in Zeile: {row}, Fehler: {e}")

# Ausgabe aller kombinierten Werte vom 31. März
if march_31_data:
    for first, third in march_31_data:
        print(f"{first}, {third}")
else:
    print("Keine Daten für den 31. März gefunden.")



# Die Todeszahlen werden von Tag zu Tag summiert, deshalb müssen die Zahlen für die einzelnen Jahre berechnet werden.

# In[20]:


# Initialisierung der Liste, die die Tupel speichern wird
zahlen = []

# Erstes Jahr und zugehöriger Wert direkt hinzufügen
zahlen.append((2020, 33071))

# Berechnung des zweiten Wertes basierend auf Ihrer Formel
neu = 111925 - 33071
zahlen.append((2021, neu))

# Berechnung des dritten Wertes
neu2 = 162465 - neu - 33071
zahlen.append((2022, neu2))

# Berechnung des vierten Wertes
neu3 = 180109 - 33071 - neu - neu2
zahlen.append((2023, neu3))

# Ausgabe der Liste mit allen gespeicherten Tupeln
print(zahlen)


# In[8]:


filename = "/Users/kamillalauter/Datenanalyse/IfSG_Influenzafaelle.tsv"
# Öffnen und Lesen der Datei
try:
    with open(filename, 'r') as file:
        for line in file:
            print(line)
except FileNotFoundError:
    print(f"Die Datei {filename} wurde nicht gefunden.")
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")


# In[39]:


import pandas as pd

# Pfad zur Eingabedatei
input_file = '/Users/kamillalauter/Datenanalyse/IfSG_Influenzafaelle.tsv'

# Die Datei einlesen
try:
    data = pd.read_csv(input_file, sep='\t')
    print("Daten erfolgreich geladen.")
except Exception as e:
    print("Fehler beim Laden der Datei:", e)
    data = pd.DataFrame()  # Erstellt ein leeres DataFrame, falls das Laden fehlschlägt

# Jahr aus 'Meldewoche' extrahieren
data['Jahr'] = data['Meldewoche'].str.split('-').str[0]

# Filtern der Daten für 'Deutschland' und die Jahre 2020, 2021, 2022, 2023
filtered_data = data[(data['Region'] == 'Deutschland') & (data['Jahr'].isin(['2020', '2021', '2022', '2023']))]
print("Gefilterte Daten für Deutschland und die Jahre 2020-2023:")
print(filtered_data.head())  # Zeigt die ersten Zeilen der gefilterten Daten

# Pfad zur Ausgabedatei
output_file = '/Users/kamillalauter/Datenanalyse/IfSG_Influenzafaelle_Deutschland_2020_2023.tsv'

# Überprüfen, ob das DataFrame leer ist, bevor es gespeichert wird
if not filtered_data.empty:
    # Schreibe die gefilterten Daten in eine neue TSV-Datei
    filtered_data.to_csv(output_file, sep='\t', index=False)
    print("Die Daten wurden erfolgreich gefiltert und in", output_file, "gespeichert.")
else:
    print("Keine relevanten Daten für Deutschland für die Jahre 2020-2023 gefunden, nichts zu speichern.")



# In[81]:


import pandas as pd

# Laden der CSV-Datei
df = pd.read_csv('/Users/kamillalauter/Datenanalyse/COVID-19-Todesfaelle_Deutschland.csv')

# Konvertierung des 'Berichtsdatum' in ein Datumsformat
df['Berichtsdatum'] = pd.to_datetime(df['Berichtsdatum'])

# Filtern der Daten für den 31. Dezember jedes Jahres
df_filtered = df[df['Berichtsdatum'].dt.month == 12]
df_filtered = df_filtered[df_filtered['Berichtsdatum'].dt.day == 31]

# Gruppierung der Daten nach Jahr und Summierung der gesamten Todesfälle
df_filtered['Year'] = df_filtered['Berichtsdatum'].dt.year
deaths_per_year = df_filtered.groupby('Year')['Todesfaelle_gesamt'].sum()

print(deaths_per_year)


# In[29]:


# Laden der zweiten TSV-Datei
df_tsv = pd.read_csv('/Users/kamillalauter/Datenanalyse/aggregated_deaths_per_year.tsv', delimiter='\t')
df_tsv['Year'] = df_tsv['Jahr']  # Übernahme der Jahre direkt, ohne Konvertierung in Datetime

# Daten für 2022 vor der Aggregation anzeigen
print("Daten für das Jahr 2022:")
df_2022 = df_tsv[df_tsv['Year'] == 2022]
print(df_2022)


# In[37]:


import pandas as pd
import matplotlib.pyplot as plt

# Initialisierung der Liste, die die Tupel speichern wird
zahlen = []

# Erstes Jahr und zugehöriger Wert direkt hinzufügen
zahlen.append((2020, 33071))

# Berechnung des zweiten Wertes basierend auf Ihrer Formel
neu = 111925 - 33071
zahlen.append((2021, neu))

# Berechnung des dritten Wertes
neu2 = 162465 - neu - 33071
zahlen.append((2022, neu2))

# Berechnung des vierten Wertes
neu3 = 180109 - 33071 - neu - neu2
zahlen.append((2023, neu3))

# Umwandlung der Liste von Tupeln in ein DataFrame für einfacheres Plotten
df_zahlen = pd.DataFrame(zahlen, columns=['Year', 'Deaths'])
df_zahlen.set_index('Year', inplace=True)

# Ausgabe der aggregierten CSV-Daten
print("Aggregierte CSV-Daten:")
print(df_zahlen)

# Laden der zweiten TSV-Datei
df_tsv = pd.read_csv('/Users/kamillalauter/Datenanalyse/aggregated_deaths_per_year.tsv', delimiter='\t')
df_tsv['Year'] = df_tsv['Jahr']  # Übernahme der Jahre direkt, ohne Konvertierung in Datetime

df_tsv_filtered = df_tsv[df_tsv['Year'].isin([2020, 2021, 2022, 2023])]
deaths_per_year_tsv = df_tsv_filtered.groupby('Year')['Fallzahl'].sum()

# Ausgabe der aggregierten TSV-Daten
print("\nAggregierte TSV-Daten:")
print(deaths_per_year_tsv)

# Plotten der Daten
plt.figure(figsize=(10, 5))
plt.plot(df_zahlen.index, df_zahlen['Deaths'], label='CSV Data', marker='o')
plt.plot(deaths_per_year_tsv.index, deaths_per_year_tsv.values, label='TSV Data', marker='x')
plt.title('Todesfälle pro Jahr')
plt.xlabel('Jahr')
plt.ylabel('Todesfälle')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




