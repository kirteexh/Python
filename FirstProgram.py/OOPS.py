class Kirteesh:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Name =",self.name)
        print("the percentile is=",sum/3)

k1 = Kirteesh("Kirteesh",[96,97,98])
k1.avg()
