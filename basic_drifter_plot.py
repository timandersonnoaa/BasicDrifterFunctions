# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:06:59 2015

@author: Timothy
"""
#==============================================================================
# Below is code to plot the tracks of drifters with information stored in at a url.
#This code is set to read from the web address containing CCSCR's data from 2014, but another address can be placed in
#the () following the pd.read_csv command to see tracks from other drifters.

#==============================================================================
#import necessary modules
import pandas as pd
import matplotlib.pyplot as plt


#make headers for dataframe, to be used in next line
headerlist= ["deployment_ID", "drifter_ID", "month", "day", "hour", "sec", "frac_yr", 'lon', 'lat', 'depth (m)', 'col11']  

#make dataframe from online source using the pandas module and the headers from above:
data=pd.read_csv("http://www.nefsc.noaa.gov/drifter/drift_cscr_2014_1.dat" , names=headerlist , delimiter=r"\s+")

#make a list of unique deployment IDs, so that when plotting tracks we can see each track seperately:
unique_ids = pd.Series(data[:][ "deployment_ID"]).unique()

#plot lon lat pairs for each unique deployment ID:
for ID in unique_ids:
    plt.plot(data[data['deployment_ID']==ID]['lon'], data[data['deployment_ID']==ID]['lat'])
    
