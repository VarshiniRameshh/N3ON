import requests
import sys
import os

def banner():
  print "HI EVERYONE!"
  print "FOUNDER: VARSHINI RAMESH & V.SURYA"
  print "TOOL NAME:N3ON"
  
def N3ON(domain):
    with open("domain.txt","r") as f:
       for i in f:
           sub_domain = i.strip()
           url = sub_domain + "." + domain
           try:
               os.system("bash .v1l03t " + url)
               sys.exit()
              
           except:
                pass

if len(sys.argv) < 2:
     banner()
     print("Syntax")
     print("python N3ON.py Domain_Name | tee -a filename.txt")
     print("Please just enter domain like: google.com not www.google.com")
     print("Example")
     print("python N3ON.py google.com | tee -a filename.txt ")
else:
     domain = sys.argv[1]
     N3ON(domain)
           

