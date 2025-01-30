from object import *

class Childsum(Summations):
    def __init__(self, a, b):
        # Call the parent class's constructor
        Summations.__init__(self, a, b)

    def getchildsum(self):
        return self.fn + self.sn

# Create an object of Childsum
obj3 = Childsum(5, 6)
print(obj3.getchildsum())
if __name__ == '__main__':
    main()

#using for git
#second
<<<<<<< HEAD
#git branch
#Again
=======
#git branch 123
>>>>>>> e381db368d7b9c16331c0ede523ab7195214f189
