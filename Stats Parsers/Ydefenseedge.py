import pandas
import csv
import os
#inputs
myinput='2025destats.txt'
myoutput='2026deprospects.csv'
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


       tackle=m[6]
      
       i+=1
       drafted = {'rank':rank,'name':name,'college':college,'class':cls,'pos':pos, 'Tackles':tackle, 'Year':year}
       player.append(drafted)


with open(myoutput, 'w', newline='') as blaj:
    write = csv.DictWriter(blaj, fieldnames=['rank','name','college','class','pos','Tackles', 'Year'])
    write.writeheader()
    write.writerows(player)