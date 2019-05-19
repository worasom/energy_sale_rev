# Predicting US Monthly Electricity Consumption by State

Estimating the electricity consumption is an important part of energy planning. The US’s Energy Information Administration (EIA) provides some estimations in their short-term energy outlook, [STEO](https://www.eia.gov/outlooks/steo/data/browser/). However, the report only provide regional electricity consumption and does not provide state-wise estimation. The goal of this project is to forecast monthly electricity consumption by state in three sectors: residential, commercial and industrial. These three sectors account for about 98.5% of total electrical consumption as shown below. 

![](plots/fig2.png)

The consumption for each sector is predicted using a different machine learning model. The models use the number of electricity customer accounts, electricity prices, and economic data such as population by state, gross domestic product by state (GSP), and weather data. i.e. monthly heating and cooling days. The ability to predict the electricity consumption, and the major contributing factors would not only help with infrastructure planning, economical projection, coming energy efficient products but also estimation of electricity sales revenue.  

The picture below shows monthly electricity consumption in each sector in California. Seasonal pattern is seen for all sectors. This means that the features must included features with similar seasonal patterns.

![](plots/fig12.png)

After gathering all the data, I work on cleaning up the data. Sometimes I obtained the same data from two places. I check the consistency of the data and the units. Checking the units are important because the same number are often reported in more than one places, but in different units (mega, million or billion). I also found some mistake on the website. The unit in STEO website is billion kilowatthours, but should  be be million kilowatt hours. The total monthly consumption for the US is around 300,000 million kWh which is about 10,000 kWh per day. If the unit in the STEO is really billion kWh, then the projection is off by 1000 times. 

Some of the data are not report monthly, thus I have to filling the missing data by forward fill (for the next phase of the project I will use interpolation). The electricity consumption data starts on Jan, 1990 to  Feb, 2019. There are 50 states + DC, but the data for weather data for Alaska and Hawaii are missing, thus omitted in this analysis.The GSP data end on October 2018. After removing the missing data, I end up with approximately 17000 rows, is about 13 MB in size. I allocate test set to be data starting on 2015.

I built three machine learning models for the three sectors. For each sector, I started with random forest regressor, split datasets into train, validation and test set by order of occurrence, then perform  feature selection using feature of importance. Then, I search for the best model and parameters in TPOT. At the end I got 0.98 - 0.99 r-square on each sector, which transfer to about 0.99 overall R-squared for the total consumption. STEO prediction has 0.9999 R-square (almost exact). Then I compare my time-series prediction to the actual consumption and short-term energy outlook report from EIA website. I deploy the time-series prediction on heroku app https://worasom-energy.herokuapp.com/app. In this app, a user can observe time-series prediction for the sector, and state they are interested in. 

In the next phase of the project, I plan to perform prediction for 2020 consumption. I plan to include confidence interval in the projection. This is achieve by first projecting all features required  by the models with linear autoregressive model. For the application, I will also improve the aesthetic for the applications, and include import informations. In term of model performance, I did some analysis and identify some states that the models have difficulty prediction their electricity consumptions. I will also try to improve the model performance for in these states, which might be achieved by creating separates model for these states. 

Note: the unit in STEO website is billion kilowatthours, but should  be be million kilowatt hours. The total monthly consumption for the US is around 300,000 million kWh which is about 10,000 kWh per day. If the unit in the STEO is really billion kWh, then the projection is off by 1000 times. 


## Table of Contents

1. [Data Sources](#sources)
2. [Analysis Procedure](#procedure)
3. [Data Clean Up](#cleanup) and Exploratory Data Analysis
4. [Data Relationship](#epa)
5. [Machine Learning Models](#ml)
6. [Model Performance](#performance)

## Data Sources<a id='sources'></a>

The data are from the following sources:

- Monthly energy consumption, revenue, prices, and number of customer by sector by state since 1990 from https://www.eia.gov/electricity/data.php#sales, https://www.eia.gov/electricity/data/browser/, and https://www.eia.gov/electricity/sales_revenue_price/. The sectors are residential, commercial, transportation, and other. There are 50 states + 1 for DC.  
- Population by state from https://fred.stlouisfed.org, example, https://fred.stlouisfed.org/series/ALPOP
- Monthly number of heating and cooling days by state from National Centers for Environmental Information, https://www.ncdc.noaa.gov/ushcn/data-access. There are no data from Alaska. 
- Monthly unemployment rate by state from Federal Reserve Bank of St. Louis, https://fred.stlouisfed.org. example , https://fred.stlouisfed.org/series/CAUR
- Quarterly total personal income by state https://fred.stlouisfed.org, example, https://fred.stlouisfed.org/series/ALOTOT
- Monthly consumer price index by state excluding food and electricity from https://fred.stlouisfed.org/series/CPILFENS
- GSP  by state  from U.S. Bureau of Economic Analysis (BEA), https://apps.bea.gov/regional/downloadzip.cfm and https://fred.stlouisfed.org 

## Analysis Procedure<a id='procedure'></a> 

- Obtain data by downloading and using web API [notebook](https://github.com/worasom/energy_sale_rev/blob/master/api.ipynb)
- Extensive feature engineering, cross checking the accuracy and consistency of the data. Clean up the missing data [notebook](https://github.com/worasom/energy_sale_rev/blob/master/clean_energy_data.ipynb). The cleaned data has approximately 17000 rows, is about 13 MB in size, and can be found in [folder](https://github.com/worasom/energy_sale_rev/tree/master/clean-data). 
- Exploratory data analysis [notebook](https://github.com/worasom/energy_sale_rev/blob/master/EPA_energy_data.ipynb)
- Feature selection and built  machine learning models for the three sectors in [notebook](https://github.com/worasom/energy_sale_rev/blob/master/energy-ML.ipynb).


## Data Clean Up<a id='cleanup'></a> [notebook](https://github.com/worasom/energy_sale_rev/blob/master/clean_energy_data.ipynb) and Explore Data [notebook](https://github.com/worasom/energy_sale_rev/blob/master/EPA_energy_data.ipynb)

The tree major sectors: residential, industrial and commercial accounts for 98.5% of the total consumption. The rest 1.5% are transportation and other sector. 


