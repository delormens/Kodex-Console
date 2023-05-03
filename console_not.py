import cmd
import time
import re
from colorama import init, Fore
import signal
import random
import os
import socket
import requests
from pyfiglet import Figlet
import folium
from SimpleQIWI import *
import os, sys
from time import sleep
import scapy.all as scapy
import argparse
import subprocess
import psutil
import ctypes
import pyscreenshot as ImageGrab
import tkinter as tk
import pywifi
from pywifi import const
from comtypes import GUID
import smtplib as smtp
from getpass import getpass

################################################################################
#                           ОБНОВЛЕНИЕ                                        #
################################################################################ 
current_version = '1.0'

def check_update():
    # выполнить запрос на ваш сайт или GitHub
    response = requests.get('https://github.com/delormens/Butterfly/blob/console/version.txt')
    new_version = response.text.strip()
    if new_version > current_version:
        # вернуть ссылку для скачивания обновления
        return new_version, 'https://github.com/delormens/Butterfly/blob/console/console_not.py'
    else:
        return None

def update():
    new_version, update_url = check_update()
    if update_url:
        print('A new version of the program is available!')
        print('Current version: ', current_version)
        print('New version: ', new_version)
        answer = input('Would you like to download a new version? [Y/n] ').strip().lower()
        if answer == 'y':
            response = requests.get(update_url)
            with open('butterfly.py', 'wb') as f:
                f.write(response.content)
            print('The new version has been uploaded.')
        else:
            return
    else:
        print('No update is required.')

update()


################################################################################
#                           РЕГИСТРАЦИЯ                                        #
################################################################################     

