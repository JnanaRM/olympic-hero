# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)

#Code starts here
data.rename(columns={'Total':'Total_Medals'}, inplace=True)
data.head(10)


# --------------
#Code starts here




#Creating new column 'Better_Event'
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter')
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'] , 'Both', data['Better_Event'])

#Finding the value with max count in 'Better_Event' column
better_event=data['Better_Event'].value_counts().index.values[0]

#Printing the better event
print('Better_Event=', better_event)

    
#Code ends here    


# --------------
#Code starts here




top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
top_countries.drop(top_countries.index[-1],inplace = True)
def top_ten(df,col):
    country_list = []
    top_10 = df.nlargest(10, col)
    country_list = list(top_10['Country_Name'])
    return(country_list)

top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')

common = [i for i in top_10_summer if i in top_10_winter]
common = [i for i in common if i in top_10]
print(common)
    


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]


fig, (ax_1,ax_2,ax_3) = plt.subplots(3,1)
#plt.plot(kind='bar',summer_df['Country_Name'],summer_df['Total_Summer'],ax=ax_1)
#plt.bar(winter_df['Country_Name'],summer_df['Total_Winter'],ax=ax_2)
ax_1.bar(summer_df['Country_Name'],summer_df['Total_Summer'])
plt.xticks(rotation=45)
plt.xlabel('Country_Name')
plt.ylabel('Medal Count')

#plt.bar(winter_df['Country_Name'],summer_df['Total_Winter'],ax=ax_2)
ax_2.bar(winter_df['Country_Name'],winter_df['Total_Winter'])
plt.xticks(rotation=45)
plt.xlabel('Country_Name')
plt.ylabel('Medal Count')

#plt.bar(top_df['Country_Name'],summer_df['Total_Medals'],ax=ax_3)
ax_3.bar(top_df['Country_Name'],summer_df['Total_Medals'])
plt.xticks(rotation=45)
plt.xlabel('Country_Name')
plt.ylabel('Medal Count')

plt.show()
#plt.bar(winter_df.Country_Name,winter_df.Total_Winter,ax = ax_2)
#plt.bar(top_df.Country_Name,top_df.Total_Summer,ax = ax_3)


# --------------
#Code starts here



summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max() 
summer_country_gold = summer_df.loc[summer_df.Golden_Ratio.idxmax()]['Country_Name']

print(summer_max_ratio)
print(summer_country_gold)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max() 
winter_country_gold = winter_df.loc[winter_df.Golden_Ratio.idxmax()]['Country_Name']
print(winter_max_ratio)
print(winter_country_gold)

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max() 
top_country_gold = top_df.loc[top_df.Golden_Ratio.idxmax()]['Country_Name']
print(top_max_ratio)
print(top_country_gold)



# --------------
#Code starts here
data_1 = data.drop(data.index[-1])



data_1['Total_Points'] = data_1['Gold_Total'] * 3 + data_1['Silver_Total'] * 2 + data_1 ['Bronze_Total'] 
most_points = data_1.Total_Points.max()
print(most_points)
best_country = data_1.loc[data_1['Total_Points'].idxmax()]['Country_Name']
#winter_df.loc[winter_df.Golden_Ratio.idxmax()]['Country_Name']
print(best_country)


# --------------
#Code starts here
best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation = 45)


