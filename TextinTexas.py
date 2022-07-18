import time
import numpy as np
import sys
import random

#print one character of a string to the screen at a time
def delay_print(string):
	for char in string:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.05)

"""
print(
'''
The year is 1855. The government is looking for a gun smuggler known only as The Hornet.

He is a man in his late 20's but not much else is known about him.
They know that he uses hornet venom on his bullets so even grazing shots can kill.
They tell you he is travelling west and that he was last spotted just outside a town called Johnstown. 

And so our tale begins...
'''
)
"""

class shootout:
	def __init__(self, name, moves, stats, health = '='*20):
		# save variables as attributes
		self.name = name
		self.moves = moves
		self.attack = stats['attk']
		self.defense = stats['def']
		self.speed = stats['spd']
		self.luck = stats['lck']
		self.health = health
		self.bars = len(health) # Amount of health bars
#
	def duel(self, shootout2):
		# Two player duel between self and shootout2
		########################
		#print fight information
		print("-----SHOOTOUT DUEL-----")
		print(f"\n{self.name}")
		print("ATTACK/", self.attack)
		print("DEFENSE/", self.defense)
		print("SPEED/", self.speed)
		print("LUCK/", self.luck)
		print("LVL/", 2*(1+np.mean([self.attack, self.defense])))
		print("\nVS")
		#--------Shootout2's info--------#
		print(f"\n{shootout2.name}")
		print("ATTACK/", shootout2.attack)
		print("DEFENSE/", shootout2.defense)
		print("SPEED/", shootout2.speed)
		print("LUCK/", shootout2.luck)
		print("LVL/", 2*(1+np.mean([shootout2.attack, shootout2.defense])))
#
		time.sleep(2)
#
		while (self.bars > 0) and (shootout2.bars > 0):
			print(f"\n{self.name}\t\tHLTH\t{self.health}")
			print(f"{shootout2.name}\t\tHLTH\t{shootout2.health}\n")
#
			print(f"\n{self.name}! ")
			for i, x in enumerate(self.moves):
				print(f"{i+1}.", x)
			index = int(input("Pick a move: "))
			delay_print(f"\n{self.name} used {self.moves[index-1]}!")
			time.sleep(1)
#
			# Determine damage to shooter 2
			shootout2.bars -= self.attack
			shootout2.health = ""
#
			# Add back bars to shooter 2
			for j in range(int(shootout2.bars+.1*shootout2.defense)):
				shootout2.health += "="
#
			time.sleep(1)
#
			print(f"\n{self.name}\t\tHLTH\t{self.health}")
			print(f"{shootout2.name}\t\tHLTH\t{shootout2.health}\n")
			time.sleep(0.5)
#
			# Check to see if shooter 2 fainted
			if shootout2.bars <= 0:
				delay_print("\n..." + shootout2.name + " fainted.")
				break
#
####### Shooter 2's turn #######
			print(f"\n{shootout2.name}! ")
			for i, x in enumerate(shootout2.moves):
				print(f"{i+1}.", x)
			index = random.randint(0,4)
			delay_print(f"\n{shootout2.name} used {shootout2.moves[index]}!")
			time.sleep(1)
#
			# Determine damage to Player
			self.bars -= shootout2.attack
			self.health = ""
#
			# Add back bars
			for j in range(int(self.bars+.1*self.defense)):
				self.health += "="
#
			time.sleep(1)
#
			print(f"\n{shootout2.name}\t\tHLTH\t{shootout2.health}")
			print(f"{self.name}\t\tHLTH\t{self.health}\n")
			time.sleep(0.5)
#
			# Check to see if other player fainted
			if self.bars <= 0:
				delay_print("\n..." + self.name + " fainted.")
				break
			print('*'*40)
#
		money = random.randint(200, 1000)
		delay_print(f"\n\nYou got ${money}\n\n")
#
if __name__ == '__main__':
	# Create shooters
	Player = shootout('Player', ['Quickdraw', 'Shawty', 'Charge Shot', 'Rifleman'], {'attk':7,'def':15,'spd':7,'lck':2})
	Doofy = shootout('Doofy', ['Tackle', 'The Wanted', 'Quick Fire', 'Duty Calls'], {'attk':10,'def':14,'spd':2,'lck':2})
	CrazyPete = shootout('Crazy Pete', ['Chainsaw', 'Six Shooter', 'Try it, Bitch', 'Beat Down'], {'attk':12,'def':2,'spd':2,'lck':12})
	Pigeon = shootout('Pigeon', ['Stomp A Mudhole', 'Deadly Smile', 'Spit', 'Ignore'], {'attk':5,'def':15,'spd':17,'lck':22})
#
	Player.duel(Pigeon)