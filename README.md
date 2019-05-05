# Title: Predicting US Monthly Electricity Consumption 

The data are from the following sources:

Monthly energy consumption, revenue, prices, and number of customer by sector by state since 1990 from https://www.eia.gov/electricity/data.php#sales, https://www.eia.gov/electricity/data/browser/, and https://www.eia.gov/electricity/sales_revenue_price/. The sectors are residential, commercial, transportation, and other. There are 50 states + 1 for DC.  
Population by state from https://fred.stlouisfed.org, example, https://fred.stlouisfed.org/series/ALPOP
Monthly number of heating and cooling days by state from https://www.ncdc.noaa.gov/ushcn/data-access. There are no data from Alaska. 
Monthly unemployment rate by state https://fred.stlouisfed.org. example , https://fred.stlouisfed.org/series/CAUR
Quarterly total personal income by state https://fred.stlouisfed.org, example, https://fred.stlouisfed.org/series/ALOTOT
Monthly consumer price index by state excluding food and electricity from https://fred.stlouisfed.org/series/CPILFENS
GSP  by state  from https://apps.bea.gov/regional/downloadzip.cfm and https://fred.stlouisfed.org 

These data were obtained by downloading and using web API [notebook](https://github.com/worasom/energy_sale_rev/blob/master/api.ipynb). 