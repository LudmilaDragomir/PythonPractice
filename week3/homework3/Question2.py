# I'm on holiday and want to hire a boat.
# The boat hire costs £20 + a refundable £5 deposit.
# I've written a program to check that I can afford the cost, but something doesn't seem right.
# Have a look at my program and work out what I've done wrong

my_money = input('How much money do you have? ')
refundable = 5
boat_cost = 20 + refundable
# print(type(boat_cost))
if int(my_money) > boat_cost:
    print('You can afford the boat hire')
else:
    print('You can\'t afford the board hire')
