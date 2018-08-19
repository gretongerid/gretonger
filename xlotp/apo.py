# -*- coding: utf-8 -*-
import os
import sys
import platform
import time
from xlpy import *
import base64

g = "\033[32;1m"
gt = "\033[0;32m"
bt = "\033[34;1m"
b = "\033[36;1m"
m = "\033[31;1m"
c = "\033[0m"
p = "\033[37;1m"
u = "\033[35;1m"
M = "\033[3;1m"
k = "\033[33;1m"
kt = "\033[0;33m"
a = "\033[30;1m"

W = '\x1b[0m'
R = '\x1b[31m'
G = '\x1b[1;32m'
O = '\x1b[33m'
B = '\x1b[34m'
P = '\x1b[35m'
C = '\x1b[36m'
GR = '\x1b[37m'



def slowprints(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.0/90)
def lodprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(7.0/90)

=(gt+"""
#############   #############
#############   #############
###                  ###
###  ########        ###
###  ########        ###
###       ###        ###
#############        ###
#############        ###
 =================================
""")
l="Harap tunggu.."

def main_menu():
    clear()
    slowprints()
    print(p+
        "   Tembak Xl Mode OTP GT.30" +
        "\nPilih Salah Satu:"
        "\n  [1] Menu Beli Paket" + 
        "\n  [2] Minta  Kode OTP" +
        "\n  [3] Menu utama"
    )
    choice = str(input(" ex:1👉 "))
    exec_menu(choice)
    return

def exec_menu(choice):
    clear()
    if(choice == ''):
        menu_actions['main']()
    else:
        try:
            menu_actions[choice]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main']()
    return

def menu_1():
    lodprint(l)
    clear()
    print()
    print(p+"Menu Beli Paket XL")
    msisdn = str(input("Masukan No 62xx 👉 "))
    clear()
    print()
    po = str(input(p+"Masukan Kode Otp 👉 "))
    clear()
        print()
    print (p+" 1.Xtra Kuota 30GB, 30day, 10K")
    print (p+" 2.Xtra 3GB, 30day, 22.9K ")
    print (p+" 3.Xtra 5GB, 30day, 32.9K ")
    print (p+" 4.Xtra 9GB, 30day, 52.9K ")
    print (p+" 5.Xtra 17GB, 30day, 82.9K ")
    print (p+" 6.Xtra 25GB, 30day, 102.9K ")
    print (p+" 7.Combo Xtra 5GB+5GB, 30day, 59K ")
    print (p+" 8.Combo Xtra 10GB+10GB, 30day, 89K ")
    print (p+" 9.Combo Xtra 15GB+15GB, 30day, 129K ")
    print (p+" 10.HOTROD 24Jam 1,5GB, 30day, 25K ")
    print (p+" 11.HOTROD 24Jam 3GB, 30day, 30K ")
    print (p+" 12.HOTROD 24Jam 6GB, 30day, 50K ")
    print (p+" 13.SuperSeru Nelpon (49932Menit) & SMS (249999), 30day, 15K ")  
    print (p+" 14.Kuota 700mb 10k")
    print (p+" 15.Xtra 10GB 30day 59k")
    print (p+" 16.Manual service id")
    pkt = str(input("Pilih Sesuai Keinginan >> "))
    
    if pkt == '1':
        i = '8110577'
    elif pkt == '2':
        i = '8211010'
    elif pkt == '3':
        i = '8211011'
    elif pkt == '4':
        i = '8211012'
    elif pkt == '5':
        i = '8211013'
    elif pkt == '6':
        i = '8211014'
    elif pkt == '7':
        i = '8211183'
    elif pkt == '8':
        i = '8211184'
    elif pkt == '9':
        i = '8211185'
    elif pkt == '10':
        i = '8211107'
    elif pkt == '11':
        i = '8211108'       
      elif pkt == '12':
        i = '8211109'
    elif pkt == '13':
        i = '8210965'
    elif pkt == '14':
        i = '8211170'
    elif pkt == '15':
        i ='8211183'
    elif pkt == '16':
        i = str(input("Service ID Paket👉"))
    else:
        print("Pilihan gak tercantum")
    lodprint(l)
    serviceid = i
    xl = XL(msisdn)
    r = xl.loginWithOTP(po)
    if(r != False):
        print(xl.purchasePackage(serviceid)['message'])
        decision = str(input(p+"Ulangi Proses [Y/N]? 👉 "))
        menu_actions['main']() if(decision in ['N','n']) else menu_actions['1']()
        
def menu_2():
    lodprint(l)
    clear()
    print()
    print(p+"Minta Kode Otp")
    msisdn = str(input("Masukan Nomor 62xx👉"))
    lodprint(l)
    xl = XL(msisdn)
    print(xl.reqOTP()['message'])
    decision = str(input(p+"Ulangi Proses[Y/N]? 👉 "))
    menu_actions['main']() if(decision in ['N','n']) else menu_2()

def menu_4():
    clear()
    print(".::Password Menu::.")
    msisdn = str(input("Input your NomerHp >> "))
    xl = XL(msisdn)
    print(xl.reqPassword()['message'])
    decision = str(input("Kamu Ingin Megulangi Proses [Y/N]? >> "))
    menu_actions['main']() if(decision in ['N','n']) else menu_actions['3']()
    return

def menu_3():
     lodprint(l)
     os.system('cd ..;python GT.py')


def exit():
    sys.exit()

def clear():
    return os.system("cls") if (platform.system() == 'Windows') else os.system("clear")

menu_actions = {
    "main" : main_menu,
    "1" : menu_1,
    "2" : menu_2,
    "3" : menu_3,
    "0" : exit
}


if __name__ == "__main__":
    main_menu()
