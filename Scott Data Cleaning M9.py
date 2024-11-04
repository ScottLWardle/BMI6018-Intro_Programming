# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 18:15:07 2024

@author: scott
"""

#%% Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#%% Importing Data
flights_data = pd.read_csv(r'C:\Users\scott\Documents\BMI 6018\data\flights.csv')
flights_data.head(10)
weather_data_pd = pd.read_csv(r'C:\Users\scott\Documents\BMI 6018\data\weather.csv')
weather_data_np = weather_data_pd.to_numpy()
#%% Pandas Data Filtering/Sorting Question Answering
#use flights_data

#Question 1 How many flights were there from JFK to SLC? Int
#get df of just those that had JFK and SLC
q_1 = flights_data.loc[(flights_data['origin'] == 'JFK') & (flights_data['dest'] == 'SLC')]
#just the columns interested in
q_1_slim = q_1[['origin', 'dest']]
#get number of rows
num_flights = q_1_slim.shape[0]
print(num_flights)

#Question 2 How many airlines fly to SLC? Should be int
q_2 = flights_data.loc[flights_data['dest'] == 'SLC']
to_slc = q_2.shape[0]
print(to_slc)

#Question 3 What is the average arrival delay for flights to RDU? float
q_3 = flights_data.loc[flights_data['dest'] == 'RDU']
RDU_delay = q_3['arr_delay'].mean()
print(RDU_delay)

#Question 4 What proportion of flights to SEA come from the two NYC airports (LGA and JFK)?  float
dest_SEA = flights_data.loc[flights_data['dest'] == 'SEA']
from_NYC = dest_SEA.loc[(dest_SEA['origin'] == 'LGA') | (dest_SEA['origin'] == 'JFK')]
from_NYC
q_4 = float(from_NYC.shape[0]/dest_SEA.shape[0])
print(q_4)

#Question 5 Which date has the largest average depature delay? Pd slice with date and float
#please make date a column. Preferred format is 2013/1/1 (y/m/d)
flights_data
flights_data['date']=flights_data['year'].astype(str) + '/' + flights_data['month'].astype(str) + '/' + flights_data['day'].astype(str)
new_flight_data = flights_data.groupby('date')['dep_delay'].mean()
new_flight_data
q_5_date = new_flight_data.idxmax()
q_5_value = new_flight_data.max()

print(f'The date with the largest average departure date delay is {q_5_date} with a time of {q_5_value}')

#Question 6 Which date has the largest average arrival delay? pd slice with date and float
new_flight_data2 = flights_data.groupby('date')['arr_delay'].mean()
q_6_date = new_flight_data2.idxmax()
q_6_value = new_flight_data2.max()
print(f'The date with the largest average arrival date delay is {q_6_date} with a time of {q_6_value}')

#Question 7 Which flight departing LGA or JFK in 2013 flew the fastest? pd slice with tailnumber and speed
#speed = distance/airtime
LGA_JFK_depart = flights_data.loc[(flights_data['origin'] == 'LGA') | (flights_data['origin'] == 'JFK')]
LGA_JFK_depart 
LGA_JFK_depart.loc[:,'speed'] = LGA_JFK_depart['distance'] / (LGA_JFK_depart['air_time'] / 60)
sorted_LGA_JFK_depart = LGA_JFK_depart.sort_values(by='speed', ascending=False)
# Get the first row, which has the maximum speed
q_7_max_speed_row = sorted_LGA_JFK_depart.iloc[0]

print(q_7_max_speed_row[['tailnum', 'speed']])

#Question 8 Replace all nans in the weather pd dataframe with 0s. Pd with no nans
weather_data_pd
q_8 = weather_data_pd.fillna(0) 
q_8

#%% Numpy Data Filtering/Sorting Question Answering
#Use weather_data_np
#Question 9 How many observations were made in Feburary? Int
weather_data_np
#observe that month is index 3 and month is an integer of 2
feb_data = weather_data_np[weather_data_np[:,3] == 2]
q_9 = len(feb_data)
print(q_9)
#Question 10 What was the mean for humidity in February? Float
q_10 = feb_data[:,8].mean()
print(q_10)
#Question 11 What was the std for humidity in February? Float
q_11 = feb_data[:,8].std()
print(q_11)
