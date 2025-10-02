n = int(input("Enter the number of elements ="))
num = []
for i in range(n):
    i = int(input("Enter element ="))
    num.append(i)
  
nums = set(num)

num2 =list(nums)
a = len(num)
b = len(num2)

while a>b:
    num2.append("_")
    b = len(num2)
print(num)
print(len(nums),num2)



