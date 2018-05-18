
# coding: utf-8

# In[25]:


import csv
f = open("guns.csv","r")
gun_data = csv.reader(f)
data = list(gun_data)
print(data[:5])


# In[26]:


headers = data[:1]
data = data[1:]
print(headers)
print(data[:5])


# In[27]:


years = [row[1] for row in data]
year_counts = {}
for year in years:
    if year in year_counts:
        year_counts[year] += 1
    else:
        year_counts[year] = 1
print(year_counts)


# ## PROPER DATETIME EXAMPLE:
# import datetime
# 
# dates = [datetime.datetime(year=int(row[1]),month=int(row[2]),day=1) for row in data]
# 
# <table>
#     <tr>
#         <td><b>dates</b></td><td>variable for list</td>
#     </tr>
#     <tr>
#         <td><b>= [</b></td><td>begin list comprehension</td>
#     </tr>
#     <tr>
#         <td><b>int(row[1]), ..</b></td><td>extract date from current row, cast to int</td>
#     </tr>
#     <tr>
#         <td><b>for row in data</b></td><td>run the loop in data</td>
#     </tr> 
# </table> 
# ## See below for example

# In[60]:


import datetime

dates = [datetime.datetime(year=int(row[1]),month=int(row[2]),day=1) for row in data]
print(dates[:5])

date_counts = {}
for row in dates:
    if row in date_counts:
        date_counts[row] += 1
    else:
        date_counts[row] = 1
date_counts


# In[63]:


sex_counts = {} #row[5]
for row in data:
    if row[5] in sex_counts:
        sex_counts[row[5]] += 1
    else:
        sex_counts[row[5]] = 1
print(sex_counts)

race_counts = {} #row[7]
for row in data:
    if row[7] in race_counts:
        race_counts[row[7]] += 1
    else:
        race_counts[row[7]] = 1
race_counts


# In[103]:


census_raw_file = open("census.csv","r")
census_data = csv.reader(census_raw_file)
census = list(census_data)
print(census)


# In[156]:


mapping = {
    'Asian/Pacific Islander': int(census[1][14]) + int(census[1][15]),
    'Black': int(census[1][12]),
    'Native American/Native Alaskan': int(census[1][13]),
    'Hispanic': int(census[1][11]),
    'White': int(census[1][10])
}
race_per_hundredk = {}

for row in race_counts:
    race_per_hundredk[row] = int(race_counts[row]) / mapping[row] * 100000

race_per_hundredk
    


# In[170]:


intents = [row[3] for row in data]
races = [row[7] for row in data]
homicide_race_counts = {}

for i,race in enumerate(races):
    if intents[i] == "Homicide":
        if race in homicide_race_counts:
            homicide_race_counts[race] += 1
        else:
            homicide_race_counts[race] = 1
            
homicide_race_counts

