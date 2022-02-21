import time

time.sleep(.5)
print("Welcome to Lorenzo's Sales_Tax Calculator \nPlease begin entering total...")

subTotal = 0

add_next_number = True

while add_next_number == True:
	num1 = float(input("Amount:"))
	subTotal = subTotal + num1
	print(subTotal)
	
	answer = input(" Want to continue?\nType y(keep adding)\nOr press enter(Grand Total)")
	if answer == 'y':
	    add_next_number = True
	else:
	    	add_next_number = False
	    	
num2 = 0.07
converted = (subTotal+num1)*num2
finAmount = converted + subTotal
print("Your Grand Total is\n**!{round(finAmount, 2)}!**")
time.sleep(1)
print("**PEACE,\nand a\nbottle of HAIR GREASE**")