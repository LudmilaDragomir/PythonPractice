# Explain what this program does
# a number variable is declared as an int, and it will increase till 100 during the execution of the for loop
for number in range(100):
    output = 'o' * number  # the output variable is declared as a string, the o will be incremented by the number
    # as the print function is part of the for loop it will prin the 'o' character increasing each time by 1
    print(output)