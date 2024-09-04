"""Join Sets
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
t = ("TheTestingAcademy", "for", "TheTestingAcademy")"""
print(t)
print(set(t))

set1 = {1, 2, 3}
set2 = {4, 5, 6}
my_set = set1.union(set2)
print(my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
my_set = set1.intersection(set2)
print(my_set)

# my_set = set1.difference(set2)
my_set = set2.difference(set1)
print(my_set)


set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 8}
subset = set2.issubset(set1)
print(subset)
