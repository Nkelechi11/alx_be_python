# Declaring variables and asking user for inputs
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

# Adding interest rate and making estimations for annual savings
# rate = 0.05
# time = 12
# projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

rate = 0.05
time = 12
projected_savings = monthly_savings * time + (monthly_savings * time * rate)

# Display results with formatted values
print(f"Your monthly savings are ${monthly_savings:.2f}")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}")
