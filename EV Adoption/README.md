# California’s Transition to Electric Vehicles

Access / Duplicate Here: https://arcg.is/015bf80

**California’s Transition to Electric Vehicles** is an interactive, scrolly-telling dashboard built to help **residents**, **policymakers**, and **advocates** understand the evolving landscape of electric vehicle (EV) adoption across the state.

This tool aggregates **county-level data** to visualize the **environmental**, **social**, and **infrastructural** dimensions of the shift to zero-emission vehicles (ZEVs). A special focus is placed on **equity**, offering a lens into the disparities in EV access and charging infrastructure.

---

## Features

### EV Adoption Trends by County

- Interactive **choropleth map** displaying changes from **2021 to 2024**
- Hover and click to view detailed **county-level statistics**
- Highlights **regional disparities**, especially between **high- and low-income counties**

### EV Infrastructure Accessibility

- Visualizes the **distribution of public chargers** across **Bay Area counties**
- Identifies **infrastructure gaps** that may hinder EV adoption
- Supports understanding of how **access to chargers** correlates with **adoption rates**

### ZEV Equity Index

A composite index designed to measure each county’s relative standing in the ZEV transition, emphasizing **equitable access**.

**Formula:**
ZEV Equity Index = z(Income) + z(Chargers per Capita) + z(Share of Multi-Family Units)


- **Higher scores** reflect better structural support for ZEV adoption
- **Lower scores** indicate systemic barriers and areas needing targeted policy action
- Supports **data-informed prioritization** of equity investments

### Policy Landscape and Recommendations

- Overview of key **federal and state policies** related to ZEVs
- Summarizes:
  - **Incentive programs**
  - **Charger deployment initiatives**
  - **Equity-focused legislation**
- Provides **forward-looking recommendations** to:
  - Close EV adoption gaps
  - Expand charger accessibility
  - Promote a **just transition** to electrification

---

## Future Improvements

- **Expand** the ZEV Equity Index to include **all California counties**, beyond the Bay Area
- **Refine the index** by incorporating additional variables such as:
  - **Transportation costs**
  - **EV rebate accessibility**
  - **Average commute distances**
- **Integrate** an incentive calculator from a related project to help users estimate available EV rebates
- **Enhance the user interface** for smoother scrolling and visual clarity
- **Link relevant resources** on EV adoption, charging, and financial assistance
- Conduct deeper **policy analysis** to localize and strengthen the recommendations


---

## Repository Structure

### Folder: `EV Adoption`

#### data

- **Final Dataset/**
  - Contains a single curated `.csv` combining all key metrics by California county from **2021 to 2024**:
    - ZEV sales
    - Chargers per capita
    - Area median income
    - Population estimates
    - Housing breakdowns

- **Raw datasets:**
  - `2021_income_CA_counties.xlsx`, `2022_income_CA_counties.xlsx`, `2024_income_CA_counties.xlsx`
  - `2024_ev_infrastructure_data.csv`, `q3_20XX_EV_Chargers.csv`
  - `Housing_Information.xlsx`
  - `ev_data.csv` (ZEV sales by county)

#### Python Files

All scripts are documented and written using **pandas**, **matplotlib**, and **seaborn**.

- `ev_infrastructure_combined_data.py`  
  Merges and cleans all datasets into the final CSV.

- **Visualization scripts:**
  - `multiFamilyHomes_vs_ZEVsales.py`
  - `zev_vs_income.py`
  - `...` (other data visualizations)

#### Graphs

- Contains PNG outputs of the visualizations above.
- These plots helped shape the final dashboard design and focus.

---

## Data Sources

A document titled **`Data Sources`** in the main folder includes links and descriptions for each dataset used, such as:

- ZEV Sales by California County  
- Area Median Income  
- Population Estimates (2021–2024)  
- Public EV Charging Infrastructure  
- Housing Type Breakdowns  
- California County Shapefiles  

---

## Project Description

The **interactive dashboard** was built to show how electric vehicle adoption differs across counties in California. By emphasizing **equity indicators**, the project highlights both progress and remaining gaps in EV accessibility and infrastructure.

All graphs and data were developed in the **first phase** of the project. These insights guided the creation of the **ArcGIS-powered scrolly-telling dashboard** in the second phase.

