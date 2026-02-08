# get the index of the @ character

emailaddress = input("Enter your email address: ").strip().lower()
at_index = emailaddress.find("@")
username = emailaddress[:at_index]
domainname = emailaddress[at_index+1:]
print("Username:", username)
print("Domain name:", domainname)