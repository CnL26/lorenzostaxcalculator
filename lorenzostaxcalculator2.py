import sys, time, os

time.sleep(.5)
title = ("          Welcome to...\nLorenzo's Sales_Tax-Calculator\n          Program\n\n      Please begin entering...\n")
for char in title:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.1)

subTotal = 0
add_next_number = True
while add_next_number == True:
	num1 = float(input("Amount:"))
	subTotal = subTotal + num1
	print(subTotal)
	answer = input(" Want to continue?\nType y(keep adding)\nOr press enter(Grand Total)\n")
	if answer == 'y':
		add_next_number = True
	else:
		add_next_number = False	    	
num2 = 0.07
converted = (subTotal+num1)*num2
finAmount = converted + subTotal

ending = (f"Your Grand Total is\n  ${round(finAmount, 2)}\n")
for char in ending:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.1)
		
time.sleep(.5)
outro = ("\n*PEACE,*\n **and a**\n***bottle of HAIR GREASE***")
for char in outro:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.1)