# use these for study https://regex101.com/  https://regexone.com/
import re

email_pattern = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
check_email = email_pattern.fullmatch('sajib@sajib.com')

#Password check minimum 8 words also ends with number
password_patter = re.compile(r"([A-Za-z0-9$%#@]{7,}[0-9])")
check_password = password_patter.fullmatch('jibrish#%@8')

if check_email and check_password:
    print("Both email and password are correct.")
else:
    print("Try again.")
