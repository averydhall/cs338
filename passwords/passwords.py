#!/usr/bin/env python3

import hashlib
import binascii
from math import comb

def hash(word):
    password = word # type=string
    encoded_password = password.encode('utf-8') # type=bytes
    hasher = hashlib.sha256(encoded_password)
    digest = hasher.digest() # type=bytes
    digest_as_hex = binascii.hexlify(digest) # weirdly, still type=bytes
    digest_as_hex_string = digest_as_hex.decode('utf-8') # type=string
    return digest_as_hex_string

# For Part 1
# --------------------------------------

passwords_cracked = 0
hashes_computed = 0

words = [line.strip().lower() for line in open('words.txt')]
users = [line.split(":") for line in open('passwords1.txt')]

for word in words:
    h = hash(word)
    hashes_computed += 1
    for user in users:
        user_h = user[1]
        if (h == user_h):
            print(user[0] + ":" + word)
            passwords_cracked += 1
print("Number of hashes computed: " + str(hashes_computed))
print("Passwords cracked: " + str(passwords_cracked))


# For Part 2
# --------------------------------------

# passwords_cracked = 0
# hashes_computed = 0

# words = [line.strip().lower() for line in open('words.txt')]
# users2 = [line.split(":") for line in open('passwords2.txt')]

# for word1 in words:
#     for word2 in words:
#         combined_word = word1 + word2
#         h = hash(combined_word)
#         hashes_computed += 1
#         for user in users2:
#             user_h = user[1]
#             if (h == user_h):
#                 print(user[0] + ":" + combined_word)
#                 passwords_cracked += 1
# print("Passwords cracked: " + str(passwords_cracked))
# print("Hashes computed: " + str(hashes_computed))


# file3 = open("cracked3.txt", "a")
# passwords_cracked = 0
# hashes_computed = 0
# words = [line.strip().lower() for line in open('words.txt')]
# users = [line.split(":") for line in open('passwords3.txt')]
# salts = [i[1].split('$')[2] for i in users]
# hashes = [i[1].split('$')[3] for i in users]
# x = 0
# while x < len(users):
#     for word in words:
#         concat = salts[x] + word
#         h = hash(concat)
#         hashes_computed += 1
#         if (h == hashes[x]):
#             print(users[x][0] + ":" + word)
#             file3.write(users[x][0] + ":" + word + "\n")
#             passwords_cracked += 1
#     x += 1
            
# print("Number of hashes computed: " + str(hashes_computed))
# print("Passwords cracked: " + str(passwords_cracked))
# file3.close()