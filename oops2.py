class Kirteesh:
    def __init__(self ,name , marks):
        self.name = name 
        self.marks = marks
    
    @staticmethod   # it's use is to use a function without 'self'...
    def my_world():
        print("My world is my family !")

    def avg(self):
        sum = 0
        for num in self.marks:
            sum += num
        print("Hi",self.name,"Your average is",sum/3) 

k1 = Kirteesh("kirteesh",[90,91,92])
k1.avg()               
k1.my_world()