annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input('Enter the portion of your salary to be saved: '))
total_cost = float(input("Enter the total cost of your dream home: "))
semi_annual_raise = float(input("Enter your semi annual raise: "))
portion_down_payment = 0.25
down_payment_amount = total_cost * portion_down_payment

# savings_mo = (annual_salary/12) * portion_saved

current_savings = 0.0

r = 0.04
T = 0
r_mo = 0.0
while current_savings < down_payment_amount:
    current_savings += ((annual_salary / 12) * portion_saved) + (current_savings * (r / 12))
    T = T + 1
    if (T % 6) == 0:
        annual_salary += (annual_salary * semi_annual_raise)
print(T)
