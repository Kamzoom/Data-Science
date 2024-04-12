import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from collections import Counter
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Einlesen der Daten
with open('store_data.csv', 'r') as file:
    records = [line.strip().split(',') for line in file]

# Entfernen von Transaktionen mit nur einem Element
records = [transaction for transaction in records if len(transaction) > 1]

# Initialisieren des Transaction Encoders
encoder = TransactionEncoder()
transaction_array = encoder.fit(records).transform(records)
df = pd.DataFrame(transaction_array, columns=encoder.columns_)

# Häufige Itemsets finden mit einem geeigneten min_support
frequent_itemsets = apriori(df, min_support=0.03, use_colnames=True)

# Assoziationsregeln aus den häufigen Itemsets generieren
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.2)

# Anzeigen der Regeln
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

import networkx as nx
import matplotlib.pyplot as plt

def plot_sankey(rules, min_lift):
    # Filtern der Regeln für bessere Klarheit
    rules = rules[rules['lift'] >= min_lift]

    label_list = []
    source = []
    target = []
    value = []

    for i, rule in rules.iterrows():
        antecedent = ', '.join(rule['antecedents'])
        consequent = ', '.join(rule['consequents'])
        if antecedent not in label_list:
            label_list.append(antecedent)
        if consequent not in label_list:
            label_list.append(consequent)

        source.append(label_list.index(antecedent))
        target.append(label_list.index(consequent))
        value.append(rule['support'])

    # Erstellen des Sankey-Diagramms
    fig = go.Figure(data=[go.Sankey(
        node=dict(pad=15, thickness=20, line=dict(color="black", width=0.5), label=label_list),
        link=dict(source=source, target=target, value=value))])

    fig.update_layout(title_text="Sankey Diagram of Association Rules", font_size=10)
    fig.show()

# Annahme: 'rules' ist ein DataFrame, das die Assoziationsregeln enthält
plot_sankey(rules, min_lift=1.2)