# Importer funksjonalitet for read, plot og beregninger
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

# Les inn data fra excel-fil
data = pd.read_excel("Kategori og painpoints.xlsx")

# Sjekk at dataene ble lest riktig ved å lese av de 10 første linjene
print(data.head(10))

# Summer antall pain point per produktområde
sum_per_po = data.groupby("Produktområde")["Antall"].sum()

# Print resultat
print("Antall pain points per produktområde:")
print(sum_per_po)

# Visualiser resultatene med labels horisontalt og grid
sum_per_po.plot(kind="barh")
plt.title("Antall pain points per produktområde")
plt.xlabel("Antall pain points")
plt.ylabel("Produktområde")
plt.grid(True)
plt.show()

# Konverter kolonnen "Antall" til et array
antall_array = data["Antall"].to_numpy()
print("Antall som NumPy-array:")
print(antall_array)

# Klassifiser risiko med en egendefinert funksjon
def risikoklasse(count):
    if count < 10:
         return "Lav risiko"
    elif count < 20:
         return "Medium risiko"
    else:
         return "Høy risiko"

# Bruk for-løkke for å klassifisere risiko per rad
risiko_liste = []
for ant in data["Antall"]:
    risiko_liste.append(risikoklasse(ant))

# Legg til risikoklassifiseringen i Dataframe
data["Risiko"] = risiko_liste

# Sjekk at Dataframe er oppdatert med ny kolonne
print("Oppdatert DataFrame med 'Risiko':")
print(data.head(10))

# Skriv data til fil
data.to_excel("Oppdatert_Kategori_og_painpoints.xlsx", index=False)
print("Data er lagret til 'Oppdatert_Kategori_og_painpoints.xlsx'")