import sys, time, os
from pyfiglet import figlet_format
import termcolor
from termcolor import colored

os.system('clear')
msg = ("Hello\nthere,")
ascii_art = figlet_format(msg, font="3-d")
colored_ascii = colored(ascii_art, 'green')
print(colored_ascii)

time.sleep(1)
os.system('clear')
title = ("          Welcome to...\n\033[1;32;40m Lorenzo's Sales_Tax-Calculator\n           Program\n\n\033[1;37;40m	Please begin entering...\n")
for char in title:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(.1)
		
subTotal = 0
add_next_number = True
os.system('clear')
while add_next_number == True:
	num1 = float(input("Amount:"))
	subTotal = subTotal + num1
	print(f"\033[1;32;40m${subTotal}")
	answer = input("\033[1;37;40m  Want to continue?\nType y(keep adding)\nOr press enter(Grand Total)\n")
	os.system('clear')
	if answer == 'y':
		add_next_number = True
	else:
		add_next_number = False	    	
num2 = float(input("Your state's decimal tax:"))
converted = (subTotal)*num2
finAmount = converted + subTotal
os.system('clear')

ending = (f"	Your Grand Total is\n\n\033[1;32;40m 	      ${round(finAmount, 2)}\n")
for char in ending:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.1)
		
time.sleep(.5)
outro = ("\n*PEACE,*\n\033[1;31;40m  **and a**\n\033[1;33;40m ***bottle of HAIR GREASE***")
for char in outro:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.1)
os.system('clear')
		
time.sleep(.2)
haha = ("\n\033[1;31;40m ~This_program_\nWill_Self_Destruct_\nIn~_5...\n4...\n3...\n2...\n1...")
for char in haha:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(.3)
os.system('clear')
		