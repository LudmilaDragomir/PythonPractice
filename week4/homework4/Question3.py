# Write a program that simulates a lottery.
# The program should have a list of seven numbers that represent a lottery ticket.
# It should then generate seven random numbers.
# After comparing the two sets of numbers, the program should output a prize based on the number of matches:
# ● £20 for three matching numbers
# ● £40 for four matching numbers
# ● £100 for five matching numbers
# ● £10000 for six matching numbers
# ● £1000000 for seven matching numbers
from random import randrange

prizes = {
    3: '£20',
    4: '£40',
    5: '£100',
    6: '£10000',
    7: '£1000000',
}

print('Welcome to our local lottery and GOOD LUCK!')
print('*******************************************')
lottery_ticket = 6552331
random_number = randrange(0, 9999999, 1)


def get_digit(number, n):
    return number // 10 ** n % 10


list_of_digits = []


def get_digit2(number):
    list_of_digits =[int(digit) for digit in str(number)]
    # list_of_digits =[ for digit in str(number)]
        # list_of_digits.append(digit)
    print(list_of_digits)
    return list_of_digits


get_digit2(3322145678)

matching_numbers = 0
for ind in range(7):
    if get_digit(random_number, ind) == get_digit(lottery_ticket, ind):
        matching_numbers = matching_numbers + 1

print('generated number: ' + str(random_number))
print('lottery ticket number: ' + str(lottery_ticket))
print(matching_numbers)
if matching_numbers > 2:
    print('You have {} matching numbers, your prize is {}'.format(matching_numbers, prizes[matching_numbers]))
else:
    print('Better luck next time!')
