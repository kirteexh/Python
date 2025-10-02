name = "kirteesh"
j=len(name)-1
print(j)
while j>=0:
    print(name[j])
    j += -1

print(name) 
# all names will be printed

print(len(name))
# 8

print(name[1:4])
# irte

print(name[-4:-1])
# ees

print(name.count("e"))
# 2

print(name[0])
# k

#name[0]=i  is not allowed in strings

i=0
j=0
while i<len(name):
    if name[i]=="e":
        j += 1
    i += 1
print(j)
# 2