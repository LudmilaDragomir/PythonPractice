import operator

listInt = [1, 2, 3]  # define a list
l_iter = iter(listInt)  # create list_iterator

while True:
    # item will be "end" if iteration is complete
    item = next(l_iter, "end")
    if item == "end":
        break
    print(item)

stats = {'a': 1000, 'b': 3000, 'c': 100, 'd': 3000}
print(max(stats.items(), key=operator.itemgetter(1))[0])
