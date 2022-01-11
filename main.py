import random
def rollStat():
	total = 0
	for x in range (0,3):
		dice = random.randint(1, 6)
		total += dice
	return total
			
statSTR = rollStat()
print("Maximum Strength:\t" + str(statSTR) + " \t Current Strength:\t" + str(statSTR) )
statDEX = rollStat()
print("Maximum Dexterity:\t" + str(statDEX) + "\t Current Dexterity:\t" + str(statDEX) )
statCHA = rollStat()
print("Maximum Charisma:\t" + str(statCHA) + " \t Current Charisma:\t" + str(statCHA) )

print("Money (£):\t\t\t" + str(random.randint(1,6)))
statHP = random.randint(1,6)
print("Maximum HP:\t\t\t" + str(statHP) + "\t Current HP:\t\t" + str(statHP) )

			
print("\n")
statsList = [statSTR, statDEX, statCHA]
print("Lowest Stat: " + str(min(statsList)) + "\t Highest Stat: " + str(max(statsList)))
