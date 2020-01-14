import pandas as pd
import json
from bokeh.models import ( ColumnDataSource, Circle, Legend)
from bokeh.plotting import figure, show, curdoc
from bokeh.layouts import widgetbox,  column
from bokeh.models.widgets import  Select

# load prediction result
pred_df = pd.read_csv('model/prediction.csv')
pred_df['Year-Month'] = pd.to_datetime(pred_df['Year-Month'])

# load steo 
steo = pd.read_csv('clean-data/steo.csv')
steo['Year-Month'] = pd.to_datetime(steo['Year-Month'])

# group by Regions and merge with prediction data
region_df = pred_df.groupby(['Year-Month','Regions'],as_index=False).sum()
region_df = region_df.merge(steo, on = ['Year-Month','Regions'])



# dictionary to map state name to state abbreviation
with open('us_state_abbrev.json') as f:
    us_state_abbrev = json.loads(f.read())

state_dict = us_state_abbrev 
state_dict.pop('Hawaii',None)
state_names = [*state_dict]
# dictionary to map sector names to their abbreviations
sector_dict = {'Residential':'RES',
               'Industrial':'IND', 'Commercial':'COM', 'Total':'ALL_no_OTH'}

def get_source(sector_name,state_name):
    '''
    return two bokeh columnar data sources for that sector, state and region
    '''
    sector = sector_dict[sector_name]
    #column to plot
    cols = ['Sale_'+sector,'Pred_'+sector, 'STEO_Sale_'+sector]
    # pick a state abbreviation 
    state = state_dict[state_name]

    # select the data dfs to plot
    data1 = pred_df[pred_df['State']==state]
    data1 = data1[cols[:2]+['Year-Month','Regions']]
    data1.columns = ['col1','col2','Year-Month','Regions']
    source1 = ColumnDataSource(data1)
    region = data1['Regions'].unique()[0]
    data2 = region_df[region_df['Regions']==region]
    data2 = data2[cols+['Year-Month']]
    data2.columns = ['col1','col2','col3','Year-Month']
    source2 = ColumnDataSource(data2)
    
    return ColumnDataSource(data1), ColumnDataSource(data2), region

# bokeh plot

# default sector and state
sector_name = 'Residential'
state_name = 'Alabama'
source1, source2, region = get_source(sector_name,state_name)
colors = ['#2c7fb8','#fec44f','#c51b8a']
    
#plot state 
p1 = figure(plot_width=700, plot_height=250, x_axis_type="datetime",tools="pan,box_zoom,reset",toolbar_location='above')
r0 = p1.line(source=source1, x='Year-Month', y='col1', color=colors[0],line_width=2)
r1 = p1.line(source=source1, x='Year-Month', y='col2', color=colors[1],line_width=2)
p1.title.text = sector_name +' electricity consumption for state: '+ state_name
p1.yaxis.axis_label = "(million kWh)"

legend = Legend(items=[
        ("Actual"   , [r0]),
        ("Predicted" , [r1]),], location="center")

p1.add_layout(legend,'right')
    
#plot region
p2 = figure(plot_width=700, plot_height=250, x_axis_type="datetime",x_range=p1.x_range,tools="pan,box_zoom,reset",toolbar_location='above')
r2 = p2.line(source=source2, x='Year-Month', y='col1', color=colors[0],line_width=2)
r3 = p2.line(source=source2, x='Year-Month', y='col2', color=colors[1],line_width=2)
r4 =p2.line(source=source2, x='Year-Month', y='col3', color=colors[2],line_width=2,line_dash=[4, 4])
p2.title.text = sector_name +' electricity consumption for Region: '+ region
p2.yaxis.axis_label = "(million kWh)"

legend = Legend(items=[
        ("Actual"   , [r2]),
        ("Predicted" , [r3]),
        ("STEO Prediction",[r4])], location="center")

p2.add_layout(legend,'right')

layout = column(p1,p2)
curdoc().add_root(layout)
