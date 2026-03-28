#for the combine dataset, its 2000 to 2025 so cut out the first 15 years. only need 2015-2025
import pandas
#panda

#both of my data files
#draft= pandas.read_csv('finaldata.csv')
combine= pandas.read_csv('NFL_Combine_Since_2000.csv')
passdata = pandas.read_csv('passfinal.csv')
recdata = pandas.read_csv('recfinal.csv')
rushdata= pandas.read_csv('rushfinal.csv')
sackdata=pandas.read_csv('sackfinal.csv')
tackledata=pandas.read_csv('tacklefinal.csv')

#filter 2015
yearsy= combine['Year'] >=2015
combine = combine[yearsy]
#one file is int another is string so make them both int
y = 'year'
Y='Year'
#draft[y] =draft[y].astype(int)
combine[Y]=combine[Y].astype(int)
for stat in [passdata, recdata, rushdata, sackdata, tackledata]:
    print(stat.columns.tolist())
#removing all the suffixes so the names combine
combine['Player']= combine['Player'].str.removesuffix(' Jr.')
combine['Player']= combine['Player'].str.removesuffix(' II')
combine['Player']= combine['Player'].str.removesuffix(' III')
combine['Player']= combine['Player'].str.removesuffix(' IV')
combine['Player']= combine['Player'].str.removesuffix(' V')

#didnt want to write 50 lines so i made a loop to remove suffix
for suffix in [ ' Jr.', ' Sr.', ' II', ' III', ' IV', ' V']:
    recdata['name']=recdata['name'].str.replace(suffix, '', regex=False)
    rushdata['name']=rushdata['name'].str.replace(suffix, '', regex=False)
    sackdata['name']=sackdata['name'].str.replace(suffix, '', regex=False)
    tackledata['name']=tackledata['name'].str.replace(suffix, '', regex=False)
    passdata['name']=passdata['name'].str.replace(suffix, '', regex=False)

# normalize college names




#sort by max value to get each players best year. for ex JSN's jr year he played only 3 games, but as a sophomore he had 1600 yards
passdata = passdata.loc[passdata.groupby(['name'])['pass yards'].idxmax()]
recdata = recdata.loc[recdata.groupby(['name'])['rec yards'].idxmax()]
rushdata = rushdata.loc[rushdata.groupby(['name'])['rush yards'].idxmax()]
sackdata = sackdata.loc[sackdata.groupby(['name'])['Sacks'].idxmax()]
tackledata = tackledata.loc[tackledata.groupby(['name'])['Tackles'].idxmax()]




#dropping columns to avoid merge issues later
recdata = recdata.drop(columns=['year'])
rushdata = rushdata.drop(columns=['year'])
passdata = passdata.drop(columns=['year'])
sackdata = sackdata.drop(columns=['Year'])
tackledata = tackledata.drop(columns=['Year'])

recdata = recdata.drop(columns=['pos'])
rushdata = rushdata.drop(columns=['pos'])
passdata = passdata.drop(columns=['pos'])
sackdata = sackdata.drop(columns=['pos'])
tackledata = tackledata.drop(columns=['pos'])

recdata = recdata.drop(columns=['rank'])
rushdata = rushdata.drop(columns=['rank'])
passdata = passdata.drop(columns=['rank'])
sackdata = sackdata.drop(columns=['rank'])
tackledata = tackledata.drop(columns=['rank'])

recdata = recdata.drop(columns=['class'])
rushdata = rushdata.drop(columns=['class'])
passdata = passdata.drop(columns=['class'])
sackdata = sackdata.drop(columns=['class'])
tackledata = tackledata.drop(columns=['class'])

recdata = recdata.drop(columns=['college'])
rushdata = rushdata.drop(columns=['college'])
passdata = passdata.drop(columns=['college'])
sackdata = sackdata.drop(columns=['college'])
tackledata = tackledata.drop(columns=['college'])



#merge

combine = combine.rename(columns={'Player':'name', 'School':'college','Year':'year'})
Data = combine.merge(recdata, on=['name'], how='left')                
Data = Data.merge(rushdata, on=['name'], how='left')
Data = Data.merge(passdata, on=['name'], how='left')
Data = Data.merge(sackdata, on=['name'], how='left')
Data = Data.merge(tackledata, on=['name'], how='left')





Data = Data.sort_values(by='Pick')
Data.to_csv('MergedDraft.csv', index=False)