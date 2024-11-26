# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 09:47:55 2021

@author: u6026797
"""
#%% libraries
import pandas as pd
import matplotlib.pyplot as plt
#from matplotlib import ticker
#%% data

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
covid_df = pd.read_csv(url, index_col=0)
print(covid_df.head())
pd.set_option('display.max_columns', None)
#see how this data looks
print(covid_df.head())
covid_df.info()
covid_df.columns
covid_df.describe()

#%% Instructions
'''
Overall instructions:
As described in the homework description, each graphic you make must:
   1. Have a thoughtful title
   2. Have clearly labelled axes 
   3. Be legible
   4. Not be a pie chart
I should be able to run your .py file and recreate the graphics without error.
As per usual, any helper variables or columns you create should be thoughtfully
named.
'''

#%% viz 1
'''
Create a visualization that shows all of the counties in Utah as a time series,
similar to the one shown in slide 22 during the lecture. The graphic should
-Show cases over time
-Have all counties plotted in a background color (something like grey)
-Have a single county plotted in a contrasting color (something not grey)
-Have well formatted dates as the X axis
'''
import matplotlib.dates as mdates
#Filter to just Utah in DF
utah_df = covid_df[covid_df['Province_State']=='Utah']
#Identify date columns in DF
date_cols = utah_df.columns[11:]
date_cols = date_cols.str.strip()
#Convert to datetime for better control of x-axis
date_range = pd.to_datetime(date_cols, format='%m/%d/%y')  
#see what this looks like
print(date_range[:5])
print(type(date_range))
#print(county_data[date_cols].head())
#Do for loop getting all counties (Admin2) in Utah and plotting the date columns for each county
for county in utah_df['Admin2'].unique():
    county_data = utah_df[utah_df['Admin2'] == county]
    #print a orange line for Davis county 
    if county == 'Davis':
        plt.plot(date_range, county_data[date_cols].values.flatten(), color='orange', label=county)
    #all other counties in gray 
    else:
        plt.plot(date_range, county_data[date_cols].values.flatten(), color='gray')

#Use an AutoDateLocator to place ticks appropriately and format as mmm yyyy
ax=plt.gca()
ax.xaxis.set_major_locator(mdates.AutoDateLocator())  
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

#define labels an titles and legend 
plt.xlabel('Date')
plt.ylabel('Number of cases')
plt.title('COVID-19 Data for Counties in Utah')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#%% viz 2
'''
Create a visualization that shows the contrast between the county in Utah with
the most cases to date to a county in Florida with the most cases to date.
The graphic should:
-Have only two counties plotted
-Highlight the difference between the two comparison counties
You may use any style of graphic you like as long as it is effective (dense)
and readable
'''
#create a copy of the covid_df for both utah and florida
utah_df = covid_df[covid_df['Province_State'] == 'Utah'].copy()
florida_df = covid_df[covid_df['Province_State'] == 'Florida'].copy()

#find the most recent date column to get the total cases to date
latest_date = date_cols[-1]

#get the total cases
utah_df['Total_Cases'] = utah_df[latest_date]
florida_df['Total_Cases'] = florida_df[latest_date]
#Print the most recent date and a sample of the updated DataFrame
print(f"The latest date is: {latest_date}")
print(utah_df[['Admin2', 'Total_Cases']].head())
print(florida_df[['Admin2', 'Total_Cases']].head())

#find county with most cases in each state
most_cases_utah = utah_df.loc[utah_df['Total_Cases'].idxmax(), 'Admin2']
most_cases_florida = florida_df.loc[florida_df['Total_Cases'].idxmax(), 'Admin2']
print(f"The county with the most cases is: {most_cases_utah}")
print(f"The county with the most cases is: {most_cases_florida}")

#create dataframe for counties with most cases
high_county_utah_df = utah_df[utah_df['Admin2'] == most_cases_utah]
high_county_fl_df = florida_df[florida_df['Admin2'] == most_cases_florida]
print(high_county_utah_df[['Admin2', 'Total_Cases']])
print(high_county_fl_df[['Admin2', 'Total_Cases']])

import matplotlib.pyplot as plt

#get the total cases for the highest county
utah_sl_cases = high_county_utah_df['Total_Cases'].iloc[0]
florida_md_cases = high_county_fl_df['Total_Cases'].iloc[0]

#create labels and values for the plot
counties = ['Utah - Salt Lake County', 'Florida - Miami Dade County']
cases = [utah_sl_cases, florida_md_cases]

#create the bar plot
plt.figure(figsize=(8, 6))
plt.bar(counties, cases, color=['purple', 'green'])

#add labels, title, and grid
plt.xlabel('County', fontsize=12)
plt.ylabel('Total COVID-19 Cases - (millions)', fontsize=12)
plt.title('Comparison of Total COVID-19 Cases in Salt Lake and Miami Dade Counties', fontsize=14)
plt.grid(axis='y', linestyle='--')

# Display the values above the bars
for i, value in enumerate(cases):
    plt.text(i, value + max(cases) * 0.02, f'{value:,}', ha='center', fontsize=10)

plt.tight_layout()
plt.show()

#%% viz 3
'''
Create a visualization that shows BOTH the running total of cases for a single
county AND the daily new cases. The graphic should:
-Use two y-axes (https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html)
-Use color to contrast the two series being plotted
-Have well formatted dates as the X axis
'''
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#print(date_cols)

#Convert to datetime for better control of x-axis
date_range = pd.to_datetime(date_cols, format='%m/%d/%y')  
print(date_range[:5])

#create dataframe for cumulative cases and daily cases for Davis county
davis_cty_cum_data = utah_df[utah_df['Admin2'] == 'Davis']
davis_daily = davis_cty_cum_data[date_cols].diff(axis=1)
#print(davis_cty_cum_data)
cum_y_values = davis_cty_cum_data[date_cols].iloc[0].values
dly_y_values = davis_daily[date_cols].iloc[0].values
#print(cum_y_values)

#define the figure and axis
fig, ax1 = plt.subplots()

#plot cumulative cases
color = 'tab:red'
#set titles and labels
plt.title('Daily versus Cumulative COVID-19 Cases for Davis County Utah', fontsize=14)
ax1.set_xlabel('Date ')
ax1.set_ylabel('Cumulative Total Cases', color=color)
#plot dates by cumulative values
ax1.plot(date_range, cum_y_values, color=color)
ax1.tick_params(axis='y', labelcolor=color)

#plot daily new cases
#put in a second axis to share both lines
ax2 = ax1.twinx()  
color = 'tab:blue'
ax2.set_ylabel('Daily New Cases', color=color) 
#plot dates by daily values
ax2.plot(date_range, dly_y_values, color=color)
ax2.tick_params(axis='y', labelcolor=color)

#set interval to 6 months to provide enough room on bottom of graph
ax2.xaxis.set_major_locator(mdates.MonthLocator(interval=6))  
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
#rotate axis to 45 degrees
ax2.tick_params(axis='x', rotation=45)

fig.tight_layout() 
fig.autofmt_xdate() 
plt.show()

#%% viz 4
'''
Create a visualization that shows a stacked bar chart of county contributions
to a given state's total cases. You may choose any state (or states).
(https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html#sphx-glr-gallery-lines-bars-and-markers-bar-stacked-py)
The graphic should:
-Have a single column delineate a state
-Have each 'slice' or column compontent represent a county
'''
#get the most recent date column which contains total
cumulative_totals = utah_df[date_cols].columns[-1]

#group by county (Admin2) and extract the total cases for the most recent date
county_cases = utah_df.groupby('Admin2')[cumulative_totals].sum()
print(county_cases)

#column define for cumulative cases
latest_col = date_cols[-1]
#initialize a dictionary to store county cases
county_cases_dict = {}

#populate dictionary with county names and their total cases
for county, total_cases in utah_df.groupby('Admin2')[latest_col]:
    county_cases_dict[county] = total_cases.sum()
print(county_cases_dict)

#create a new dictionary with an "Other" category for cases under 25000
threshold = 25000  #define a threshold
filter_cases_dict = {}  #store grouped cases
other_total = 0  #keep track of "other" counties

for county, total_cases in county_cases_dict.items():
    if total_cases >= threshold:
        #if cases exceed threshold - keep as is
        filter_cases_dict[county] = total_cases
    else:
        #if cases below the threshold -add to the "Other" 
        other_total += total_cases

#add the "Other" category to the filtered dictionary
if other_total > 0:
    filter_cases_dict['Other'] = other_total

print(filter_cases_dict)

import matplotlib.pyplot as plt
import numpy as np

#list out the counties from the filtered dictionary
counties = list(filter_cases_dict.keys())
#list out the number cases for each from dictionary
covid_cases = list(filter_cases_dict.values())

# Colors for the bars using cmap
colormap = plt.colormaps["plasma"]
colors = [colormap(i / len(counties)) for i in range(len(counties))]

#get figure size
fig, ax = plt.subplots(figsize=(12,4))

#start out with zeros for plot
cumulative_cases = np.zeros(len(counties))

left = 0
for idx, (county, cases) in enumerate(zip(counties, covid_cases)):
    ax.barh(
        y=["Covid Cases"],
        width=[cases],
        color=colors[idx],
        label=county,
        left=left,
        )
    left += cases
    
#set titles and labels
ax.set_title('Total Covid Cases in Utah by County', fontsize=16)
ax.set_xlabel('Number Cases', fontsize=12)
ax.set_yticks([])
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{int(x):,}"))
ax.legend(
    loc='upper center', 
    bbox_to_anchor=(0.5, -0.15), 
    ncol=len(counties),
    title='Counties',
    frameon=False)

plt.tight_layout()
plt.show()


#%% extra credit (5 points)
'''
Use Seaborn to create a grouped box plot of all reported states. Each boxplot
should be a distinct state. Have the states ordered from most cases (FL) to fewest 
cases. (https://seaborn.pydata.org/examples/grouped_boxplot.html)
'''
