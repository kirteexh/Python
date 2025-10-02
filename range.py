for i in range(5):
    print(i)

    # a range is a function that starts with 0 , and increases by 1
    # it is used as = range(start,stop,incr)
    # start = 0 ; incr = 1
    
for j in range(5,10): #range(start,stop)
    print(j)

for k in range (10,100,10):   # range(start,stop,incr)
    print(k)


    # example
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)    
factorial(5)        