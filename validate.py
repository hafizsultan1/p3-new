import re

email = input ("enter your email? ").strip()

#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
 # [^@] any character except the @ sign + (any number of characters before +)
if re.search(r"^\w+@\w+\.edu|com|gov", email):
    print ("valid")
else:
    print ("invalid")

'''
import re
email = input ("enter your email? ").strip()

username, domain = email.split("@")

if username and "." in domain and domain.endswith("edu."):
    print ("valid")
else:
    print ("invalid")
'''