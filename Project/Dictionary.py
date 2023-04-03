class Dictionary(object):
    # note: you cannot (and don't have to) use self here
    # Name = None
    # ID = None

    def __init__(self, dictionary):
        self.__dict__.update(dictionary)

# q = { 'Field1' : 3000, 'Field2' : 6000, 'RandomField' : 5000 }
# instance = DictionaryFields(q)

# print(instance.Field1)      # => 3000
# print(instance.Field2)    # => 6000
# print(instance.RandomField) # => 5000