class PasswordConsole(cmd.Cmd):
    os.system("cls")
    intro = 'Welcome to our authorization system. To register, enter "register", to log in - "login".'
    prompt = Fore.WHITE + '> '
    users = {'DELORMEN': '12345', 'VeLson': '123456789', 'Admin': 'Admin'}

    def __init__(self):
        super().__init__()
        self.registered = False

    def precmd(self, line):
        if not self.registered and not line.startswith('register') and not line.startswith('login'):
            print("[!] Please log in to use the functions")
            return ''
        return line

    def do_register(self, arg):
        '[*] User Registration'
        username = input("Enter the username: ")
        while username in self.users:
            username = input("[X] This user already exists, please enter a different name: ")
        password = input("Enter the password: ")
        self.users[username] = password
        print("[+] User {} registered".format(username))

    def do_logout(self, arg):
        '[*] Logout'
        self.registered = False
        print('[!] You are logged out')

    def do_login(self, arg):
        '[*] Log in to the system'
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        os.system("cls")
        if username in self.users and self.users[username] == password:
            self.registered = True
            #print("[+] Successfully logged in as {}".format(username))
        else:
            print("[X] Incorrect username or password")
        print(Fore.LIGHTWHITE_EX + f"""
                                                                                 .:^~!!!777!!~^::.    
   :~!7J55PGP555YJ?7!~:.                                                 .::~?Y555PPPGBBG##&##55Y7. 
.?GG5&&&#BPPGPP555555Y7!?J7~.        ..                   .:.        :~?5GY77JYYYYYYY55P5GB#&&BB&&G:          Welcome to Hacker Console           
G&&GB&&#BGGP55YYYYJJJYYYP###B5?~.    .^^.               .^^.     .^?PB###BP5YYJJJJJJJJYY5PB#&&#YB&&7          The server is running
#&#P#&&#BP5YYYYYJJJYYYYYY555PGBBG57:   .:^.           .:^.    .!YGBBGP5YYJJJJYYYJJJJJYYYYPG#&#G#&&Y.          Version: Not
~B&&PP&#BGP55YYYJYYYYYJ?JJJJYY55PBBB57:   :^.        :^.    ~JG#BGP5YYJJ?????JJJJJJJJJJJ5G#&&#G##J.           User: {username}
 :G&##&##BP55YYYYYJJJYYJJJJJJJJY55PGB#B5!.  :^:    :^.   :?P#BGPP5YYJJJ?JJJJJJ????JJYY55G#&B5#@&?             [!] Buy the premium version
  :Y#&PG&#BG55YYJJJJJJJJJYYJJJJJYY55PPGB#G?.  :^.:::   :JB#BGP555YYYJJJJJJJJJJJJ??JJYY5P#&&&#&J^    
    :P&&&&#BP5YYYJJJJJJJJJJJJJYYYY5555PPGB#G?. ~PBY: .JB#BGP555555YYJJJJ??????JJJJJY55G#&GB&&J      
     :P&B5&&BG55YYJJJJJJJJJJJJJJYY55555PPGGB#G7?&&&77G#BGPPP5555YYYJJJJJJJ??????JJJY5P#&&B#G~       
       ?&#&&#G55YYJYJJJJJJJJJJJJJJYYYY555PPGB##B&&&B#BBGPP55YYYYJJJJJJJJJJJJJJJJJJYY5G#&&&@7        
       .B@#B#BP5555YYJJJJJJJJJJJJJYYYY555PPGGGB######BBGPPP55YYYYJJJJ????????JJJYY5PG#&BG&5.        
        ~P#B&&BG55YYJJJJJJJJJJJJJYYYY555PPPPGGB#####BGGPPP555YYYYYJJJJJJJJJJJJJJJY5P#&&&@J          
         .B@&##BP5YYYYYYYYYJJJYYYYYYYYY555PPPGG#####BGP55555YYYYYYYYYYYJJJJJJJYYY5PB&##&5.          
          ^Y##&&BG55YYYYYYYYYYYJJJJYYYYYYY55PPG#####BPP5YYYYYYYYJJJJYYYY5555YYYY5B&&&#5^            
            ^JG##BPPPPPP555YYJJJJJJJYJJJYYY555G#####BP55YYYYJJYJJJJJJJJYY55PGGBG5J??!:              
              .::!P##BGP5YYJJJJJJJJJJJJJJYY5YYG######G5YYYYJJJJJJJJJJJJJYY55G##&#G7                 
                ?##&&#G55YYJJJJJJJJJJJJJJJYYY5B######G5JYJJJJJJJJJJJJJJYYY5PB#&&#&#^                
                P&&&&#BG55YYJJJJJJJJJJJJJJYYYPB######BPJJYJJJJJJJJJJJJJYY5PG#&&&&&@7                
               ^#&##&&&BP5YYYJJJJJJJJJJJYYYY5GB&5JY&##GYJYJJJJJJJJJJJJYY55P#&&&##&5^                
               .J###&&&#BP55YYYYYJJJJJJYYYYYPBB&!  G##B5YYYYJJJJJJJYY5Y55GB&&&&&@J                  
                 ?@&&&&&#BP55P5YJJJYYYYYY55PGB##^  7&#BG5YYYYJJYYJYYYPGPPB&&&&#@@^                  
                 ^#@##&&&#BBBG5YYYY5YYYY555GBB#G.  :B#BBP555YYYY5YYY5PB##&&&&&#Y!                   
                  :?#&&&&&&&&BP555P55Y55PPPGBB#Y    5#BBG55555555PPPPG#&&&&&&@?                     
                    ?@&&&&&&&#GGGGGPP5PPPPGB#B#7    !&B#BPP5PP55PPBBBB&&&&&#&#:                     
                    .P&#&&&&&&#&#BGGPGGBGBBB#B5.    .JG#BBBGBGPPPG#&&&&&&&&#7:                      
                      ~G@&&&&&&&&&BGB######G7:        .^5#####BBB#&&&&&&@@@?                        
                       :B@@&&&&&&&&######B?:             !Y#&&&&&&&&&&&#PYJ.                        
                        :??YB@&&&&&&&&&BY^                 ^J#@@@&#&@@B^                            
                            .JB#GPPBBG?:                     ^JP5!^^77:                             
                              .:.  ...                                                           
    """)


    def default(self, arg):
        print("Command not found:", arg)

