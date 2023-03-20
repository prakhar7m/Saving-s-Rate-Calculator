current_salary = float(input("Enter your annual salary: "))
total_cost = 1000000
semi_annual_raise = 0.07
down_payment = 0.25 * total_cost
r = 0.04
max_portion_saved_as_integer = 10000
min_portion_saved_as_integer = 0
best_portion_saved_as_integer = max_portion_saved_as_integer
possible_to_pay_in_three_years = True
num_steps = 0


def savings(current_salary, best_portion_saved):
    current_savings = 0.0
    T = 36
    while T >= 0:
        T = T - 1
        current_savings += ((current_salary / 12) * best_portion_saved) + (current_savings * (r / 12))
        if (T % 6) == 0:
            current_salary += (current_salary * semi_annual_raise)
    return current_savings


while True:
    num_steps += 1
    best_portion_saved = best_portion_saved_as_integer / 10000

    if abs(savings(current_salary,best_portion_saved) - down_payment) <= 100:
        break

    if savings(current_salary,best_portion_saved) > down_payment:
        max_portion_saved_as_integer = best_portion_saved_as_integer
    else:
        min_portion_saved_as_integer = best_portion_saved_as_integer

    if min_portion_saved_as_integer >= max_portion_saved_as_integer:
        possible_to_pay_in_three_years = False
        break

    best_portion_saved_as_integer = (max_portion_saved_as_integer + min_portion_saved_as_integer) // 2


if possible_to_pay_in_three_years:
    print('Best savings rate: {}'.format(best_portion_saved))
    print('Steps in bisection search: {}'.format(num_steps))
else:
    print('It is not possible to pay the down payment in three years.')

