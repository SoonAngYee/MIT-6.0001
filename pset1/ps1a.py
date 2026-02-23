annual_salary = float(input("Enter your annual salary: $"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25 * total_cost
current_savings = 0
months = 0
while current_savings < portion_down_payment:
    current_savings += current_savings * 0.04 / 12
    current_savings += portion_saved * annual_salary / 12
    
    months += 1

else:
    print("Number of months: ", (months))