################################################################################
#                           ОСНОВНЫЕ ФУНКЦИИ                                   #
################################################################################

    def do_device(self, arg):
            '[*] List of hacked devices'
            print("IP\t\t\tMAC Address\t\t\tDevice\n========================================================================")
            print("193.22.244.255          B8:7B:C5:6D:46:0E               iPhone 11")
            print("216.217.192.66          8C:1A:DE:07:17:32               Samsung A50")
            print("203.225.103.115         80:19:70:0D:7F:96               Samsung A23")
            print("76.153.138.214          A8:91:3D:C6:FB:12               iPhone XR")
            print("4.45.38.243             9F:AE:2E:ED:BD:5D               iPhone X")   
            print("176.13.41.56            CC:C9:5D:92:A4:0C               iPhone 12")
            print("77.145.196.172          D8:06:06:64:8C:C1               Apple Watch 6")
            print("91.190.152.132          D4:DC:CD:AD:AF:5B               iPhone 7+")
            print("87.60.140.153           6C:C7:EC:78:15:2D               Samsung S9+")
            print("234.144.195.51          9C:28:C8:F7:91:6E               Realme 10a")
            print("133.77.25.197           E8:6D:CB:E5:8A:34               Samsung A51")
            print("131.54.6.178            E8:7F:95:87:B1:40               iPhone SE")
            print("89.204.243.48           6C:43:3C:82:41:D5               Not defined")
            print("61.80.234.120           8D:87:37:83:7E:0C               HONOR 9X")

    def do_buy(self, arg):
        '[*] Buy Premium'
        os.system('start chrome https://vk.com/im?media=&sel=605967506')

    def do_deleted(self, arg):
        '[*] Deleted a device'
        txt = Fore.LIGHTRED_EX + '[!] To unlock all functions, you need to purchase Premium\n' + Fore.WHITE
        for i in txt:
            time.sleep(0.1)
            print(i, end='', flush=True)

    def do_clear(self, arg):
        '[*] Clear Console'
        os.system('cls')

    def do_genpass(self, arg):
        '[*] Password generation'
        txt = Fore.LIGHTRED_EX + '[!] To unlock all functions, you need to purchase Premium\n' + Fore.WHITE
        for i in txt:
            time.sleep(0.1)
            print(i, end='', flush=True)

    def do_hackpass(self, arg):
        '[*] Password Bruteforce'
        txt = Fore.LIGHTRED_EX + '[!] To unlock all functions, you need to purchase Premium\n' + Fore.WHITE
        for i in txt:
            time.sleep(0.1)
            print(i, end='', flush=True)

    def do_binary(self, arg):
        '[*] Binary converter'
        txt = Fore.LIGHTRED_EX + '[!] To unlock all functions, you need to purchase Premium\n' + Fore.WHITE
        for i in txt:
            time.sleep(0.1)
            print(i, end='', flush=True)

    def do_ddos(self, arg):
        '[*] DDos'
        txt = Fore.LIGHTRED_EX + '[!] To unlock all functions, you need to purchase Premium\n' + Fore.WHITE
        for i in txt:
            time.sleep(0.1)
            print(i, end='', flush=True)

    def do_qiwi(self, arg):
        '[*] Qiwi Balance Check'
        txt = Fore.LIGHTRED_EX + '[!] To unlock all functions, you need to purchase Premium\n' + Fore.WHITE
        for i in txt:
            time.sleep(0.1)
            print(i, end='', flush=True)

    def do_phone(self, arg):
        '[*] Phone Info'       
        txt = Fore.LIGHTRED_EX + '[!] To unlock all functions, you need to purchase Premium\n' + Fore.WHITE
        for i in txt:
            time.sleep(0.1)
            print(i, end='', flush=True)

    def do_network(self, arg):
        '[*] Network scanner'
        txt = Fore.LIGHTRED_EX + '[!] To unlock all functions, you need to purchase Premium\n' + Fore.WHITE
        for i in txt:
            time.sleep(0.1)
            print(i, end='', flush=True)

    def do_mac(self, arg):
        '[*] Mac Changer'
        txt = Fore.LIGHTRED_EX + '[!] To unlock all functions, you need to purchase Premium\n' + Fore.WHITE
        for i in txt:
            time.sleep(0.1)
            print(i, end='', flush=True)

    def do_site(self, arg):
        '[*] Our website'
        os.system('start chrome https://delormen.com')

    def do_ping(self, arg):
        '[*] Ping IP'
        txt = Fore.LIGHTRED_EX + '[!] To unlock all functions, you need to purchase Premium\n' + Fore.WHITE
        for i in txt:
            time.sleep(0.1)
            print(i, end='', flush=True)

    def do_search(self, arg):
        '[*] Internet search'
        txt = Fore.LIGHTRED_EX + '[!] To unlock all functions, you need to purchase Premium\n' + Fore.WHITE
        for i in txt:
            time.sleep(0.1)
            print(i, end='', flush=True)

    def do_caps(self, arg):
        '[*] Register Converter'
        txt = Fore.LIGHTRED_EX + '[!] To unlock all functions, you need to purchase Premium\n' + Fore.WHITE
        for i in txt:
            time.sleep(0.1)
            print(i, end='', flush=True)

