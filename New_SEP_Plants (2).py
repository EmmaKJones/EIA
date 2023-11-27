#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


ft = pd.read_excel('C:/Users/EJones/Desktop/SEP_Python/CurrentFacilityTable.xlsx')
plants = pd.read_excel('C:/Users/EJones/Desktop/SEP_Python/2___Plant_Y2022.xlsx')
gen = pd.read_excel('C:/Users/EJones/Desktop/SEP_Python/3_1_Generator_Y2022.xlsx', 'Operable')


# In[3]:


#Merge Plants to Operable Generator Table
results = plants.merge(gen, how = 'left', left_on='Plant Code', right_on='Plant Code')


# In[9]:


#Identify list of plants already in the FacilityInfo table
indiplants = ft[['PlantCode', 'WUSurveyNumber','OnlineYear']]
indiplants.drop_duplicates()


# In[10]:


#Merge Plants/Generator Table with FacilityInfo plant table
all_results = results.merge(indiplants, how = 'left', left_on='Plant Code', right_on='PlantCode')
all_results


# In[6]:


#Find the length of each WUSurveyNo field. This is used to find those plants without a surveyno
all_results['Length'] = all_results['WUSurveyNumber'].astype(str).map(len)
all_results.to_excel('C:/Users/EJones/Desktop/SEP_Python/Results.xlsx')


# In[7]:


#Filter for Texas, 22, WUS Surveyed Technology, and plants without a SurveyNo
NewPlants = all_results.loc[(all_results['State_x']== 'TX') & (all_results['Primary Purpose (NAICS Code)']== 22)
& (all_results['Length'] == 3)
& 
((all_results['Technology'] == 'Conventional Steam Coal') | \
(all_results['Technology'] == 'Natural Gas Fired Combined Cycle') | \
 (all_results['Technology'] == 'Natural Gas Fired Combustion Turbine') | \
(all_results['Technology'] == 'Natural Gas Internal Combustion Engine') | \
(all_results['Technology'] == 'Natural Gas Steam Turbine') | \
(all_results['Technology'] == 'Nuclear'))]


# In[8]:


#Remove duplicates to get a list of plants to send to WUS
NewWUSPlants = NewPlants[['Plant Code', 'Plant Name_x','City',]]
NewWUSPlants.drop_duplicates().to_excel('C:/Users/EJones/Desktop/SEP_Python/NewPlants.xlsx')

