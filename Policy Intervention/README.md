# EV Adoption at the Zip Code Level - Emily Tianshi

## Overview
This document outlines the process of cleaning, analyzing, and visualizing data on electric vehicle adoption at the ZIP-code level in California. The analysis was conducted using Python in Google Colab.

## Datasets
This project uses data aggregated from several sources. Below is a description of each dataset, how it was obtained, and how it was used.

### Dataset 1: ZipCodeToCounty.csv:
This dataset maps California ZIP codes to their corresponding counties and includes ZIP-level population estimates. Because ZIP codes do not align perfectly with county boundaries (some ZIP codes span multiple counties), this dataset provides an approximate ZIP-to-county mapping. Additionally, population data is incomplete, and many rows contain NaN values in the "Population" column. The dataset is an excerpt from Rowzero’s national ZIP-to-county mapping, which includes additional county-level information for the entire United States.

### Dataset 2: ElectricVehicles2023.csv:
This dataset contains the number of light-duty electric vehicles registered in California ZIP codes in 2023. It uses data from the California Energy Commission’s Zero Emission Vehicle and Infrastructure Statistics Dashboard, which originally includes vehicle data from 2010 to 2023. The original dataset covers Diesel, Gasoline, Hybrid, and Electric vehicles and is aggregated at both the ZIP and County levels.
For this project, I filtered the dataset to include only Battery Electric Vehicles (BEVs), Fuel Cell Electric Vehicles (FCEVs), and Plug-In Hybrid Electric Vehicles (PHEVs) from the year 2023. For more information on the source data, contact: mediaoffice@energy.ca.gov.
