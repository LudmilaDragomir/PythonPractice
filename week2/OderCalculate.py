# each_person = 0.5
# number_of_people = input('How many people?')
#
# print('You need {} '+ str(int(each_person * float(number_of_people))))

whole_pizza = 1
#
def pizza_number():
    no_friends = int(input("How many people are there in total?"))
    no_pizza = no_friends / 2

    print("You need {} pizzas for {} of people".format(no_pizza, no_friends))