################################################################################
#                         ФУНКЦИИ РЕГИСТРАЦИИ И КОНСОЛИ                        #
################################################################################

    def do_resetpass(self, arg):
        '[*] Reset password'
        txt = Fore.LIGHTRED_EX + '[!] To unlock all functions, you need to purchase Premium\n' + Fore.WHITE
        for i in txt:
            time.sleep(0.1)
            print(i, end='', flush=True)

    def do_reload(self, arg):
        '[*] Reload Console'
        print("[!] In development...")

################################################################################
#                         ТРОЯНЫ, ВИРУСЫ, РАТНИКИ                              #
################################################################################

    def do_antivirus(self, arg):
        '[!] Need administrator rights [!]\n[*] Checking your PC for viruses'
        txt = Fore.LIGHTRED_EX + '[!] To unlock all functions, you need to purchase Premium\n' + Fore.WHITE
        for i in txt:
            time.sleep(0.1)
            print(i, end='', flush=True)

    def do_virus(self, arg):
        '[*] Infect a PC with a virus'
        txt = Fore.LIGHTRED_EX + '[!] To unlock all functions, you need to purchase Premium\n' + Fore.WHITE
        for i in txt:
            time.sleep(0.1)
            print(i, end='', flush=True)


    def do_delfile(self, arg):
        '[!] Need administrator rights [!]\n[*] Self-destruct'
        txt = Fore.LIGHTRED_EX + '[!] To unlock all functions, you need to purchase Premium\n' + Fore.WHITE
        for i in txt:
            time.sleep(0.1)
            print(i, end='', flush=True)

    def do_cd(self, arg):
        '[!] Need administrator rights [!]\n[*] The script gets into the main folder of the PC'
        txt = Fore.LIGHTRED_EX + '[!] To unlock all functions, you need to purchase Premium\n' + Fore.WHITE
        for i in txt:
            time.sleep(0.1)
            print(i, end='', flush=True)

    def do_image(self, arg):
        '[*] Takes a screenshot and sends it to you'
        txt = Fore.LIGHTRED_EX + '[!] To unlock all functions, you need to purchase Premium\n' + Fore.WHITE
        for i in txt:
            time.sleep(0.1)
            print(i, end='', flush=True)

    def do_trojan(self, arg):
        '[*] Trojan'
        def trojan():
            txt = Fore.LIGHTRED_EX + '[!] To unlock all functions, you need to purchase Premium\n' + Fore.WHITE
        for i in txt:
            time.sleep(0.1)
            print(i, end='', flush=True)



################################################################################
#                         ПРАВА АДМИНИСТРАТОРА                                 #
#              [!] To unlock all functions, you need to purchase Premium              #
################################################################################


    def do_email(self, arg):
        '[*] Backconnect by mail'
        txt = Fore.LIGHTRED_EX + '[!] To unlock all functions, you need to purchase Premium\n' + Fore.WHITE
        for i in txt:
            time.sleep(0.1)
            print(i, end='', flush=True)

    def do_stealler(self, arg):
        '[*] Stealler'
        txt = Fore.LIGHTRED_EX + '[!] To unlock all functions, you need to purchase Premium\n' + Fore.WHITE
        for i in txt:
            time.sleep(0.1)
            print(i, end='', flush=True)

    def do_exit(self, arg):
        'Exit Console'
        print(Fore.LIGHTBLUE_EX + """        
   ______                ____               __
  / ____/___  ____  ____/ / /_  __  _____  / /
 / / __/ __ \/ __ \/ __  / __ \/ / / / _ \/ / 
/ /_/ / /_/ / /_/ / /_/ / /_/ / /_/ /  __/_/  
\____/\____/\____/\__,_/_.___/\__, /\___(_)   
                             /____/           
        """ + Fore.WHITE)
        time.sleep(1)
        os.system('cls')
        return True

def signal_handler(sig, frame):
   print(Fore.RED  + "[!] Attention! THE OPERATION WAS STOPPED USING CTRL+C [!]" + Fore.WHITE)
signal.signal(signal.SIGINT, signal_handler)

if __name__ == '__main__':
    PasswordConsole().cmdloop()
