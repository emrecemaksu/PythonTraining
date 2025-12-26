a = "This is a string"
b = 10 # integer
c = 4.87 # float
d = True # boolen
e = [1, 2, 4, 8] # list and mutable
e.append(5) # adding an item on the list
e.insert(2, 3) # inserting an item at index 2
ex = [1, 'apple']
e.extend(ex) # extending list by another list, you can add any iterable object (tuple, set, dict etc.)
print(e)
f = (1, 2, 5, 10) # tuple and immutable
fx = (1,) # single value tuple, comma is required
g = { 'name': 'Emre', 'age' : 25} # dict, key-value pairs, mutable, ordered, changable, unduplicated keys
h = {"apple", 2, 3, "apple"} # set -> unchangable, unordered, unindexed you can remove and add items
print(h) #duplicates are not allowed in sets
h.add("banana")
h.remove("apple")
print(h) #All apple items are removed