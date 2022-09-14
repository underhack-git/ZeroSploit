import os, random, subprocess, sys
from methods import methods
from colorama import Fore, init
os.system ("clear")
try:
    list_files = subprocess.run(["adb"], stdout=subprocess.DEVNULL)
    if 1 == list_files.returncode:
        print (Fore.GREEN+"adb is installed!\n"+Fore.WHITE)
except:
    print(Fore.RED+"adb is not installed!")
    input = input("{0}install adb{1}[{2}y{1}/{2}n{1}]: ".format(Fore.BLUE, Fore.WHITE, Fore.GREEN))
    if input == "y":
        try:
            os.system("pkg install adbapt update && apt install wget && wget https://github.com/MasterDevX/Termux-ADB/raw/master/InstallTools.sh &")
            os.system("apt install adb")
            os.system("apt-get install adb")
        except:
            print(Fore.RED+"Failed to install")
            sys.exit(0)
    elif input == "n":
        print (Fore.RED+"without adb will not work"+Fore.WHITE)
        sys.exit()
    else:
        print("error")
        sys.exit()
#=====================================
banner = '''
\033[92m
          +hydNNNNdyh+
        +mMMMMMMMMMMMMm+
      `dMMm\033[0m:\033[92mNMMMMMMN\033[0m:\033[92mmMMd`
      hMMMMMMMMMMMMMMMMMMh
  \033[92m..  yyyyyyyyyyyyyyyyyyyy  ..
\033[92m.mMMm`MMMMMMMMMMMMMMMMMMMM`mMMm.            \033[0m Created by Deiwan\033[92m
\033[92m:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
 MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM
 +yy+ MMMMMMMMMMMMMMMMMMMM +yy+
      mMMMMMMMMMMMMMMMMMMm
      `\++MMMMh++hMMMM++/`
          MMMMo  oMMMM
          MMMMo  oMMMM
          oNMm-  -mMИs\n'''
os.system("adb tcpip 5555")
print(Fore.BLUE+"           ZEROSPLOIT")
print(banner)
data = '''
{0}[{1}1{0}]  {2}Show Connected Devices     
{0}[{1}2{0}]  {2}Restart Server  
{0}[{1}3{0}]  {2}Connect / Disconnect
{0}[{1}4{0}]  {2}Access Shell on a phone    
{0}[{1}5{0}]  {2}APK management  
{0}[{1}6{0}]  {2}Screenshot/record              
{0}[{1}7{0}]  {2}Show real time log of device    
{0}[{1}8{0}]  {2}Reboots menu                    
{0}[{1}9{0}]  {2}Storage manager
{0}[{1}10{0}] {2}Dump System Info 
{0}[{1}11{0}] {2}Get Battery Status
{0}[{1}12{0}] {2}Internet manager
{0}[{1}13{0}] {2}Remove Password
{0}[{1}14{0}] {2}Use Keycode
{0}[{1}15{0}] {2}Get Current Activity         
{0}[{1}16{0}] {2}use custom adb command\n
{0}[{1}99{0}] {2}Exit   {0}[{1}0{0}] {2}Clear
'''.format(Fore.CYAN, Fore.RED, Fore.GREEN)
print (Fore.RED+"""list script commands""")
print (data)
md = methods
try:
    while True:
        option = input(Fore.GREEN + "zerosploit"+Fore.RED + "(menu) "+Fore.WHITE + "> ")
        if option == "0":
            os.system("clear")
            print (banner)
            print (data)
        elif option == "1":
            md.print_devices(md)
        elif option == "2": 
            os.system("adb kill-server && adb start-server")
        elif option == "3":
            md.connect(md)
        elif option == "4":
            md.shell(md)
        elif option == "5":
            md.APK_management(md)
        elif option == "6":
            md.screens(md)
        elif option == "7":
            md.log(md)
        elif option == "8":
            md.reboots_menu(md)
        elif option == "9":
            md.storage_meneger(md)
        elif option == "10":
            md.dumpsys(md)
        elif option == "11":
            md.battery(md)
        elif option == "12":
    	    md.inter_manager(md)
        elif option == "13":
    	    md.rm_pass(md)
        elif option == "14":
            md.keycode(md)
        elif option == "15":
    	    md.activity(md)
        elif option =="16":
    	    md.custom_command(md)
        elif option == "99":
            os.system("adb disconnect")
            print (Fore.GREEN+"\nThank you for using ZeroSploit!\n\n"+Fore.BLUE+"sucessfully exit...\n"+Fore.WHITE)
            sys.exit()
        else:
            print (Fore.RED+" invalid option")
except KeyboardInterrupt:
    os.system("echo && adb disconnect")
    print (Fore.GREEN+"\nThank you for using ZeroSploit!\n\n"+Fore.BLUE+"sucessfully exit...\n"+Fore.WHITE)
    sys.exit()
