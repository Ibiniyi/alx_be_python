income = float(input( " Enter your monthly income " ))
expenses = float(input( " Enter your monthly expenses " ))
monthly_saving = income - expenses
annual_interest = 0.05
projected_saving = monthly_saving * 12 + (monthly_saving * 12 * annual_interest)

print(f" Your monthly saving are: {monthly_saving} ")
print(f"Projected savings after one year, with interest, is: {projected_saving}")
