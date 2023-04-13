import socket, threading
import colorama
import os
import sys
import fade
from colorama import Fore
import time
m=Fore.MAGENTA
lm=Fore.LIGHTMAGENTA_EX
w=Fore.WHITE
lw=Fore.LIGHTWHITE_EX
black=Fore.LIGHTBLACK_EX
y=Fore.LIGHTYELLOW_EX
r=Fore.LIGHTRED_EX
g=Fore.GREEN
lg=Fore.LIGHTGREEN_EX
c=Fore.CYAN
lc=Fore.LIGHTCYAN_EX
blue=Fore.BLUE
lb=Fore.LIGHTBLUE_EX
os.system("@mode con cols=90 lines=40")
os.system("cls")
os.system(f"title ^>^>^> Noxius Pinger ^| Noxius Multitool 💔 ^| Made by 𝖋𝖗𝖆𝖓_𝖆𝖋𝖕_ ^<^<^<")
gui="""
        ╔═══════════════════════════════════════════════╗ ╔═══════════════╗
        ║      ╔╗╔╔═╗═╗ ╦╦╦ ╦╔═╗  ╔═╗╦╔╗╔╔═╗╔═╗╦═╗      ║ ║   fran_afp_   ║
        ║      ║║║║ ║╔╩╦╝║║ ║╚═╗  ╠═╝║║║║║ ╦║╣ ╠╦╝      ║ ╠═══════════════╣
        ║      ╝╚╝╚═╝╩ ╚═╩╚═╝╚═╝  ╩  ╩╝╚╝╚═╝╚═╝╩╚═      ║ ║  NoxiusOnTop  ║
        ╚═══════════════════════════════════════════════╝ ╚═══════════════╝
        ╔═════════════════════════════════════════════════════════════════╗
        ║           [!] Noxius Pinnger by fran_afp_#0001 [!]              ║
        ║                                                                 ║
        ║               [&] docs.projectnoxius.xyz [&]                    ║
        ╚═════════════════════════════════════════════════════════════════╝
"""

faded_gui=fade.brazil(gui)
print(faded_gui)
def tcpping(ip,port):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((ip,port))
        print(f"                {m}[{w}OK{m}] {g}Connection to {y}{ip} {lg}in port {y}{port} {lb}[{y}By Noxius{lb}] {m}[{w}OK{m}]")
    except:
        print(f"                        {m}[{w}HIT{m}] {r}Oops {y}{ip} {r}is down {lb}[{y}By Noxius{lb}]")

ip = input(f"{m}[{w}>>>{m}] {black}IP:{y} ")
print("")
port = input(f"{m}[{w}>>>{m}] {black}Port:{y} ")
print("")
while True:
    try:
        os.system(f"title - Noxius Pinger ^| Noxius Multitool 💔 ^| Made by 𝖋𝖗𝖆𝖓_𝖆𝖋𝖕_ ^| Ping to {ip} in port {port} -")
        tcpping(ip,int(port))
        time.sleep(0.25)
    except KeyboardInterrupt:
        exit(0)
