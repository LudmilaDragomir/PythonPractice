# I have a lot of boxes of eggs in my fridge and I want to calculate how many omelettes I can make.
# Write a program to calculate this.
# Assume that a box of eggs contains six eggs and I need four eggs for each omelette, but I should be
# able to easily change these values if I want.
# The output should say something like "You can make 9 omelettes with 6 boxes of eggs".

nr_of_eggs_per_box = 6

boxes_of_eggs = input('Introduce the number of boxes of eggs you have ')

while len(boxes_of_eggs) == 0:
    boxes_of_eggs = input('Introduce the number of boxes of eggs you have ')

nt_of_egg_per_omlet = input('Introduce the number of eggs per omlet ')
while len(nt_of_egg_per_omlet) == 0:
    nt_of_egg_per_omlet = input('Introduce the number of eggs per omlet ')

number_of_omelettes_that_can_be_made = (nr_of_eggs_per_box * int(boxes_of_eggs)) / int(nt_of_egg_per_omlet)

message = "You can make '{}' omelettes with '{}' boxes of eggs".format(number_of_omelettes_that_can_be_made, boxes_of_eggs)
print(message)
