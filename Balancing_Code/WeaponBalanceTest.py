#Program Name: WeaponBalanceTest.py
#Purpose: Platform for building weapon classes and testing results near infinity (or very large values)
#Author: Jack O'Brien
#Date of creation: 12/11/2014
#Date of last edit: 12/11/2014

from random import randint
import matplotlib.pyplot as plt
import numpy as np



class Gun():

	def __init__(Damage = '1d6+0', Category = 'M', Range = 40, Critical = '19-20x2'):

		self.Damage = parseDamage(Damage)

		self.Critical = parseCritical(Critical)

		self.Category = 'M'

		self.Range = Range


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
	
	n = int(Critical[Critical.find('x'):]) #Critical Multiplier

	def detectCritical(RawRoll): #Function for determining critical hit result

		if RawRoll >= threatRange:

			return n

		else:

			return 0

	return detectCritical
