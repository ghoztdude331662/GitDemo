class Summations:
    def __init__(self,a,b):
        self.fn=a
        self.sn = b

    def getSum(self):

        s=self.fn+self.sn
        return s
def main():
    obj=Summations(2,3)
    r=obj.getSum()
    print(r)

if __name__=="__main__":
    main()


