#import pandas for df and sklearn to use with the df
import pandas as pd
import numpy
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_extraction.text import CountVectorizer
past = pd.read_csv('MergedDraft.csv')
pres = pd.read_csv('26MergedProspectsESPN.csv')
#dv
past = past.dropna(subset=['Pick'])
y = past['Pick']

#iv
x= past[['Position','college','Height','Weight','40-yd Dash','Vertical Jump','Bench Press','Broad Jump','3-Cone Drill','20-yd Shuttle','receptions','rec yards','Tds_x','carries','rush yards','YpC','Tds_y','CmpPct','pass yards','PTds','ints','P rating','Sacks','Tackles']]

#turn strings into readable variables 
xblah = pd.get_dummies(x, columns=['Position','college'])
#removes blank spaces and puts a 0 so no more errors 
xblah = xblah.fillna(0)

xtrain, xtest, ytrain, ytest = train_test_split(xblah, y,test_size =0.2, random_state=7 )

model = RandomForestRegressor()
model.fit(xtrain,ytrain)


#now prospects

xprospect = pres[['Position','college','Height','Weight','40-yd Dash','Vertical Jump','Bench Press','Broad Jump','3-Cone Drill','20-yd Shuttle','receptions','rec yards','Tds_x','carries','rush yards','YpC','Tds_y','CmpPct','pass yards','PTds','ints','P rating','Sacks','Tackles']]

xprospectblah = pd.get_dummies(xprospect, columns=['Position', 'college'])
xprospectblah = xprospectblah.fillna(0)

xprospectblah = xprospectblah.reindex(columns = xblah.columns , fill_value=0)


#draft stuff

draftorder = ['Raiders','Jets','Cardinals','Titans','Giants','Browns','Commanders','Saints','Chiefs','Bengals','Dolphins','Cowboys','Rams','Ravens','Buccaneers','Jets','Lions','Vikings','Panthers','Cowboys','Steelers','Chargers','Eagles','Browns','Bears','Bills','49ers','Texans','Chiefs','Dolphins','Patriots','Seahawks']
teamneeds ={
    'Raiders':['QB'],
    'Jets':['EDGE'], 
    'Cardinals':['EDGE', 'ILB','OLB'],
    'Titans':['WR','RB', 'ILB','OLB'],
    'Giants':['ILB','OLB','S', 'WR','RB'],
    'Browns':['LT', 'WR', 'OG'],
    'Commanders':['RB','EDGE','WR'],
    'Saints':['WR','EDGE','DT'],
    'Chiefs':['EDGE', 'CB','WR'],
    'Bengals':['S','DT','EDGE'],
    'Dolphins':['WR','OT','OG'],
    'Cowboys':['CB','S','ILB'],
    'Rams':['OT','WR','OG'],
    'Ravens':['EDGE','WR','OG'],
    'Buccaneers':['EDGE','WR'],
    'Lions':['OT','OG','CB'],
    'Vikings':['RB', 'DT','DL','S'],
    'Panthers':['WR', 'TE','EDGE','RB'],
    'Steelers':['WR','QB','RB'],
    'Chargers':['WR','OG','S'],
    'Eagles':['RT','EDGE','WR','OT'],
    'Bears':['EDGE','DT','S','RB'],
    'Bills':['OG','EDGE','ILB'],
    '49ers':['RT','OG','WR'],
    'Texans':['OT','OG','RB'],
    'Patriots':['WR','OT'],
    'Seahawks':['EDGE','CB','RB'] 
    }
#determine better player
pres['PPick'] = model.predict(xprospectblah)

#sort by that value of betterness and make a copy to not mess up the original list
bestav = pres.sort_values('PPick')
bestav = bestav.copy()
i=1
for team in draftorder:
    need = teamneeds[team]
    u = bestav[bestav['Position'].isin(need)]
    
    #if bestav.index.get_loc(u.index[0])> 5 and i<10:
    #    pick = bestav[bestav['Position']!='QB'].iloc[0]  
    #if bestav.index.get_loc(u.index[0])> 9 and i>10:
      #  pick = bestav[bestav['Position']!='QB'].iloc[0]  

    #else:
     #   pick = bestav[bestav['Position'].isin(need)].iloc[0]
    pick = bestav[bestav['Position'].isin(need)].iloc[0]
    
    print(f"{team}-{i}-{pick['name']}-{pick['Position']}")
    i+=1
    bestav = bestav.drop(pick.name)

        


