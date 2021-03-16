from os import system
from menu import commands

terHgt = 37
terWdt = 125

def menu(terHgt,terWdt):
	while True:
		returnstat = str(commands(str(''),terHgt,terWdt))
		if returnstat == 'Exit':
			system('clear')
			break

system('clear')
menu(terHgt,terWdt)
system('clear')
