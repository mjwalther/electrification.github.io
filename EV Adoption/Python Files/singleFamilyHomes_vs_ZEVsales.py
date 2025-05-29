import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

dataset = "/Users/jiro/Desktop/Capstone/Data Sources/County_Level_Data_mar4.csv"
df = pd.read_csv(dataset)

df["Population"] = df["Population"].replace(r'[,]', '', regex=True).astype(float)
df["ZEV Sales per 1000"] = df["ZEV Sales"] / (df["Population"] / 1000)
df["Single Detached"] = df["Single Detached"].replace(r'[,]', '', regex=True).astype(float)
df["Single Family Homes per 1000"] = df["Single Detached"] / (df["Population"] / 1000)


plt.figure(figsize=(12, 7))
sns.scatterplot(data=df, x="Single Family Homes per 1000", y="ZEV Sales per 1000", 
                hue="COUNTY", palette="tab20", alpha=0.85, edgecolor="black", s=30)

plt.xlabel("Number of Single Family Homes per 1000 Residents")
plt.ylabel("ZEV Sales per 1000 Residents")
plt.title("ZEV Sales per 1000 Residents vs. # of Single Family Homes per 1000 Residents by County")

# Hide legend if too crowded
plt.legend([], [], frameon=False)

plt.grid(True)
plt.show()