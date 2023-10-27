#!/usr/bin/env python
# coding: utf-8

# # PROJECT - COVID 19

# ## IMPORTING LIBRARIES 

# ### TASK 1

# In[ ]:





# In[63]:


import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
print ('Modules are imported')


# In[ ]:





# ## TASK 1.1

# ### Loading the Dataset

# In[64]:


dataset_url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df = pd.read_csv(dataset_url)


# In[65]:


df.head()


# In[66]:


df.tail()


# ### Lets check the shape of the dataframe

# In[67]:


df.shape


# ## TASK 2.1

# ### Lets do some preprocessing

# In[68]:


df = df[df.Confirmed > 0]


# In[69]:


df.head()


# In[70]:


### Lets see the data related to a country for example Italy


# In[71]:


df[df.Country == 'Italy']


# ### Let's see Global spread of Covid 19

# In[72]:


fig = px.choropleth(df, locations = 'Country', locationmode= 'country names', color = 'Confirmed', animation_frame='Date')
fig.show()


# ### Task 2.2 : Exercise 
# #### Let's see Global deaths of Covid19

# In[73]:


fig = px.choropleth(df, locations = 'Country', locationmode= 'country names', color = 'Deaths', animation_frame='Date')
fig.update_layout(title_text = 'Global Deaths of Covid-19')
fig.show()


# ### Task 3.1:
# #### Let's Visualize how intensive the Covid19 Transmission has been in each of the country
# ##### let's start with an example:

# In[74]:


df_china = df[df.Country == 'China']
df_china.head()


# In[75]:


df_china = df_china[['Date','Confirmed']]


# In[76]:


df_china.head()


# In[77]:


df_china['Infection Rate'] = df_china['Confirmed'].diff()
df_china.head()


# In[78]:


px.line(df_china, x = 'Date', y = ['Confirmed', 'Infection Rate'], log_y=True)


# In[79]:


df_china['Infection Rate'].max()


# ### Task 3.2:
# #### Let's Calculate Maximum infection rate for all of the countries

# In[80]:


df.head()


# In[81]:


countries = list(df['Country'].unique())
max_infection_rates = []
for c in countries :
    MIR = df[df.Country == c].Confirmed.diff().max()
    max_infection_rates.append(MIR)


# ### Task 3.3:
# #### let's create a new Dataframe 

# In[82]:


df_MIR = pd.DataFrame()
df_MIR['Country'] = countries
df_MIR['Max Infection Rate'] = max_infection_rates
df_MIR.head()


# #### Let's plot the barchart : maximum infection rate of each country

# In[83]:


px.bar(df_MIR, x='Country', y = 'Max Infection Rate', color = 'Country', title = 'Global maximum infection rate', log_y=True)


# ### Task 4: Let's See how National Lockdowns Impacts Covid19 transmission in Italy

# ### COVID19 pandemic lockdown in Italy 
# On 9 March 2020, the government of Italy under Prime Minister Giuseppe Conte imposed a national quarantine, restricting the movement of the population except for necessity, work, and health circumstances, in response to the growing pandemic of COVID-19 in the country. <a href="https://en.wikipedia.org/wiki/COVID-19_pandemic_lockdown_in_Italy#:~:text=On%209%20March%202020%2C%20the,COVID%2D19%20in%20the%20country.">source</a>

# In[84]:


italy_lockdown_start_date = '2020-03-09'
italy_lockdown_a_month_later = '2020-04-09'


# In[85]:


df.head()


# #### let's get data related to italy

# In[86]:


df_italy = df[df.Country == 'Italy']
df_italy.head()


# #### let's calculate the infection rate in Italy

# In[87]:


df_italy['Infection Rate'] = df_italy.Confirmed.diff()
df_italy.head()


# #### ok! now let's do the visualization

# In[88]:


fig = px.line(df_italy, x='Date', y= 'Infection Rate', title = "Before and After Lockdown in Italy")
fig.add_shape(
    dict(
        type="line",
        x0=italy_lockdown_start_date,
        y0=0,
        x1=italy_lockdown_start_date,
        y1=df_italy['Infection Rate'].max(),
        line = dict(color = 'red' , width = 1)
    )
)
fig.add_annotation(
    dict(
        x=italy_lockdown_start_date,
        y=df_italy['Infection Rate'].max(),
        text = 'Starting date of the lockdown'
    )
)

fig.add_shape(
    dict(
        type="line",
        x0=italy_lockdown_a_month_later,
        y0=0,
        x1=italy_lockdown_a_month_later,
        y1=df_italy['Infection Rate'].max(),
        line = dict(color = 'yellow' , width = 1)
    )
)
fig.add_annotation(
    dict(
        x=italy_lockdown_a_month_later,
        y=df_italy['Infection Rate'].max(),
        text = 'A month later'
    )
)
fig.show()


# ## Task 5: Let's See how National Lockdowns Impacts Covid19 active cases in Italy

# In[89]:


df_italy.head()


# #### let's calculate number of active cases day by day 

# In[90]:


df_italy['Deaths Rate'] = df_italy.Deaths.diff()
df_italy.head()


# #### Now let's plot a line chart to compare COVID19 national lockdowns impacts on spread of the virus and number of active cases

# In[91]:


fig = px.line(df_italy, x='Date', y = ['Infection Rate', 'Deaths Rate'])
fig.show()


# In[92]:


df_italy['Infection Rate'] = df_italy['Infection Rate']/df_italy['Infection Rate'].max()
df_italy['Deaths Rate'] = df_italy['Deaths Rate']/df_italy['Deaths Rate'].max()


# #### Let's plot the line chart again

# In[93]:


plt.figure(figsize = (16,16))
fig = px.line(df_italy, x='Date', y=['Infection Rate', 'Deaths Rate'])
fig.add_shape(
    dict(
        type="line",
        x0=italy_lockdown_start_date,
        y0=0,
        x1=italy_lockdown_start_date,
        y1=df_italy['Infection Rate'].max(),
        line = dict(color = 'red' , width = 1)
    )
)
fig.add_annotation(
    dict(
        x=italy_lockdown_start_date,
        y=df_italy['Infection Rate'].max(),
        text = 'Starting date of the lockdown'
    )
)

fig.add_shape(
    dict(
        type="line",
        x0=italy_lockdown_a_month_later,
        y0=0,
        x1=italy_lockdown_a_month_later,
        y1=df_italy['Infection Rate'].max(),
        line = dict(color = 'yellow' , width = 1)
    )
)
fig.add_annotation(
    dict(
        x=italy_lockdown_a_month_later,
        y=df_italy['Infection Rate'].max(),
        text = 'A month later'
    )
)
fig.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




