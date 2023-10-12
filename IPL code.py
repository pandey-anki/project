#Program for Data Analysis and Visualization on IPL Data
#importing the required libraries
import pandas as pd

#loading the ipl data from csv file to DataFrame object
ipl_data = pd.read_csv('IPL Matches.csv')

#showing the first five records of ipl dataset
ipl_data.head()

#finding the number of rows and columns in ipl dataset
ipl_data.shape

#Getting the information of all columns of ipl dataset
ipl_data.info()

#Getting total number of player of match awards
ipl_data['player_of_match'].value_counts()

#Getting top 5 players with most player of match awards
ipl_data['player_of_match'].value_counts()[0:5]

import matplotlib.pyplot as plt
import seaborn as sns

plt.title("Players of the matches")
plt.bar(list(ipl_data['player_of_match'].value_counts()[0:5].keys()),
list(ipl_data['player_of_match'].value_counts()[0:5]))
plt.show()

#Extracting records where team batting first won the match  
batting_first_data = ipl_data[ipl_data['result'] == 'runs']
batting_first_data.shape

#Finding how many times each team won batting first
batting_first_data['winner'].value_counts()

plt.title("Teams won matches batting first")
plt.bar(list(batting_first_data['winner'].value_counts()[0:3].keys()),
list(batting_first_data['winner'].value_counts()[0:3]),
color=['blue','yellow','purple'])
plt.show()

#Extracting records where team batting second won the match
batting_second_data = ipl_data[ipl_data['result'] == 'wickets']
batting_second_data.shape

#Finding out how many times each team won matches batting second
batting_second_data['winner'].value_counts()

plt.title("Teams won matches batting second")
plt.bar(list(batting_second_data['winner'].value_counts()[0:3].keys()),
list(batting_second_data['winner'].value_counts()[0:3]),
color=['purple','blue','yellow'])
plt.show()

list(batting_second_data['winner'].value_counts()[0:3])

list(batting_second_data['winner'].value_counts()[0:3].keys())

plt.title("Teams won matches batting second")
plt.pie(list(batting_second_data['winner'].value_counts()[0:3]),
labels=list(batting_second_data['winner'].value_counts()[0:3].keys()),
wedgeprops = {'edgecolor': 'black'}, autopct = '%.2f%%')
plt.show()