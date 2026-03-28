import pandas
import csv
import os
#inputs
myinput='2025rbstats.txt'
myoutput='2026rbprospects.csv'
#read it now

blaw = open(myinput, 'r')
rushline = blaw.read()
blaw.close()

newrushlist = rushline.split('\n')

newrushlist = [line.strip() for line in newrushlist if line.strip()!='']

i=0
player=[]
amount = len(newrushlist)
year = 0
nrl=newrushlist
while i<amount:
    if nrl[i].isdigit() and len(nrl[i]) ==4:
        year = int(nrl[i])
        i+=1
    else:
       m = nrl[i].split('\t')
           
       rank = m[0]
       name = m[1]
       college = m[2]
       cls = m[3]
       pos =m[4]
       car=m[6]
       yards=m[7]
       ypc=m[8]
       td =m[9]
       i+=1
       drafted = {'rank':rank,'name':name,'college':college,'class':cls,'pos':pos, 'carries':car, 'rush yards':yards,'YpC':ypc,'Tds':td, 'year':year}
       player.append(drafted)


with open(myoutput, 'w', newline='') as blaj:
    write = csv.DictWriter(blaj, fieldnames=['rank','name','college','class','pos','carries','rush yards','YpC','Tds','year'])
    write.writeheader()
    write.writerows(player)