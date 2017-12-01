#Create a program to randomly generate a the current Multi-State PowerBall lottery ticket. The lottery ticket
#must have 5 numbers between and the values of 1 and 69, and 2 bonus balls between
#the values of 1 and 26.
import random

main_numbers=[]
bonus_numbers=[]
main_numbers_count=0
bonus_numbers_count=0

while main_numbers_count<5:
    number=random.randint (1,69)
    if number not in main_numbers:
        main_numbers.append (number)
        main_numbers_count+=1
while bonus_numbers_count<2:
    number=random.randint(1,26)
    if number not in bonus_numbers:
        bonus_numbers.append(number)
        bonus_numbers_count+=1
main_numbers.sort()


print (main_numbers,bonus_numbers)
