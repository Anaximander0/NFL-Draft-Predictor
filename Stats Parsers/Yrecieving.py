import pandas
import csv
import os
#inputs
myinput='2025wrstats.txt'
myoutput='2026wrprospects.csv'
#read it now

blaw = open(myinput, 'r')
recline = blaw.read()
blaw.close()

newreclist = recline.split('\n')

newreclist = [line.strip() for line in newreclist if line.strip()!='']

i=0
player=[]
amount = len(newreclist)
year = 0
nrl=newreclist
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
       rec=m[6]
       yards=m[7]
       td =m[9]
       i+=1
       drafted = {'rank':rank,'name':name,'college':college,'class':cls,'pos':pos, 'receptions':rec, 'rec yards':yards, 'Tds':td, 'year':year}
       player.append(drafted)


with open(myoutput, 'w', newline='') as blaj:
    write = csv.DictWriter(blaj, fieldnames=['rank','name','college','class','pos','receptions', 'rec yards', 'Tds','year'])
    write.writeheader()
    write.writerows(player)