from icecream import ic
class AOperations:
    def sum(self,x,y):
        return x+y


obj=AOperations()
ic(obj)
def multiply(self,x,y):
    return x*y
AOperations.sum=multiply
#replacing sum() function with multiply() function
ic(obj.sum(3,4))


