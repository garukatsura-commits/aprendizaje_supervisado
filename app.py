import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

# Rellenar valores nulos
df["Age"] = df["Age"].fillna(df["Age"].median())

plt.figure(figsize=(8,5))
sns.histplot(df["Age"], bins=20, kde=True, color="royalblue")

plt.title("Distribución de Edades de los Pasajeros")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")

plt.show()
