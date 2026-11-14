import pandas as pd


df = pd.read_csv("aro_index.tsv" , sep = "\t")

print(df.shape)
print(df.columns)
print(df.head())


import matplotlib.pyplot as plt

mechanisms = df["Resistance Mechanism"].dropna()
mechanisms = mechanisms.str.split(";")
mechanisms = mechanisms.explode()
mechanisms = mechanisms.str.strip()
mechanism_counts = mechanisms.value_counts()
print(mechanism_counts)

mechanism_counts.plot(kind="barh")

plt.title("Resistance genes by Mechanism")
plt.xlabel("Number of genes")
plt.tight_layout()
plt.show()


drug_classes = df["Drug Class"].dropna()
drug_classes = drug_classes.str.split(";")
drug_classes = drug_classes.explode()
drug_classes = drug_classes.str.strip()

drug_counts = drug_classes.value_counts()
print(drug_counts.head(10))

top10 = drug_counts.head(10)
top10.plot(kind="bar")
plt.title(" Top 10 drug classes by number of resistance genes")
plt.ylabel("Number of genes")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

                      

    
