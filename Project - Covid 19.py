# PROJECT - COVID 19

## IMPORTING LIBRARIES 

import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
print ('Modules are imported')

### Loading the Dataset

dataset_url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df = pd.read_csv(dataset_url)

### Let's see the dataframe

df.head()
df.tail()

### Lets check the shape of the dataframe

df.shape

### Lets do some preprocessing

df = df[df.Confirmed > 0]

### Let's see the updated Dataframe

df.head()

### Lets see the data related to a country for example Italy

df[df.Country == 'Italy']

### Let's see Global spread of Covid 19

fig = px.choropleth(df, locations = 'Country', locationmode= 'country names', color = 'Confirmed', animation_frame='Date')
fig.show()
 
#### Let's see Global deaths of Covid19

fig = px.choropleth(df, locations = 'Country', locationmode= 'country names', color = 'Deaths', animation_frame='Date')
fig.update_layout(title_text = 'Global Deaths of Covid-19')
fig.show()

### Let's Visualize how intensive the Covid19 Transmission has been in each of the country

##### let's start with an example:

df_china = df[df.Country == 'China']
df_china.head()

df_china = df_china[['Date','Confirmed']]

df_china.head()

## calculating the first derivation of confrimed column

df_china['Infection Rate'] = df_china['Confirmed'].diff()
df_china.head()


px.line(df_china, x = 'Date', y = ['Confirmed', 'Infection Rate'], log_y=True)

df_china['Infection Rate'].max()

#### Let's Calculate Maximum infection rate for all of the countries

df.head()

countries = list(df['Country'].unique())
max_infection_rates = []
for c in countries :
    MIR = df[df.Country == c].Confirmed.diff().max()
    max_infection_rates.append(MIR)

#### let's create a new Dataframe 

df_MIR = pd.DataFrame()
df_MIR['Country'] = countries
df_MIR['Max Infection Rate'] = max_infection_rates
df_MIR.head()

#### Let's plot the barchart : maximum infection rate of each country

px.bar(df_MIR, x='Country', y = 'Max Infection Rate', color = 'Country', title = 'Global maximum infection rate', log_y=True)

### Let's See how National Lockdowns Impacts Covid19 transmission in Italy

### COVID19 pandemic lockdown in Italy 
On 9 March 2020, the government of Italy under Prime Minister Giuseppe Conte imposed a national quarantine, restricting the movement of the population except for necessity, work, and health circumstances, in response to the growing pandemic of COVID-19 in the country. <a href="https://en.wikipedia.org/wiki/COVID-19_pandemic_lockdown_in_Italy#:~:text=On%209%20March%202020%2C%20the,COVID%2D19%20in%20the%20country.">source</a>

italy_lockdown_start_date = '2020-03-09'
italy_lockdown_a_month_later = '2020-04-09'

df.head()

#### let's get data related to italy

df_italy = df[df.Country == 'Italy']
df_italy.head()

#### let's calculate the infection rate in Italy

df_italy['Infection Rate'] = df_italy.Confirmed.diff()
df_italy.head()

#### ok! now let's do the visualization

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


### Let's See how National Lockdowns Impacts Covid19 active cases in Italy

df_italy.head()

#### let's calculate number of active cases day by day 

df_italy['Deaths Rate'] = df_italy.Deaths.diff()
df_italy.head()

#### Now let's plot a line chart to compare COVID19 national lockdowns impacts on spread of the virus and number of active cases

fig = px.line(df_italy, x='Date', y = ['Infection Rate', 'Deaths Rate'])
fig.show()

#### Let's normalize the columns

df_italy['Infection Rate'] = df_italy['Infection Rate']/df_italy['Infection Rate'].max()
df_italy['Deaths Rate'] = df_italy['Deaths Rate']/df_italy['Deaths Rate'].max()

#### Let's plot the line chart again

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
