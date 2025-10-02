# kdr_set = set(input("Enter the numbers =").split())
# print(kdr_set)
 
eng_readers = int(input())
eng_roll = set(map(int , input().split()))

# set function is used to convert it to a set obviously
# map (function , iterable)
# .split() function splits the elements separately

fre_readers = int(input())
fre_roll = set(map(int , input().split()))

result = eng_roll - fre_roll

print(len(result))