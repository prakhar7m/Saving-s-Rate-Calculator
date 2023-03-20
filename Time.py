# 1.Call the cost of your dream home total_cost .
# 2.Call the portion of the cost needed for a down payment portion_down_payment .
# For simplicity, assume that portion_down_payment = 0.25 (25%).
# 3.Call the amount that you have saved thus far current_savings .
# You start with a current savings of $0.
# 4.Assume that you invest your current savings wisely,
# with an annual return of r (in other words, at the end of each month,
# you receive an additional current_savings*r/12 funds to put into your savings – the 12 is because r is
# anannual rate). Assume that your investments earn a return of r = 0.04 (4%).
# 5.Assume your annual salary is annual_salary .
# 6.Assume you are going to dedicate a certain amount of your salary each month to saving for the down payment.
# Call that portion_saved .
# This variable should be in decimal form (i.e. 0.1 for 10%).
# 7.At the end of each month, your savings will be increased by the return on your investment,
# plus a percentage of your monthly salary (annual salary / 12).
# Write a program to calculate how many months it will take you to save up enough money for a down payment.
# You will want your main variables to be floats, so you should cast user inputs to floats.
# Your program should ask the user to enter the following variables:
# 1.The starting annual salary (annual_salary)
# 2.The portion of salary to be saved (portion_saved)
# 3.The cost of your dream home (total_cost)
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input('Enter the portion of your salary to be saved: '))
total_cost = float(input("Enter the total cost of your dream home: "))
salary_month = annual_salary/12

portion_down_payment = float(input("Enter the downpayment % of your dream home: "))
portion_down_payment = portion_down_payment/100 
down_payment_amount = total_cost*portion_down_payment

savings_mo = salary_month * portion_saved

current_savings = 0.0

r = 0.04
T = 0
r_mo = 0.0
while current_savings < down_payment_amount:
    current_savings = current_savings + savings_mo + (current_savings * (r / 12))
    T = T + 1
print (T)



