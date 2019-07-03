#!/usr/bin/python3

# Requires Python version 3 for "requests" module

# Determine if a password has been pwned and is listed in known compromised
# password lists without actually sending the password or its full hash.
# This makes use of Troy Hunt's "haveibeenpwned.com" API to search 500M+
# breached passwords.


import hashlib
import requests

base_url = "https://api.pwnedpasswords.com/range/"

# Step 0: Get the password from the user
password = input("Enter a password to check: ")

# Step 1: Calculate the password hashes
hash = hashlib.sha1(password.encode('utf-8')).hexdigest()
hash_left = hash[:5]
hash_right = hash[5:].upper()

print("Hashes: " + hash_left + " " + hash_right)

# Step 2: Request a list of possible matches
full_url = base_url + hash_left

r = requests.get(full_url)
if r.status_code != 200:
  print("API request failed. Error: " + r.status_code + " " + r.reason)
  exit()

# Step 3: Parse the list and look for a match
working_list = r.text.split("\r\n")

result = next((s for s in working_list if hash_right in s), None)

if result == None:
  print("No matches found. Yay!")
else:
  print("Your password matched " + result.split(":")[1] + " lists.")
