# You have a budget of £10 and want to write a program to decide which burger  restaurant to go to.
# 1. Input the price of a burger using input()
# 2. Check whether the price is less than or equal (<=) 10.00
# 3. Print the result in the format below
# Burger is within budget: True

budget = 10.00
burger_price = input('What is the price of a burger ')
is_less = float(burger_price) <= budget

vegetarian_option = input('Is there a vegetarian option? (y/n) ')
meets_criteria = str(vegetarian_option) == 'y'

is_good = meets_criteria and is_less
print('Burger is within budget: {} '.format(is_good))


