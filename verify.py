
# -*- coding: utf-8 -*-

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


CurrentHash = 'INPUT HASH'

print(bcolors.OKBLUE + "[ 👟 ] Authentication Server 0.1" + bcolors.ENDC)
print(bcolors.OKGREEN + "[ ✅ ] Current approved SHA256 hash: " + bcolors.BOLD + bcolors.OKGREEN + CurrentHash + bcolors.ENDC)
print(bcolors.OKBLUE + "[ 🔎 ] Obtaining hash.." + bcolors.ENDC)


# filename = input("Enter the input file name: ")
# filename = server.py
with open('server.py',"rb") as f:
    bytes = f.read() # read entire file as bytes
    readable_hash = hashlib.sha256(bytes).hexdigest();
print(bcolors.OKGREEN + "[ ✅ ] Successfully obtained SHA-256 hash: " + bcolors.BOLD + bcolors.OKGREEN + readable_hash)

if CurrentHash == readable_hash:
    print(bcolors.OKGREEN + bcolors.BOLD + "[ ✅ ] Server is up to date." + bcolors.ENDC)

else:
    print('Error')


