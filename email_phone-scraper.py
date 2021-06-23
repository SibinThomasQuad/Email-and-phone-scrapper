import re
from urllib.request import urlopen
print("##############################################")
print("#                                            #")
print("#          Email & Phone Scrapper            #")
print("#                                            #")
print("##############################################")
url = input("Enter a website to scan: (include http(s)://)\n>>")
website = urlopen(url).read().decode('utf8')
print("[1] Scrape Phone Number\n")
print("[2] Scrape Email\n")
option = input("Select The Option >>")
if option =='1':
    #line
    print("[+] Scrapped Phone Numbers\n")
    numbers = (re.findall(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})",website))
    print ('\n'.join(map(str, numbers)))
if option == '2':
    #data
    print("[+] Scapped Emails\n")
    emails = (re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",website))
    print ('\n'.join(map(str, emails)))
