# Hello
#Author Jacob Woloschek
import sys
class Dino:
	health = 5

	def function(self):
		print("Def message")

print'This program will print out how many total dinosaurs are created'
print 'using the Polyraptor and Forerunner of the Empire combo'
print ' '
dmg = raw_input('Enter damage to be done: ')
#print("Damage: " + dmg)
count = 0
dead = 0
Dinos = []
Dinos.append(Dino())
#print 'health:',Dinos[0].health
#Dinos[0].health -= 1
#print 'health:',Dinos[0].health

for x in range(int(dmg)): # Starting from 0 dmg loop through to max dmg
	#print 'X is',x
	for num, obj in enumerate(Dinos,start=0): # Iterate through the Dinos list and distribute damage
		if Dinos[num] == 0: # No longer in use
			num +=1
		else:
			Dinos[num].health -= 1 # Deal one damage to each Dino object in list
			#print num,'Pinged for 1'
			#print '	Dino',num,'has health',Dinos[num].health
			count += 1 # This variable "counts" how many new dinosaurs need to be created
			#Dinos.append(Dino())
			#print 'copy of',num,'being created'
			if Dinos[num].health == 0: # Checks to see if current dino has 0 health
				print 'Dino',num,'is dead' # If it does print that it's dead
				# The "num" in the above print statement aligns with the number in the list not the actual number of dead dinos

				#Dinos[num] = 0
				#Dinos[num].health = sys.maxint
				#dead += 1
				del Dinos[num] # Delete dino from list
				Dinos[num+1].health -= 1 # Subtract 1 from health of next dino since deleting messes up the order
	print ''
	for y in range(int(count)): # After damage and deaths are deal with add the new dinosaurs to the list
		Dinos.append(Dino()) 
	count = 0

total = len(Dinos) - int(dead)
#print 'len',len(Dinos),'dead',dead
print 'Dinos:',total # Print number of dinos left

