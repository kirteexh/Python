def consider(list, idx=0):
    if(idx > len(list)-1):
        return
    print(list[idx])
    consider(list , idx+1) 
    
consider([1,2,3,4,5])

