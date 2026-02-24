annual_salary = float(input("Enter your starting salary: $"))
cost_of_house = 1000000
downpayment = 0.25 * cost_of_house
max_savings = 0
current_savings = 0
epsilon = 100
number_of_guesses = 0
high = 10000
low =0
guess = (high + low) // 2
for m in range(1, 37):
    monthly_salary = annual_salary / 12
    max_savings += max_savings * 0.04 / 12
    max_savings += monthly_salary
    if m % 6 == 0:
        monthly_salary += monthly_salary * 0.07
if max_savings < (downpayment - epsilon):
    print("It is not possible to pay the down payment in three years.")
else:
    while abs(current_savings - downpayment) > epsilon:
        guess = (high + low) // 2
        number_of_guesses += 1
        current_savings = 0
        monthly_salary = annual_salary / 12
        for months in range(1,37):
            current_savings += current_savings * 0.04 / 12
            current_savings += float(guess/10000) * monthly_salary    
            if months % 6 == 0:
                monthly_salary += monthly_salary * 0.07
        if current_savings < downpayment:
            low = guess
        else:
            high = guess
        if low >= high:
            break        
    if low >= 9999:
        print("It is not possible to pay the down payment in three years.")
    else:
        print(f"Best savings rate: {float(guess/10000):.4f}")
        print(f"Steps in bisection search: {number_of_guesses}")