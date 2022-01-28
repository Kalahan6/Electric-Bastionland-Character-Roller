import random
def rollStat():
	total = 0
	for x in range (0,3):
		dice = random.randint(1, 6)
		total += dice
	return total

print("BASTIONLAND CHARACTER GENERATOR")
print("\n")			
statSTR = rollStat()
print("Maximum/Starting Strength:\t"+ str(statSTR))
statDEX = rollStat()
print("Maximum/Starting Dexterity:\t"+ str(statDEX))
statCHA = rollStat()
print("Maximum/Starting Charisma:\t" + str(statCHA))
print("\n")

print("Money (£):\t\t\t" + str(random.randint(1,6)))
statHP = random.randint(1,6)
print("Maximum HP:\t\t\t" + str(statHP))
print("Current HP:\t\t\t" + str(statHP) )

print("\n")

statsList = [statSTR, statDEX, statCHA]
if max(statsList) <= 9:
	careerNumber = min(statsList) - 2
elif max(statsList) == 10:
	careerNumber = min(statsList) + 5
elif max(statsList) == 11:
	careerNumber = min(statsList) + 13
elif max(statsList) == 12:
	careerNumber = min(statsList) + 22
elif max(statsList) == 13:
	careerNumber = min(statsList) + 32
elif max(statsList) == 14:
	careerNumber = min(statsList) + 42
elif max(statsList) == 15:
	careerNumber = min(statsList) + 52
elif max(statsList) == 16:
	careerNumber = min(statsList) + 62
elif max(statsList) == 17:
	careerNumber = min(statsList) + 72
elif max(statsList) == 18:
	careerNumber = min(statsList) + 82

print("Failed Career # (Stats based):\t" + str(careerNumber))

careerNumberRandom = random.randint(1,100)
print("Failed Career # (D100 based):\t" + str(careerNumberRandom))