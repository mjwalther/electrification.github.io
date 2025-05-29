import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Load the CSV file
df = pd.read_csv("/Users/jiro/Desktop/Capstone/Data Sources/County_Level_Data_feb18.csv")

# Filter for the year 2024
df_2024 = df[df["Data Year"] == 2024].copy()

# Convert 'Median Income' to numeric
df_2024["Median Income"] = df_2024["Median Income"].replace('[\$,]', '', regex=True).astype(float)

# Convert 'Population' to numeric
df_2024["Population"] = df_2024["Population"].replace(',', '', regex=True).astype(float)
df_2024["Population"] = pd.to_numeric(df_2024["Population"], errors='coerce')

# ZEV Sales Per Capita
df_2024["ZEV Sales Per 1000 Residents"] = (df_2024["ZEV Sales"] / df_2024["Population"]) * 1000

# Scatter Plot
plt.figure(figsize=(12, 6))
plt.scatter(df_2024["Median Income"], df_2024["ZEV Sales Per 1000 Residents"], color='b', s=10)

for i, row in df_2024.iterrows():
    plt.text(row["Median Income"], row["ZEV Sales Per 1000 Residents"], row["COUNTY"], fontsize=6, ha='right')

# log scale to the y-axis
plt.yscale("log")

# Run regression on log-transformed ZEV Sales Per 1000 Residents
slope, intercept, _, _, _ = linregress(df_2024["Median Income"], np.log(df_2024["ZEV Sales Per 1000 Residents"]))

# Generate x-values
x_values = np.linspace(df_2024["Median Income"].min(), df_2024["Median Income"].max(), 100)

# Convert predictions back from log-scale
y_values = np.exp(slope * x_values + intercept)

# best fit line
plt.plot(x_values, y_values, color='red', linestyle='dashed', label="Best Fit Line")

plt.xlabel("Median Income ($)")
plt.ylabel("ZEV Sales Per 1000 Residents (Log Scale)")
plt.title("ZEV Sales Per 1000 Residents vs. Median Income (2024) [Log Scale]")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

plt.show()

""" 
# Distribution of ZEV Sales per 1000 residents: To check if log-scale is needed

plt.hist(df_2024["ZEV Sales Per 1000 Residents"], bins=30)
plt.xlabel("ZEV Sales Per 1000 Residents")
plt.ylabel("Frequency")
plt.title("Distribution of ZEV Sales Per 1000 Residents")
plt.show() """
