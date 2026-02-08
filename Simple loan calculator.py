# Loan Payment Calculator
# Write a program that prompt the user to enter all loan information and calculates the monthly payment using the formula in pervious slide
loan_amount = float(input("Enter the loan amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
loan_term_years = int(input("Enter the loan term (in years): "))

# Convert annual interest rate to monthly and decimal
monthly_interest_rate = annual_interest_rate / 100 / 12
# Convert loan term to months
loan_term_months = loan_term_years * 12

# Calculate monthly payment using the formula
monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -loan_term_months)

# Display the monthly payment rounded to 2 decimal places
print(f"The monthly payment for the loan is: {round(monthly_payment, 2)}")