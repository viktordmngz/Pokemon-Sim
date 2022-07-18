import time
import numpy as np
import sys
import random
#
#print one character of a string to the screen at a time
def delay_print(string):
	for char in string:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.05)
#
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
#
class shootout:
	def __init__(self, name, moves, stats, health = '===================='):
		# save variables as attributes
		self.name = name
		self.moves = moves
		self.attack = stats['attk']
		self.defense = stats['def']
		self.speed = stats['spd']
		self.luck = stats['lck']
		self.health = health
		self.bars = 20 # Amount of health bars
#
	def playersTurn(self,shooter2):
		print(f"\n{self.name}\t\tHLTH\t{self.health}")
		print(f"{shooter2.name}\t\tHLTH\t{shooter2.health}\n")
#
		print(f"\n{self.name}!\n")
		for i, x in enumerate(self.moves):
			print(f"{i+1}.", x)
		index = int(input("Pick a move: "))
		delay_print(f"\n{self.name} used {self.moves[index-1]}!")
		time.sleep(1)
#
		# Determine damage to shooter 2
		if random.random() > (1-luck/100):
			delay_print(f"\n{self.moves[index-1]} missed!\n")
			time.sleep(1)
			return
		shooter2.bars -= self.attack
		shooter2.health = ""
		if shooter2.bars <= 0:
			print(f"\n{self.name}\t\tHLTH\t\t{self.health}")
			print(f"{shooter2.name}\t\tHLTH\t\t{shooter2.health}")
			time.sleep(0.5)
			delay_print("\n..." + shooter2.name + " fainted.")
			money = random.randint(200, 1000)
			delay_print(f"\n\nYou got ${money}\n\n")
			return
#
		# Add back bars to shooter 2
		for j in range(int(shooter2.bars+.1*shooter2.defense)):
			shooter2.health += "="
		time.sleep(1)
#
		print(f"\n{self.name}\t\tHLTH\t{self.health}")
		print(f"{shooter2.name}\t\tHLTH\t{shooter2.health}\n")
		time.sleep(0.5)
		return
#							SHOOTER 2's TURN
	def cpuTurn(self, shooter2):
		####### Shooter 2's turn #######
			delay_print(f"\n{shooter2.name}!\n")
			for i, x in enumerate(shooter2.moves):
				print(f"{i+1}.", x)
			index = random.randint(0,3)
			delay_print(f"\n{shooter2.name} used {shooter2.moves[index]}!")
			time.sleep(1)
#
			# Determine damage to Player
			if random.random() > (1-luck/100):
				delay_print(f"\n{shooter2.moves[index]} missed!\n")
				time.sleep(1)
				return
			self.bars -= shooter2.attack
			self.health = ""
#
			# Check to see if other player fainted
			if self.bars <= 0:
				print(f"\n{self.name}\t\tHLTH\t{self.health}")
				print(f"{shooter2.name}\t\tHLTH\t{shooter2.health}\n")
				time.sleep(0.5)
				delay_print("\n..." + self.name + " fainted.")
				# How much money we lose
				money = random.randint(100, 500)
				delay_print(f"\n\nYou lost ${money}\n\n")
				return
			# Add back bars
			for j in range(int(self.bars+.1*self.defense)):
				self.health += "="
#
			time.sleep(1)
#
			print(f"\n{shooter2.name}\t\tHLTH\t{shooter2.health}")
			print(f"{self.name}\t\tHLTH\t{self.health}\n")
			time.sleep(0.5)
#
	def duel(self, shooter2):
		# Two player duel between self and shooter2
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
		print(f"\n{shooter2.name}")
		print("ATTACK/", shooter2.attack)
		print("DEFENSE/", shooter2.defense)
		print("SPEED/", shooter2.speed)
		print("LUCK/", shooter2.luck)
		print("LVL/", 2*(1+np.mean([shooter2.attack, shooter2.defense])))
		time.sleep(2)
#
		while (self.bars > 0 and shooter2.bars > 0):
			self.playersTurn(shooter2)
			if shooter2.bars <= 0:
				print('\n')
				print('*'*40)
				break
			self.cpuTurn(shooter2)
			print('\n')
			print('*'*40)
#
if __name__ == '__main__':
	# Create shooters
	Player = shootout('Player', ['Quickdraw', 'Shawty', 'Charge Shot', 'Rifleman'], {'attk':8,'def':15,'spd':7,'lck':55})
	Doofy = shootout('Doofy', ['Tackle', 'The Wanted', 'Quick Fire', 'Duty Calls'], {'attk':4,'def':14,'spd':2,'lck':2})
	CrazyPete = shootout('Crazy Pete', ['Chainsaw', 'Six Shooter', 'Try it, Bitch', 'Beat Down'], {'attk':10,'def':2,'spd':2,'lck':12})
	Pigeon = shootout('Pigeon', ['Stomp A Mudhole', 'Dynamite Stick', 'ACME Anvil', 'Ignore'], {'attk':5,'def':15,'spd':17,'lck':22})
#
	Player.duel(CrazyPete)


""""
Need some way to do speed and luck

want speed to determine which player goes first

want luck to determine whether a move hits

for luck:
maybe a random integer comparison

ex:
luck = 12
maybe that can correlate with a 12% chance of a miss

if random.random() > (1-(luck/100)):


"""