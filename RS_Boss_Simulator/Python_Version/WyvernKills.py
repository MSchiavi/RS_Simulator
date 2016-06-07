import math
import random
import time
from Loot import *
from decimal import *
import sys
from InputReader import *
import time
from partitions import *
from fractions import Fraction
from formater import *

start_time = time.time()

inFile = sys.argv[1]
Input = open(inFile)
Contents = Input.read()
print(Contents)
Input.close()



inputs = Input_filereader(inFile)

AKS = inputs[1]  #user inputs
TripTime = inputs[0] # user inputs
NumKills = round(TripTime/AKS)
BinSize = inputs[3]

#Need to automate finding these numbers so the user can automate "bin" size

Parts = partitions(BinSize)
Parts.setup()


#Order FindPartitions returns an array in
# Common Uncommon RDT Elite Legs Visage

#commL = 55875
#uncommL = 13968.8
#legsL = 873.047
#visageL = 44.0
#rdtL = 27937.5
#eliteL = 1277.14

#commL = Partitions[0]
#uncommL = Partitions[1]
#legsL = Partitions[4]
#visageL = Partitions[5]
#rdtL = Partitions[2]
#eliteL = Partitions[3]

commL = Parts.Partitions[0]
uncommL = Parts.Partitions[1]
legsL = Parts.Partitions[4]
visageL = Parts.Partitions[5]
rdtL = Parts.Partitions[2]
eliteL = Parts.Partitions[3]


Prize={}

print( "You input you will kill", int(NumKills), "Wyverns, the sumulation will calculate your loot within 20% of this number of kills. This is to speed up calculation time, calculation  time may vary.")

#LootTest simply tests using a random number to pick a piece of loot from the loot inventory in "Loot.py"
def LootTest(x):
    i=0.0
    while i < x:
        a=random.randrange(0,len(LootCom['Item']),1)
        print LootCom['ID'][a],LootCom['Item'][a],LootCom['Quantity'][a],LootCom['Value'][a]
        i=i+1

#LootTest2 uses a while loop to add items to the prize lists, plans are to add a certain number of each item based on rarity to the list to then be picked from randomly for the loot drop.
def LootTest2():
    i=0
    j=0
    while i < (len(LootCom['Item'])):
        print i
        Prize.update({i: [LootCom['Item'][i],LootCom['Quantity'][i],LootCom['Value'][i]]})
        i = i+1
            #    while j < (len(LootUnCom['Item'])):
            #print j
            #Prize.update({i: LootUnCom['Item'][j]})
            #j=j+1
    return Prize

def in_comm(point):
    x = point[0]
    y = point[1]
    return (x > 0 and x <= commL) and (y > 0 and y <= BinSize)
#return 1==1
def in_uncomm(point):
    x = point[0]
    y = point[1]
    return (x > commL and x <= (commL + uncommL)) and (y > 0 and y <= BinSize)

def in_legs(point):
    x = point[0]
    y = point[1]
    return (x > (commL + uncommL) and x <= (commL + uncommL + legsL)) and (y > 0 and y <= BinSize)

def in_visage(point):
    x = point[0]
    y = point[1]
    return (x > (commL + uncommL + legsL) and x <= (commL + uncommL + legsL + visageL)) and (y > 0 and y <= BinSize)

def in_rdt(point):
    x = point[0]
    y = point[1]
    return (x > (commL + uncommL + legsL + visageL) and x <= (commL + uncommL + legsL + visageL + rdtL)) and (y > 0 and y <= BinSize)

def in_elite(point):
    x = point[0]
    y = point[1]
    return (x > (commL + uncommL + legsL + visageL + rdtL) and x <= (commL + uncommL + legsL + visageL + rdtL+eliteL)) and (y > 0 and y <= BinSize)



def GenLowProb(Repeats):
    comm_count = 0
    uncomm_count = 0
    legs_count = 0
    visage_count = 0
    rdt_count = 0
    elite_count = 0
    for i in range(1,int(Repeats) + 1):


            
        point = [random.randint(0,BinSize),random.randint(0,BinSize)]
        
        
        if in_comm(point):
            comm_count = comm_count + 1
        elif in_rdt(point):
            rdt_count = rdt_count + 1
        elif in_uncomm(point):
            uncomm_count += 1
        elif in_elite(point):
            elite_count += 1
        elif in_legs(point):
            legs_count += 1
        elif in_visage(point):
            visage_count += 1
    counts = [comm_count,rdt_count,uncomm_count,elite_count,legs_count,visage_count]
    return counts



Events = inputs[2] + 1 # so when they type in 500 its 500 and not 499 because range function
B = 0
def DropTableNumbers():
    avg = [0,0,0,0,0,0]
    
    for i in range(1,Events):
    
        sys.stdout.write('\r')
        sys.stdout.write("Wyvern Events Generated:      " + str(i) + "/" + str(Events - 1))
        sys.stdout.flush()
    
        a = GenLowProb(NumKills)
        avg = [a[0]+avg[0],a[1]+avg[1],a[2]+avg[2],a[3]+avg[3],a[4]+avg[4],a[5]+avg[5]]
        if i == Events - 1:
            avg = ['%.3f'%((avg[0]+0.0)/i),'%.3f'%((avg[1]+0.0)/i),'%.3f'%((avg[2]+0.0)/i),'%.3f'%((avg[3]+0.0)/i),'%.3f'%((avg[4]+0.0)/i),'%.3f'%((avg[5]+0.0)/i)]
            Total = (round(float(avg[0])) + round(float(avg[1])) + round(float(avg[2])) + round(float(avg[3])) + round(float(avg[4])) + round(float(avg[5])))
    results = [avg,Total]
    return results

