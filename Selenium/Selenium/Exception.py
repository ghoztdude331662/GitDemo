x=5
#assert(x==5)    Assertion

#if(x!=5):
#    raise Exception("X is 5")

try:
    with open("test.txt","r") as file:
        file.read()
except:
    print("file wont read")