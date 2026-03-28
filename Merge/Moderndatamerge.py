import pandas as pd

prospects= pd.read_csv('2026prospectcombine - qb.csv')
prospects = prospects.rename(columns={'Player':'name', 'School':'college','Year':'year'})
qbstats = pd.read_csv('2026qbprospects.csv')
wrtestats = pd.read_csv('2026wrprospects.csv')
rbstats=pd.read_csv('2026rbprospects.csv')
destats =pd.read_csv('2026deprospects.csv')
lbstats=pd.read_csv('2026lbprospects.csv')
espn=pd.read_csv('espntop26 - Sheet1.csv')


for suffix in [ ' Jr.',' Jr', ' Sr.', ' II', ' III', ' IV', ' V']:
    prospects['name']=prospects['name'].str.replace(suffix, '', regex=False)
    qbstats['name']=qbstats['name'].str.replace(suffix, '', regex=False)
    wrtestats['name']=wrtestats['name'].str.replace(suffix, '', regex=False)
    rbstats['name']=rbstats['name'].str.replace(suffix, '', regex=False)
    destats['name']=destats['name'].str.replace(suffix, '', regex=False)
    lbstats['name']=lbstats['name'].str.replace(suffix, '', regex=False)
    espn['name']=espn['name'].str.replace(suffix, '', regex=False)
    

qbstats = qbstats.loc[qbstats.groupby(['name'])['pass yards'].idxmax()]
wrtestats = wrtestats.loc[wrtestats.groupby(['name'])['rec yards'].idxmax()]
rbstats = rbstats.loc[rbstats.groupby(['name'])['rush yards'].idxmax()]
destats = destats.loc[destats.groupby(['name'])['Sacks'].idxmax()]
lbstats = lbstats.loc[lbstats.groupby(['name'])['Tackles'].idxmax()]


#dropping columns to avoid merge issues later
wrtestats = wrtestats.drop(columns=['year'])
rbstats = rbstats.drop(columns=['year'])
qbstats = qbstats.drop(columns=['year'])
destats = destats.drop(columns=['Year'])
lbstats = lbstats.drop(columns=['Year'])

wrtestats = wrtestats.drop(columns=['pos'])
rbstats = rbstats.drop(columns=['pos'])
qbstats = qbstats.drop(columns=['pos'])
destats = destats.drop(columns=['pos'])
lbstats = lbstats.drop(columns=['pos'])

wrtestats = wrtestats.drop(columns=['rank'])
rbstats = rbstats.drop(columns=['rank'])
qbstats = qbstats.drop(columns=['rank'])
destats = destats.drop(columns=['rank'])
lbstats = lbstats.drop(columns=['rank'])

wrtestats = wrtestats.drop(columns=['class'])
rbstats = rbstats.drop(columns=['class'])
qbstats = qbstats.drop(columns=['class'])
destats = destats.drop(columns=['class'])
lbstats = lbstats.drop(columns=['class'])

wrtestats = wrtestats.drop(columns=['college'])
rbstats = rbstats.drop(columns=['college'])
qbstats = qbstats.drop(columns=['college'])
destats = destats.drop(columns=['college'])
lbstats = lbstats.drop(columns=['college'])

prospects['name']=prospects['name'].str.strip()
espn['name']=espn['name'].str.strip()


#merge

Data = prospects.merge(wrtestats, on=['name'], how='left')                
Data = Data.merge(rbstats, on=['name'], how='left')
Data = Data.merge(qbstats, on=['name'], how='left')
Data = Data.merge(destats, on=['name'], how='left')
Data = Data.merge(lbstats, on=['name'], how='left')
Data = Data.merge(espn, on=['name'], how='inner')

#Data = Data.sort_values(by='Pick')
Data.to_csv('26MergedProspectsESPN.csv', index=False)


