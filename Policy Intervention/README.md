# EV Adoption at the Zip Code Level - Emily Tianshi

## Overview
This document outlines the process of cleaning, analyzing, and visualizing data on electric vehicle adoption at the ZIP-code level in California. The analysis was conducted using Python in Google Colab.

## Datasets
This project uses data aggregated from several sources. Below is a description of each dataset, how it was obtained, and how it was used.

### Dataset 1: ZipCodeToCounty.csv:
This dataset maps California ZIP codes to their corresponding counties and includes ZIP-level population estimates. Because ZIP codes do not align perfectly with county boundaries (some ZIP codes span multiple counties), this dataset provides an approximate ZIP-to-county mapping. Additionally, population data is incomplete, and many rows contain NaN values in the "Population" column. The dataset is an excerpt from [Rowzero’s national ZIP-to-county mapping](https://rowzero.io/workbook/2A115AA67BC134773EA77374/79?ref=zip-to-county), which includes additional county-level information for the entire United States.

### Dataset 2: ElectricVehicles2023.csv:
This dataset contains the number of light-duty electric vehicles registered in California ZIP codes in 2023. It uses data from the [California Energy Commission’s Zero Emission Vehicle and Infrastructure Statistics Dashboard](http://www.energy.ca.gov/zevstats), which originally includes vehicle data from 2010 to 2023. The original dataset covers Diesel, Gasoline, Hybrid, and Electric vehicles and is aggregated at both the ZIP and County levels.
For this project, I filtered the dataset to include only Battery Electric Vehicles (BEVs), Fuel Cell Electric Vehicles (FCEVs), and Plug-In Hybrid Electric Vehicles (PHEVs) from the year 2023. For more information on the source data, contact: mediaoffice@energy.ca.gov.

### Dataset 3: EVs_by_Zip.csv
This dataset was used to create a ZIP-code level dashboard in ArcGIS. It combines data from Dataset 1 (ZipCodeToCounty.csv) and Dataset 2 (ElectricVehicles2023.csv), filtered to include only records from 2023. A new column, EVs per Capita, was created by dividing the number of electric vehicles by the ZIP code population (Number of Vehicles / ZIP Code Population).

### Dataset 4: AGI_by_Zip_2022.csv:
To analyze the relationship between EV adoption and personal income by zip code, I used data on personal income tax in California. Data was pulled from California Data Portal’s dataset, [“Personal Income Tax Statistics By Zip Code.”](https://data.ca.gov/dataset/personal-income-tax-statistics-by-zip-code/resource/7091fcca-e695-49ab-aa44-6e0c6f49c9c1) The original dataset extends from 1992 to 2022 and contains information on tax returns, California AGI, Total Tax Liability, and coordinates, for each California zip code. I filtered the original dataset to only include information from the most recent year, 2022. 

### Dataset 5: ElectricVehicles2022.csv
This dataset contains the same type of information as Dataset 2 (ElectricVehicles2023.csv) and is sourced from the same [California Energy Commission dashboard](http://www.energy.ca.gov/zevstats). It includes electric vehicle registration data at the ZIP-code level for the year 2022.

## Data Analysis

### Zip_vs_County_Adoption_Rates.ipynb
This code takes in Dataset 1 (ZipCodeToCounty.csv) and Dataset 2 (ElectricVehicles2023.csv) to analyze the relationship between electric vehicle adoption rates at the zip code and county level. In addition to quantitative statistics about the datasets, the code also produces the following figures: “Zip vs County EV Adoption Rates,” “Top EV Adoption Outliers By Zip,” and “Top 10 Counties by Standard Deviation of EV Adoption.”

### Income_Based_Adoption_Curve.ipynb
This code takes in Dataset 4 (AGI_by_Zip_2022.csv) and Dataset 5 (ElectricVehicles2022.csv) to analyze the relationship between electric vehicle adoption and income. The code produces the figure, “EV Adoption vs. Income.”
