---
layout: default
---

# Predicting US Monthly Electricity Consumption by State

Estimating the electricity consumption is an important part of energy planning. The Energy Information Administration (EIA) provides some estimations in their short-term energy outlook. However, the report focuses on fossil fuel consumptions and prices. The small electricity consumption section focuses on residential consumption. The goal of this project is to forecast monthly electricity consumption by state in three sectors: residential, commercial and industrial. These three sectors account for 98.5% of total electrical consumption. The consumption for each sector is predicted using a different machine learning model. The models use the number of electricity customer accounts, electricity prices, and economic data such as population by state, gross domestic product by state (GSP), and weather data. i.e. monthly heating and cooling days. Furthermore, since consumption is linearly correlated with sales revenue, the predicted consumption can be converted to sales revenue using the price of electricity. 

## Table of Contents

1. [Data Sources](#sources)
2. [Analysis Procedure](#procedure)
3. [Data Clean Up](#cleanup) and [Exploratory Data Analysis]
4. [Data Relationship](#epa)
5. [Machine Learning Models](#ml)
6. [Model Performance](#performance)

## Data Sources<a id='sources'></a>

The data are from the following sources:

- Monthly energy consumption, revenue, prices, and number of customer by sector by state since 1990 from https://www.eia.gov/electricity/data.php#sales, https://www.eia.gov/electricity/data/browser/, and https://www.eia.gov/electricity/sales_revenue_price/. The sectors are residential, commercial, transportation, and other. There are 50 states + 1 for DC.  
- Population by state from https://fred.stlouisfed.org, example, https://fred.stlouisfed.org/series/ALPOP
- Monthly number of heating and cooling days by state from https://www.ncdc.noaa.gov/ushcn/data-access. There are no data from Alaska. 
- Monthly unemployment rate by state https://fred.stlouisfed.org. example , https://fred.stlouisfed.org/series/CAUR
- Quarterly total personal income by state https://fred.stlouisfed.org, example, https://fred.stlouisfed.org/series/ALOTOT
- Monthly consumer price index by state excluding food and electricity from https://fred.stlouisfed.org/series/CPILFENS
- GSP  by state  from https://apps.bea.gov/regional/downloadzip.cfm and https://fred.stlouisfed.org 

## Analysis Procedure<a id='procedure'></a> 

- Obtain data by downloading and using web API [notebook](https://github.com/worasom/energy_sale_rev/blob/master/api.ipynb)
- Extensive feature engineering, cross checking the accuracy and consistency of the data. Clean up the missing data [notebook](https://github.com/worasom/energy_sale_rev/blob/master/clean_energy_data.ipynb). The cleaned data has approximately 17000 rows, is about 13 MB in size, and can be found in [folder](https://github.com/worasom/energy_sale_rev/tree/master/clean-data). 
- Exploratory data analysis [notebook](https://github.com/worasom/energy_sale_rev/blob/master/EPA_energy_data.ipynb)
- Feature selection and built  machine learning models for the three sectors in [notebook](https://github.com/worasom/energy_sale_rev/blob/master/energy-ML.ipynb).


## Data Clean Up<a id='cleanup'></a> [notebook](https://github.com/worasom/energy_sale_rev/blob/master/clean_energy_data.ipynb) and Explore Data [notebook](https://github.com/worasom/energy_sale_rev/blob/master/EPA_energy_data.ipynb)

The tree major sectors: residential, industrial and commercial accounts for 98.5% of the total consumption. The rest 1.5% are transportation and other sector. 
![](https://github.com/worasom/energy_sale_rev/blob/master/plots/fig2.png)