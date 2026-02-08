# the student e-mail address are created using the following rules:
#firstname. lastname @hccs.edu
#write a code  to genrate an e-mail address given a student first name and last name.
first_name = input("Enter your first name: ").strip().lower()
last_name = input("Enter your last name: ").strip().lower()
email = f"{first_name}.{last_name}@hccs.edu"
print("Your email address is:", email)
