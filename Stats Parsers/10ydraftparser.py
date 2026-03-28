# my nfl draft parser
#use this for pasting data and turning in2 csv
import csv
import os
#input and output
myinput='rawdata.txt'
outputfile='finaldata.csv'
#open it
blah = open(myinput, 'r')
readit = blah.read()
blah.close()
#closed
#time to split it 
newlist = readit.split('\n')
newlist =[line.strip() for line in newlist if line.strip() !='']
#add a newline at the pick number to seperate by player
i=0
player=[]
amount = len(newlist)
year = 2014
while i < amount:
    if newlist[i].isdigit():
        
        pick=newlist[i]
        i+=1
        if int(pick)==1:
            year +=1
        else:
            year =year
        
        

        teamname=newlist[i]
        i+=1

        city = newlist[i]
        i+=2

        name=newlist[i]
        i+=1

        position=newlist[i]
        i+=1

        college=newlist[i]
        i+=1
        
        if '>' in newlist[i] or 'From' in newlist[i] or 'from' in newlist[i]:
            trade=newlist[i]
            i+=1
        else: 
            trade =''
        drafted = {'pick':pick,'team name':teamname,'name':name,'position':position,'college':college,'year':year}
        player.append(drafted)
        
    
    

    else:
        i+=1

with open(outputfile, 'w', newline='') as blaf:
    write = csv.DictWriter(blaf, fieldnames=['pick','team name','name','position','college','year'] )
    write.writeheader()
    write.writerows(player)