TableNumbers = [0,0]
while (TableNumbers[1] > (NumKills + NumKills*.20) or (TableNumbers[1] < NumKills - NumKills*.20)):
        TableNumbers = DropTableNumbers()

print("\n")
print("Number of times hit on a respective table \n")
print("Common, RDT, Uncommon, Elite Clue, Legs, Visage!!! \n ")
print(TableNumbers[0])
print(TableNumbers[1])



def Calculate_Loot():
    loot = {}
    loot['Item'] = []
    loot['Quantity'] = []
    loot['Value'] = []

    for i in range(0,int(float(TableNumbers[0][0]))): # This is the common stuff
        Id = random.choice(LootCom['ID'])
        if LootCom['Item'][Id] in loot['Item']:
            item = loot['Item'].index(LootCom['Item'][Id])
            loot['Quantity'][item] = loot['Quantity'][item] + LootCom['Quantity'][Id]
            loot['Value'][item] = loot['Value'][item] + LootCom['Value'][Id]
        else:

            loot['Item'].append(LootCom['Item'][Id])
            loot['Quantity'].append(LootCom['Quantity'][Id])
            loot['Value'].append(LootCom['Value'][Id] * LootCom['Quantity'][Id])

    for j in range(0,int(float(TableNumbers[0][2]))): # This is the uncommon stuff
        Id = random.choice(LootUnCom['ID'])
        if LootUnCom['Item'][Id] in loot['Item']:
            item = loot['Item'].index(LootUnCom['Item'][Id])
            loot['Quantity'][item] = loot['Quantity'][item] + LootUnCom['Quantity'][Id]
            loot['Value'][item] = loot['Value'][item] + LootUnCom['Value'][Id]
        else:
            loot['Item'].append(LootUnCom['Item'][Id])
            loot['Quantity'].append(LootUnCom['Quantity'][Id])
            loot['Value'].append(LootUnCom['Value'][Id] * LootUnCom['Quantity'][Id])
   

    for j in range(0,int(float(TableNumbers[0][3]))): # This is the elite clue
        Id = random.choice(LootElite['ID'])
        if LootElite['Item'][Id] in loot['Item']:
            item = loot['Item'].index(LootElite['Item'][Id])
            loot['Quantity'][item] = loot['Quantity'][item] + LootElite['Quantity'][Id]
            loot['Value'][item] = loot['Value'][item] + LootElite['Value'][Id]
        else:
            loot['Item'].append(LootElite['Item'][Id])
            loot['Quantity'].append(LootElite['Quantity'][Id])
            loot['Value'].append(LootElite['Value'][Id] * LootElite['Quantity'][Id])

    for j in range(0,int(float(TableNumbers[0][4]))): # This is the legs
        
        Id = random.choice(LootLegs['ID'])
        if LootLegs['Item'][Id] in loot['Item']:
            item = loot['Item'].index(LootLegs['Item'][Id])
            loot['Quantity'][item] = loot['Quantity'][item] + LootLegs['Quantity'][Id]
            loot['Value'][item] = loot['Value'][item] + LootLegs['Value'][Id]
        else:
            loot['Item'].append(LootLegs['Item'][Id])
            loot['Quantity'].append(LootLegs['Quantity'][Id])
            loot['Value'].append(LootLegs['Value'][Id] * LootLegs['Quantity'][Id])

    for j in range(0,int(float(TableNumbers[0][5]))): # This is the Vrare stuff aka visage
        Id = random.choice(LootVrare['ID'])
        if LootVrare['Item'][Id] in loot['Item']:
            item = loot['Item'].index(LootVrare['Item'][Id])
            loot['Quantity'][item] = loot['Quantity'][item] + LootVrare['Quantity'][Id]
            loot['Value'][item] = loot['Value'][item] + LootVrare['Value'][Id]
        else:
            loot['Item'].append(LootVrare['Item'][Id])
            loot['Quantity'].append(LootVrare['Quantity'][Id])
            loot['Value'].append(LootVrare['Value'][Id] * LootVrare['Quantity'][Id])

    print(loot['Item'])
    print(loot['Quantity'])
    print(loot['Value'])
    return loot
loot = Calculate_Loot()
print("********************************************************")
print("Formated loot table ")
print("********************************************************")
formatedloot = format(loot['Item'],loot['Quantity'],loot['Value'])
print(formatedloot)
print(Total(formatedloot), "Total gps")
print(perhour(Total(formatedloot),TripTime),"  gp/hr")
print("Run time:",'%.3f'%(time.time()-start_time) )