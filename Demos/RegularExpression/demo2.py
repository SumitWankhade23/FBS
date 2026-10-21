# import re
# email = input("Enter email id to check: ")
# pat = r"^[a-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2}$"
# res = re.search(pat,email)
# if res:
#     print("pattern found")
# else:
#     print("pattern not found")    

import re

email = input("Enter email id to check: ").strip()
pat = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"

if re.fullmatch(pat, email):
    print("Valid email id")
else:
    print("Invalid email id")