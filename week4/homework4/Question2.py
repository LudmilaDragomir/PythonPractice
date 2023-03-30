# I'm setting up my own market stall to sell chocolates.
# I need a basic till to check the prices of different chocolates that I sell.
# I've started the program and included the chocolates and their prices. Finish the program by asking
# the user to input an item and then output its price.

chocolates = {
    'white': 1.50,
    'milk': 1.20,
    'dark': 1.80,
    'vegan': 2.00,
    }

product = input('What chocolates would you like: white, milk, dark, vegan ?')

if chocolates.__contains__(product) :
    print('The chocolate {} cost £{} '.format(product, chocolates[product]))
else:
    print('Sorry, whe don\'t have this type of chocolates yet')

#  Things to consider:
# what if the chocolate the user mentioned is not sold in the shop.
# Will the user get any message about it?
# What if we expand the chocolate selection to hundreds of chocolate types?
# Is it efficient to iterate through a list of hundreds of dictionaries?
# What is the purpose of the list in this case?
