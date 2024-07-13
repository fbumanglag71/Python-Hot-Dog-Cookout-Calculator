## Author: Francisco Bumanglag
## Project: HOT DOG COOKOUT CALCULATOR
## Assignment: Module 1 Project 6
## Course: Python Santa Ana College
## Class: CMPR114 Jason Sim
## Date: June 18, 2023

import math

#CONSTANTS
HOT_DOG_PACKAGE = 10
HOT_BUNS_PACKAGE = 8

#INPUT 
numberPeople = int(input('Enter the number of people who will be at the cookout: '))
numberDogsPerson = int(input('Enter the number of hot dogs each person will eat: '))

#CALCULATIONS -- NUMBER OF PACKAGES REQUIRED 
totalDogsRequired = math.ceil(numberPeople * numberDogsPerson / HOT_DOG_PACKAGE)
hotDogsBunsRequired = math.ceil(numberPeople * numberDogsPerson / HOT_BUNS_PACKAGE)
        #math.ceil returns the smallest integer greater than or equal to a given number.


#CALCULATIONS -- LEFTOVERS 
dogsLeftover = (totalDogsRequired * HOT_DOG_PACKAGE) - (numberPeople * numberDogsPerson)
bunsLeftover = (hotDogsBunsRequired * HOT_BUNS_PACKAGE) - (numberPeople * numberDogsPerson)

#OUTPUT 
print ('The number of hot dogs needed for the cookout is: ', totalDogsRequired)
print ('The number of hot dog buns need for the cookout is: ', hotDogsBunsRequired)
print ('The number of leftover hot dogs is: ', dogsLeftover)
print ('The number of leftoever hot dog buns is: ', bunsLeftover)







