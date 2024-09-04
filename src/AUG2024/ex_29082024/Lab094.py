# List
# List - Collection of Items( Duplicate is allowed)
"""append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list"""
my_list = [1, 2, 3]  # Same type of data (# int)

mylist = [1, 2, 3]
print(mylist)
print(len(mylist))
print(mylist[0], my_list[1])

my_list[0] = "Pramod"
my_list[1] = "Dutta"
my_list[2] = "Dutta2"

print("element at the index 0 - ", my_list[0])
print("element at the index 0 - ", my_list[1])
print("element at the index 0 - ", my_list[2])
print(mylist)
for ele in my_list:
    print(ele)

for i in range(2, 10, 2):  # [1,2,3,4,5,6,7,8,9]
    print(i)
print("-------------")

# Append => add item to end of the list
my_list.append("ram")
print(my_list)
mylist.append(4)
mylist.append(5)
print(mylist)
# extend () add multiple item The extend() method adds the specified list elements (or any iterable) to the end of
# the current list.
my_list.extend([6, 7, 8])
print(my_list)
mylist.extend([6, 7, 8])
print(mylist)

# insert => insert any item  any place
mylist.insert(3, "ravi")
print(mylist)
f = ["amm", "manage", "apply"]
print(f)
mylist.remove(2)
print(mylist)
mylist.copy()
print(mylist)
mylist.clear()
print(mylist)
num = [6, 8, 9, 5, 4]
num.sort()
print(num)
num.reverse()
print(num)
