from os import system
from lvmFunctions import *

def headbar(string,terHgt,terWdt):
	system('tput setaf 3')
	system('tput bold')
	headLen = len(string) + 8
	print(("-" * int((terWdt - headLen)/2)) + "{0} CONSOLE".format(string) + "-" * int((terWdt - headLen)/2))
	print("=" * terWdt)
	system('tput sgr0')
	system('tput setaf 7')

def menuOptions(terHgt,terWdt):
	system('tput setaf 6')
	print()
	print(" "*int(terWdt/10) + " 1: List Disks   " + " "*int(terWdt/10) + " 2: List PVs    " + " "*int(terWdt/10) + " 3: List VGs    " + " "*int(terWdt/10) + " 4: List LVs    " + " "*int(terWdt/10))
	print(" "*int(terWdt/10) + " 5: Format Disk  " + " "*int(terWdt/10) + " 6: Create PV   " + " "*int(terWdt/10) + " 7: Create VG   " + " "*int(terWdt/10) + " 8: Create LV   " + " "*int(terWdt/10))  
	print(" "*int(terWdt/10) + " 9: Mount Unmount" + " "*int(terWdt/10) + "10: Move PV     " + " "*int(terWdt/10) + "11: Extend VG   " + " "*int(terWdt/10) + "12: Extend LV   " + " "*int(terWdt/10))
	print(" "*int(terWdt/10) + "13: fdisk Utility" + " "*int(terWdt/10) + "14: Remove PV   " + " "*int(terWdt/10) + "15: Reduce VG   " + " "*int(terWdt/10) + "16: Reduce LV   " + " "*int(terWdt/10))
	print(" "*int(terWdt/10) + "17: Linux Shell  " + " "*int(terWdt/10) + "18: Exit (q)    " + " "*int(terWdt/10) + "19: Remove VG   " + " "*int(terWdt/10) + "20: Remove LV   " + " "*int(terWdt/10))
	print()
	print(terWdt * "_")
	system('tput setaf 7')
	print("\n")

def commands(headstr,terHgt,terWdt):
	while True:
		headbar('LVM TUI',terHgt,terWdt)
		menuOptions(terHgt,terWdt)
		choice = str(input("Enter Choice: "))
		print()
		if choice == '1':
			listDisks()
		elif choice=='2':
			listPVs()
		elif choice=='3':
			listVGs()
		elif choice=='4':
			listLVs()
		elif choice=='5':
			formatDisk()
		elif choice=='6':
			createPV()
		elif choice=='7':
			createVG()
		elif choice=='8':
			createLV()
		elif choice=='9':
			mountUmountDisk()
		elif choice=='10':
			movePV()
		elif choice=='11':
			extendVG()
		elif choice=='12':
			extendLV()
		elif choice=='13':
			fdiskutil()
		elif choice=='14':
			removePV()
		elif choice=='15':
			reduceVG()
		elif choice=='16':
			reduceLV()
		elif choice=='17':
			getShell()
		elif choice=='19':
			removeVG()
		elif choice=='20':
			removeLV()
		elif choice in ['18','q','quit','exit','Q','Quit','Exit']:
			return 'Exit'
		else :
			print("PLEASE ENTER A VALID INPUT")

		print()
		input("Press Enter... ")
		system('clear')
