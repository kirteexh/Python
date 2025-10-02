class Vesit:
    def __init__(self , fullname):
        self.name = fullname
        print("Adding new name...")

    def hello(self):       # Don't forget to write 'self' inside the function    
        print(self.name,"Hi 2nd year")    
    
    def age(self):
        print("They are 19 y/o" , self.name)

k1 = Vesit("Kirteesh")
# print(k1.name)

# k2 = Vesit("Nihar")
# print(k2.name)

k1.age()  # to call the new function

# x1 = Vesit()
# print(x1.name)
# print(Vesit().name)    # Both of them are same ....