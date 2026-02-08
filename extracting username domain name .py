# valid e-mail address has the following format: username@domainname 
# write a code to  extract the username and domain name from an e-mail address
email = input("Enter your email address: ").strip().lower()
username, domain = email.split("@")
print("Username:", username)
print("Domain:", domain)