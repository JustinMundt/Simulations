
"""Blackjack simulator
This is a simple blackjack simulator that uses a monte carlo style simulation to show possible outcomes. 
The simulation can be modified to allow different percentage chance to win based on card counting or other methods.
"""



import random
import matplotlib
import matplotlib.pyplot as plt

hours = int(input("How many Hours are you going to play for? \n"))


TBC = 0
Totalvalue = 0
BC=0
val = 0


def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        #print roll, 'roll was 100, you win 1/100'
        return True
    elif roll <= 49:
        #print roll, 'roll was 1-49, you lose 49/100'
        return False
    elif 100 > roll > 50:
        #print roll, 'roll was 51 to 99 you win 49/100'
        return True    



def simplebettor(funds, initial_wager, wager_count, BC = 0):
    value = funds
    wager = initial_wager
    
    
    wX = []
    vY = []
    
    
    currentWager = 1
    
    while currentWager <= wager_count and value >0:
        if rollDice():
            A = varyingwager(wager) # wager will be 1x, 2x, 4x, or 8x the bet
            value += A
            #print 'A WIN!', value, wager, A
            wX.append(currentWager)
            vY.append(value)
        else:
            B = varyingwager(wager)
            value -= B
            #print 'A LOSS!', value, wager, B
            wX.append(currentWager)
            vY.append(value)
            
        currentWager += 1
        
    if value <= 0:
        value = 'broke'
        BC += 1
    #print 'Funds:',value, currentWager, TBC, BC
    plt.plot(wX,vY)
    return BC, value
   
def varyingwager(start_amount):
        roll = random.randint(1,100)
        if roll >=85:
            rint = 8
        elif roll >=70:
            rint = 4
        elif roll >= 25:
            rint = 2
        else:
            rint = 1
        return start_amount * rint
       

        
x = 0
totalplayers = int(input("Total Players"))

while x<totalplayers:
    BC, val =simplebettor(20000,100,60*hours) #varyingwager will give start wager, 2X, 4X or 8X the initial bet to start with the bettor (varyingwager(25))
    TBC += BC
    if isinstance(val, int):
        Totalvalue += val
    x+=1    
    
#plt.ylim([-2000,100000])    
plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()
print("Broke Count = ",TBC, "/",totalplayers)
print("Average Value = ",Totalvalue/totalplayers)
#print hours, hours*60
