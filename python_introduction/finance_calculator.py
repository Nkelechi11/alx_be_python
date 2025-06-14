# 6765




# finance_calculator.py

# Prompt the user for their monthly income
income = float(input("Enter your monthly income: "))

# Prompt the user for their total monthly expenses
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Calculate projected savings after one year with 5% interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Display the monthly savings
print(f"Your monthly savings are ${monthly_savings}.")

# Display the projected annual savings with interest
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")



