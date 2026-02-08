# given athat the email address has the following format: first name . lastname @hccs.edu
# write a program to extract the first name and last name from the email address
email = input("Enter your email address: ").strip().lower()
first_name, last_name = email.split("@")[0].split(".")
print("First Name:", first_name)
print("Last Name:", last_name)