#Program Name: WeaponBalanceTest.py
#Purpose: Platform for building weapon classes and testing results near infinity (or very large values)
#Author: Jack O'Brien
#Date of creation: 12/11/2014
#Date of last edit: 12/11/2014

from random import randint
import matplotlib.pyplot as plt
import numpy as np


class Gun():

	def __init__(self, Damage = "1d6+0", Category = 'M', Range = 40, Critical = '19-20x2'):

		self.Damage = parseDamage(Damage)

		self.Critical = parseCritical(Critical)

		self.Category = 'M'

		self.Range = Range

	def attack(self, DC = 10, Bonus = 0): #Run Through an Attack

		toHit = rollToHit(Bonus) #Initial Roll

		crit = 0 #Number of Critical Hits

		damageCaused = 0 #Total Damaged Inflicted on Target

		for i in range(self.Critical(toHit['Raw']) - 1): #determines the bonus from critical hits

				crit = i + 1

				if not self.Critical(rollToHit(Bonus)):

					break

		if toHit['Result'] > DC or toHit['Raw'] == 20:

			for i in range(crit + 1):damageCaused += self.Damage()

		return damageCaused



def parseDamage(Damage, pos = 0): #Parses the Damage parameter for a weapon

	n = int(Damage[:Damage.find('d')]) #Number of dice rolled

	d = int(Damage[Damage.find('d')+1:Damage.find('+')]) #Number of sides on dice rolled

	m = int(Damage[Damage.find('+')+1:]) #Modifier of the dice roll

	def Output(): #Function used for determining result of weapon use

		result = 0

		for i in range(n):

			result += randint(1,d)

		result += m

		return result
	
	return Output



def parseCritical(Critical): #Parses the Critical parameter for a weapon

	if Critical.find('-') != -1:

		threatRange = int(Critical[:Critical.find('-')]) #Sets the threat range for a critical hit

	else:

		threatRange = 20
	
	n = int(Critical[Critical.find('x')+1:]) #Critical Multiplier

	def detectCritical(RawRoll): #Function for determining critical hit result

		if RawRoll >= threatRange:

			return n

		else:

			return 0

	return detectCritical


def rollToHit(Bonus = 0): #Manages d20 rolls by returning raw roll values and final roll values

	raw = randint(1,20)

	return {'Raw':raw,'Result': raw + Bonus}


def rateWeapon(weapon):

	Data = np.array([weapon.attack(Bonus = 20) for i in range(500000)])
	plt.hist(Data, bins = Data.max()-Data.min(), range = (Data.min(), Data.max()+1))
	print "Mean:  ",np.mean(Data)
	print "Median:",np.median(Data)
	print "TTK:   ",10.0/np.mean(Data)

	plt.show()

rifle = Gun(Damage = '2d8+0', Critical = '20x3')
sniper = Gun(Damage = '2d10+0', Critical = '20x4')
pistol = Gun()
rocket = Gun(Damage = '10d10+0', Critical = '20x0')

rateWeapon(rifle)
rateWeapon(sniper)
rateWeapon(pistol)
rateWeapon(rocket)

