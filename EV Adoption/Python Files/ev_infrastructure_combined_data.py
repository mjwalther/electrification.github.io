import pandas as pd

combined_data = "/Users/jiro/Desktop/Capstone/Data Sources/County_Level_Data_feb26.csv" 
ev_data = "/Users/jiro/Desktop/Capstone/Data Sources/q3_2021_EV_Chargers.csv"  # EV infrastructure data (only for 2023)

# Read the datasets
county_df = pd.read_csv(combined_data)  # ZEV sales (multiple years)
ev_data_df = pd.read_csv(ev_data)  # EV infrastructure data (only for 2023)

# Standardize county names
county_df["COUNTY"] = county_df["COUNTY"].str.strip().str.title()
ev_data_df["County"] = ev_data_df["County"].str.strip().str.title()

# Merge 2023 EV data into the county dataset
county_df = county_df.merge(ev_data_df, left_on="COUNTY", right_on="County", how="left")

# Drop redundant "County" column from EV dataset
county_df.drop(columns=["County"], inplace=True)

# Ensure that EV infrastructure data is only filled for 2023 rows, keeping others unchanged
for col in ev_data_df.columns:
    if col != "County":  # Avoid processing the county name column
        merged_col = col + "_y"  # Column name from ev_data_df
        original_col = col + "_x"  # Column name from county_df
        
        if merged_col in county_df.columns:  # Ensure column exists in merged dataset
            county_df[col] = county_df.apply(
                lambda row: row[merged_col] if row["Data Year"] == 2021 else row[original_col], axis=1
            )

# Drop temporary "_x" and "_y" columns created by merging
county_df.drop(columns=[col for col in county_df.columns if col.endswith("_x") or col.endswith("_y")], inplace=True)

# Save the updated dataset
county_df.to_csv("/Users/jiro/Desktop/Capstone/Data Sources/County_Level_Data_Feb26.csv", index=False)

print(county_df.head())
