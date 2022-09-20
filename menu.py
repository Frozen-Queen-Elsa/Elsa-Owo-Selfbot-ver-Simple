import os, time, sys
from version import version
from color import color
class UI:

	@classmethod
	def slowPrinting (cls, text):
		for letter in text:
			sys.stdout.write(letter)
			sys.stdout.flush()

			time.sleep(0.000001)
		print()

	@classmethod
	def logo(cls):
		print(f'{color.okcyan}{elsa}{color.reset}')
		print(f"                   {color.purple}Version: {version} moded VIP{color.reset}")
		time.sleep(0.5)
		print()
		print("╔═════════════════════════════════════════════════════════════════════════════════╗")
		print()
		print(f" {color.yellow}This is the moded auto by {color.okcyan}Iris {color.yellow}({color.okcyan}ThanhThanh2k7{color.yellow}). {color.reset}")
		print(f" {color.yellow}Thanks to {color.okcyan}ahihiyou20{color.yellow} for the original version{color.reset}")
		print(f" {color.yellow}Thanks to {color.okcyan}Naru2203{color.yellow} for the auto owo slot version{color.reset}")
		print()
		print("╚═════════════════════════════════════════════════════════════════════════════════╝")
		print()
		time.sleep(1) 

	@classmethod
	def start(cls):
		print("╔═══════════════════════════════╗")
		print()
		print(f"       {color.purple}[1]{color.reset} Load Data")
		print(f"       {color.purple}[2]{color.reset} Create New data")
		print(f"       {color.purple}[3]{color.reset} Additional Info")
		print()
		print("╚═══════════════════════════════╝")



	@classmethod
	def newData(cls):
		print("╔═══════════════════════════════════════════╗")
		print()
		print("         [0] Exit And Save")
		print("         [1] Change All Settings")
		print("         [2] Change Token")
		print("         [3] Change Channel")
		print("         [4] Change Auto Setting")
		print("         [5] Change Pray/Curse Mode")
		print("         [6] Change Gems Mode")
		print("         [7] Change Exp Mode")
		print("         [8] Change Sleep Mode")
		print("         [9] Change Webhook Settings")
		print("         [10] Change Selfbot Commands")
		print("         [11] Change Daily Mode")
		print("         [12] Change Stop Time")
		print("         [13] Chage Sell Mode")
		print("         [14] Change Solve Captcha")
		print("         [15] Change Owo Casino Setting")
		#print("         [16] Change Sound Music Setting")
		print("         [16] Change API 2Capcha Setting")		
		print()
		print("╚═══════════════════════════════════════════╝")
	@classmethod
	def info(cls):
		print(f"{color.purple}╔═════════════════Support════════════════╗{color.reset}")
		print(f"\t{color.purple}https://discord.gg/9uZ6eXFPHD{color.reset}")
		print(" ")
		print(f"{color.purple}╔═══════════════════════════════════════════════════════════════════════════Disclaimer═══════════════════════════════════════════════════════╗{color.reset}")
		print(f"\t{color.purple}This SelfBot Is Only For Education Purpose Only. Deny All Other Promises Or Responsibilities. Use The SelfBot At Your Own Risk.")
		print(" ")
		print(f'{color.purple}╔═════════════════Credit═════════════════╗{color.reset}')
		print(f'\t{color.purple} [Developer] {color.reset} Sudo-Nizel')
		print(f'\t{color.purple} [Developer] {color.reset} ahihiyou20')
		print(" ")
		print(f'{color.purple}╔═════════════════════════Selfbot Commands════════════════════════╗{color.reset}')
		print("\t{Prefix}send {Message} [Send Your Provied Message}")
		print("\t{Prefix}restart [Restart The Selfbot]")
		print("\t{Prefix}exit [Stop The Selfbot]")
		print("\t{Prefix}sm {on/off} [Turn On Or Off Sleep Mode]")
		print("\t{Prefix}em {on/off} [Turn On Or Off Exp Mode]")
		print("\t{Prefix}pm {on/off} [Turn On Or Off Pray Mode]")
		print("\t{Prefix}gm {on/off} [Turn On Or Off Gems Mode]")
		print("\t{Prefix}gems [Use Gems]")
		print(" ")
		print("{Prefix} == Your Prefix")
		print(" ")
		print("Note: Alright If You See Someone Selling This Code Then You Got Scammed Because This Code Is Free!")
		time.sleep(0.5)
		print("Press Enter To Exit")
		input()


elsa='''\
███████╗██╗     ███████╗ █████╗                                                           
██╔════╝██║     ██╔════╝██╔══██╗                                                          
█████╗  ██║     ███████╗███████║                                                          
██╔══╝  ██║     ╚════██║██╔══██║                                                          
███████╗███████╗███████║██║  ██║                                                          
╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝                                                          
                                                                                          
 ██████╗ ██╗    ██╗ ██████╗     ███████╗███████╗██╗     ███████╗██████╗  ██████╗ ████████╗
██╔═══██╗██║    ██║██╔═══██╗    ██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝
██║   ██║██║ █╗ ██║██║   ██║    ███████╗█████╗  ██║     █████╗  ██████╔╝██║   ██║   ██║   
██║   ██║██║███╗██║██║   ██║    ╚════██║██╔══╝  ██║     ██╔══╝  ██╔══██╗██║   ██║   ██║   
╚██████╔╝╚███╔███╔╝╚██████╔╝    ███████║███████╗███████╗██║     ██████╔╝╚██████╔╝   ██║   
 ╚═════╝  ╚══╝╚══╝  ╚═════╝     ╚══════╝╚══════╝╚══════╝╚═╝     ╚═════╝  ╚═════╝    ╚═╝   
                                                                                          
'''
