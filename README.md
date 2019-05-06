# Title: Predicting US Monthly Electricity Consumption 

The data are from the following sources:

Estimating the electricity consumption is an important part of energy planning. The Energy Information Administration (EIA) provides some estimations in their short-term energy outlook. However, the report focuses on fossil fuel consumptions and prices. The small electricity consumption section focuses on residential consumption. The goal of this project is to forecast monthly electricity consumption by state in three sectors: residential, commercial and industrial. These three sectors account for 98.5% of total electrical consumption. The consumption for each sector is predicted using a different machine learning model. The models use the number of electricity customer accounts, electricity prices, and economic data such as population by state, gross domestic product by state (GSP), and weather data. i.e. monthly heating and cooling days. Furthermore, since consumption is linearly correlated with sales revenue, the predicted consumption can be converted to sales revenue using the price of electricity. 


Monthly energy consumption, revenue, prices, and number of customer by sector by state since 1990 from https://www.eia.gov/electricity/data.php#sales, https://www.eia.gov/electricity/data/browser/, and https://www.eia.gov/electricity/sales_revenue_price/. The sectors are residential, commercial, transportation, and other. There are 50 states + 1 for DC.  
Population by state from https://fred.stlouisfed.org, example, https://fred.stlouisfed.org/series/ALPOP
Monthly number of heating and cooling days by state from https://www.ncdc.noaa.gov/ushcn/data-access. There are no data from Alaska. 
Monthly unemployment rate by state https://fred.stlouisfed.org. example , https://fred.stlouisfed.org/series/CAUR
Quarterly total personal income by state https://fred.stlouisfed.org, example, https://fred.stlouisfed.org/series/ALOTOT
Monthly consumer price index by state excluding food and electricity from https://fred.stlouisfed.org/series/CPILFENS
GSP  by state  from https://apps.bea.gov/regional/downloadzip.cfm and https://fred.stlouisfed.org 

Analysis Procedures: 

- Obtain data by downloading and using web API [notebook](https://github.com/worasom/energy_sale_rev/blob/master/api.ipynb)
- Extensive feature engineering, cross checking the accuracy and consistency of the data. Clean up the missing data [notebook](https://github.com/worasom/energy_sale_rev/blob/master/clean_energy_data.ipynb). The cleaned data has approximately 17000 rows, is about 13 MB in size, and can be found in [folder](https://github.com/worasom/energy_sale_rev/tree/master/clean-data). 
- Exploratory data analysis [notebook](https://github.com/worasom/energy_sale_rev/blob/master/EPA_energy_data.ipynb)
- Feature selection and built  machine learning models for the three sectors in [notebook](https://github.com/worasom/energy_sale_rev/blob/master/energy-ML.ipynb).

Explore relationship between the electricity sale and revenue. Since revenue follow a linear relationship with consumption with slope as retail price. Being able to predict the consumption also means predicting the revenue.

![](https://github.com/worasom/energy_sale_rev/blob/master/plots/fig1.png) 

The tree major sectors: residential, industrial and commercial accounts for 98.5% of the total consumption. The rest 1.5% are transportation and other sector. 
![](https://github.com/worasom/energy_sale_rev/blob/master/plots/fig2.png)

The dedogram below shows relationship among the fetures for the Residential sector. The population are highly correlated to the consumption. 

![](https://github.com/worasom/energy_sale_rev/blob/master/plots/fit3.png)

Similarly, population also highly correlated with the commercial consumption
![](https://github.com/worasom/energy_sale_rev/blob/master/plots/fit5.png)

Since all models consider state population as the most important feature, it is worth looking at the consumption per population for each state.

![](https://github.com/worasom/energy_sale_rev/blob/master/plots/plot1.png) 

The first plot shows average electricity consumption per capita by state in 2018, segmented into the consumption for the residential, industrial, and commercial sectors. Within each plot, the states are first grouped by regions, then sorted by the latitude of the state. For residential consumption, one might expect that electricity consumption would be higher in the northern states, because of the necessity of heating during their long, severe winters; however, the southern states actually top the electricity consumption charts.  This suggests that the number of days that requires air conditioning usage (number of cooling days) and regional information are likely important features in the model. For the industrial sector, the consumption also has a strong regional trend, against suggesting that regional information is an important feature for this sector. For the commercial sector, except for DC, the consumption is pretty uniform, thus the regional information is likely not important. 


## Machine Learning Models

Use random forest regressor to predict the electricity sale for each sector. After hyperparameter tuning, the model achieve 0.97 R-squared on the test set (15% of the data). 

The figure below shows features selected by the model for residential consumption.

![](https://github.com/worasom/energy_sale_rev/blob/master/plots/fig6.png)

The second model for industrial consumption achieves 0.95 R-squred. The figure below shows features selected by the model for industrial consumption.

![](https://github.com/worasom/energy_sale_rev/blob/master/plots/fig7.png)

The third model for commercial consumption achieves 0.93 R-squred. The figure below shows features selected by the model for industrial consumption.

![](https://github.com/worasom/energy_sale_rev/blob/master/plots/fig8.png)


## Model Performance 
I analyze the machine learning model performance by state. The prediction for the three sectors are summed together, and the R-squared score is calculated against the actual data. The overall R-squared is 0.97. 

![](https://github.com/worasom/energy_sale_rev/blob/master/plots/fig9.png)

However, when breaking down the performance of the model by state, the model best predicts the consumption in MS and NC, and worst prediction is in VT and NH. 

![](https://github.com/worasom/energy_sale_rev/blob/master/plots/fig10.png)

Time series plots shows the three best and the worse prediction. The actual data and the prediction for VT and NH are far apart.

![](https://github.com/worasom/energy_sale_rev/blob/master/plots/fig11.png)

Plotting the model performance on the map, we see that the model performs well on the southern states, which have high population and high consumption (blue). But the model prediction of the electricity consumption of the sparsely populated northern states is poor. I am working on improving the model performance for these states.

![](https://github.com/worasom/energy_sale_rev/blob/master/plots/plot2.png)

In summary, this project aims to predict monthly electricity consumption for each state in the US using population, weather, and economic data. Separate machine learning models are constructed for each of the three electricity consumption sectors (residential, industrial, and commercial). The preliminary models indicate good performance for southern states, but poor performance for northern states. After optimizing the models, I plan to build a web application to show the monthly forecast against the EIA forecast. 


