# Create a program that tells you whether you need an umbrella when you leave the house.
# The program should:
# 1. Ask you if it is raining using input()
# 2. If the input is 'y', it should output 'Take an umbrella'
# 3. If the input is 'n', it should output 'You don't need an umbrella'
print('Welcome to the weather prediction!')
is_raining = input('It is raining? ')
if is_raining == 'y':
    print('Take an umbrella!')
else:  # elif is_raining == 'n':
    print('You don\'t need an umbrella')
