import pandas as pd

# Exemple de dictionnaire de données
data = {
    'Nom': ['Alice', 'Bob', 'Charlie', 'David'],
    'Âge': [25, 30, 28, 35],
    'Note': [85, 90, 88, 95]
}

# Conversion du dictionnaire en DataFrame
df = pd.DataFrame(data)

# Affichage du DataFrame
print(df)