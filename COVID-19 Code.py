 #Program for Data Analysis on Covid-19 Data using Seaborn Library 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

covid_19_data = pd.read_csv('covid_19_india.csv')

covid_19_data.info()

covid_19_data = pd.read_csv('covid_19_india.csv', parse_dates=['Date'])

covid_19_data.info()

covid_19_data.isnull().sum()

covid_19_data = covid_19_data[['Date', 'State/UnionTerritory', 'Cured', 'Deaths', 'Confirmed']]
covid_19_data.head()

covid_19_data.columns = ['date', 'state', 'cured', 'deaths', 'confirmed']
covid_19_data.head()

maximum_confirmed_cases_on_a_day = covid_19_data[
covid_19_data['date'] == '2020-06-30']
maximum_confirmed_cases_on_a_day.head()

maximum_confirmed_cases_on_a_day =
maximum_confirmed_cases_on_a_day.sort_values(by='confirmed',ascending=False)
maximum_confirmed_cases_on_a_day

top_ten_states_confirmed_cases_data_on_a_day =
maximum_confirmed_cases_on_a_day[0:10]
top_ten_states_confirmed_cases_data_on_a_day

plt.figure(figsize=(15,10))
plt.title("Top Ten 10 States Confirmed Cases on a Day")
sns.barplot(x='state', y='confirmed',
data=top_ten_states_confirmed_cases_data_on_a_day)
plt.show()

maharashtra_covid_data = covid_19_data[covid_19_data.state == 'Maharashtra']
maharashtra_covid_data.shape

plt.figure(figsize=(15, 10))
plt.title("Maharashtra Covid-19 Confirmed Cases")
sns.lineplot(x='date', y='confirmed',
data=maharashtra_covid_data, color='green')
plt.show()