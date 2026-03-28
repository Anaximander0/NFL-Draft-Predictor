import pandas
import csv
import os
#inputs
myinput='2025qbstats.txt'
myoutput='2025qbprospects.csv'
#read it now

blaw = open(myinput, 'r')
passline = blaw.read()
blaw.close()

newpasslist = passline.split('\n')

newpasslist = [line.strip() for line in newpasslist if line.strip()!='']

i=0
player=[]
amount = len(newpasslist)
year = 0
nrl=newpasslist
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


       Pct=m[8]
       yards=m[9]

       td=m[11]
       ints=m[12]
       Prating=m[13]
       i+=1
       drafted = {'rank':rank,'name':name,'college':college,'class':cls,'pos':pos, 'CmpPct':Pct, 'pass yards':yards,'Tds':td,'ints':ints,'P rating':Prating,'year':year}
       player.append(drafted)


with open(myoutput, 'w', newline='') as blaj:
    write = csv.DictWriter(blaj, fieldnames=['rank','name','college','class','pos','CmpPct','pass yards','Tds','ints','P rating','year'])
    write.writeheader()
    write.writerows(player)