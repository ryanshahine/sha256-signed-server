# -*- coding: utf-8 -*-
import urllib.request

import hashlib

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



url = "https://raw.githubusercontent.com/ryanshahine/sha256-signed-server/master/hash.txt"
file = urllib.request.urlopen(url)

for line in file:
    CurrentHash = line.decode("utf-8").rstrip()



print(bcolors.OKBLUE + "[ 👟 ] Authentication Server 0.1" + bcolors.ENDC)
API = input(bcolors.OKBLUE + "[ 👟 ] Insert API Key: " + bcolors.ENDC)
print(bcolors.OKBLUE + "[ 👟 ] API Key: " + API + " Approved" + bcolors.ENDC)
print(bcolors.OKGREEN + "[ ✅ ] Current approved SHA256 hash: " + bcolors.BOLD + bcolors.OKGREEN + CurrentHash + bcolors.ENDC)
print(bcolors.OKBLUE + "[ 🔎 ] Obtaining hash.." + bcolors.ENDC)


# filename = input("Enter the input file name: ")
# filename = server.py
with open('verify.py',"rb") as f:
    bytes = f.read() # read entire file as bytes
    readable_hash = hashlib.sha256(bytes).hexdigest();
print(bcolors.OKGREEN + "[ ✅ ] Successfully obtained SHA-256 hash: " + bcolors.BOLD + bcolors.OKGREEN + readable_hash)

if CurrentHash == readable_hash:
    print(bcolors.OKGREEN + bcolors.BOLD + "[ ✅ ] Server is up to date." + bcolors.ENDC)

else:
    print(bcolors.FAIL + "[ ❌ ] Error: Incorrect hash" + bcolors.ENDC)

