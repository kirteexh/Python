list = [45,98,8,1]
 # Lists are mutable
tuple = (45,98,8,1)
 # Tuples are immutable

print(tuple)

list.copy() #copies the list
list.append(10) # adds at the end 
list.sort()  # sorts in the ascending order
list.sort(reverse=True) # sorts in the descending order
list.reverse() # sorts in reverse
list.insert(1,99) # replaces the element
print(list)
print(list[0])
print(len(list))
list[0]=13
print(list)

 # all slicing properties are allowed
 # Lists are mutable
 # Tuples are immutable