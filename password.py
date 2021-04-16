#inspiration and reference from https://pynative.com/python-generate-random-string/

import random
import string

x = int(input("Please enter the length in characters of the password you want to generate: "))

pw_chars = string.ascii_letters + string.punctuation + string.digits

pw = ''.join(random.choice(pw_chars) for i in range(x))

print("Your password is: ")
print(pw)
