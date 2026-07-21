# Dodavanje biblioteka
import pandas as pd

df = pd.read_csv("messagescsv.csv")

# Printovanje nekoliko redova radi upoznavanja sa podacima
print(df.head())

# Provera da li postoje nedostajuce vrednosti i ciscenje istih
print("\nMissing values per column:\n", df.isna().sum()) 
df = df.dropna()
print("\nMissing values per column after cleaning:\n", df.isna().sum()) 

# Prebacivanje vrednosti u mala slova u koloni "category"
df['category'] = df['category'].str.strip().str.lower()

# Zadrži samo redove gde je category 'spam' ili 'ham'
df = df[df['category'].isin(['spam', 'ham'])]
print("\nUnique values after filtering:\n", df['category'].unique())

# Sacuvaj novi ociscen dataset
df.to_csv("messagescsv_cleaned.csv", index=False)