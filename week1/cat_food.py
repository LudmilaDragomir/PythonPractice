from calendar import weekday
from datetime import datetime

animal = 'cat'
number_of_animals = 10
number_of_cans_per_day = 2

# todaysDate = datetime.date.today();

# print(str(number_of_animals) + " " + animal + " eats " + str(number_of_animals*number_of_cans_per_day) + " per day")
print("{} {} eats {} per day".format(str(number_of_animals), animal, str(number_of_animals*number_of_cans_per_day)))
# print(str(number_of_animals) + " " + animal+ " eats " + str(number_of_animals*number_of_cans_per_day * 7) + " per week")