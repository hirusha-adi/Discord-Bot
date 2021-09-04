import pyautogui
from time import sleep

def send(text):
    pyautogui.typewrite(text)
    pyautogui.press('enter')

sleep(1.5)
send("[!] Starting progressive scan on target")


sleep(3)
send("Scan report for <@tia>")
sleep(0.5)
send("Host is up")
sleep(2)
send("""
STATE   SERVICE     VERSION
Online  2,3,8       Windows 10
100024  6,2,9       rpcbind   
100024  6,2,9       46066/TCP   

[!!] FATAL ERROR! LOST CONNECTION TO TARGETS DISCORD ACCOUNT!
""")
sleep(4)
send("Device Type: Laptop")
sleep(0.5)
send("OS Details: 0.19043.1202")
send("[+] SCAN COMPLETED!")







