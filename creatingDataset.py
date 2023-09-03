import numpy as np
import pandas as pd
import pickle


df=pd.read_csv('Dataset1.csv',na_values='=')
labels=df['Prices']

data=df.copy()
data=data.dropna()

Dict={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
month_column=[]
for rr in data['Date']:
    str=rr
    str2=str.split('-')
    month_column.append(Dict[int(str2[1])])

season=[]
for it in month_column:
    if it=='January' or it=='February':
        season.append('winter')
    elif it=='March' or it=='April':
        season.append('spring')
    elif it=='May' or it=='June':
        season.append('summer')
    elif it=='July' or it=='August':
        season.append('monsoon')
    elif it=='September' or it=='October':
        season.append('autumn')
    elif it=='November' or it=='December':
        season.append('pre_winter')

seasons=[]
for it in season:
    if it=="winter":
        seasons.append(0)
    elif it=="spring":
        seasons.append(1)
    elif it=="summer":
        seasons.append(2)
    elif it=='monsoon':
        seasons.append(3)
    elif it=="autumn":
        seasons.append(4)
    elif it=="pre_winter":
        seasons.append(5)

names=[]
for it in data['Vegetable']:
    if it=='Potato':
        names.append(0)
    elif it=='Onion':
        names.append(1)
    elif it=='Tomato':
        names.append(2)
    elif it=='Lady_Finger':
        names.append(3)
    elif it=='Ginger':
        names.append(4)

states=[]
for it in data['State']:
    if it=='Delhi':
        states.append(0)
    elif it=='Dehradun':
        states.append(1)
    
availability=[]
for it in data['Availability']:
    if it=='Low':
        availability.append(0)
    elif it=='Moderate':
        availability.append(1)
    elif it=='High':
        availability.append(2)

demand=[]
for it in data['Demand']:
    if it=='Low':
        demand.append(0)
    elif it=='Moderate':
        demand.append(1)
    elif it=='High':
        demand.append(2)

data={
    'name':names,
    'season':seasons,
    'state':states,
    'availability':availability,
    'demand':demand
}

print(data)

print(labels)

data2=pd.DataFrame(data)
pickle.dump({'data':data2,'labels':labels},open('trainabledata.pickle','wb'))
print("done")