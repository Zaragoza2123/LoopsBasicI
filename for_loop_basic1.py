
def basic():
    for x in range(1,156):
        print(x)
basic()        


def mulsOf5():
    for y in range(5,1001):
        if y%5==0:
            print(y)
mulsOf5()            


def dojoway():
    for d in range(1, 101):
        if d%10==0:
            print("Coding Dojo")
        elif d%5==0:
            print("Coding")    
        else:
            print(d)  
dojoway()  


def whoa():
    sum = 0
    for i in range(0, 500000):
        if i%2==1:
            sum = i + sum
    print(sum)
whoa()


def downfour():
    for f in range(2018, 0, -4):
        print(f)
downfour()        


def flexcount(lowNum, highNum, mult):
    for x in range(lowNum,highNum+1):
        if x%mult==0:
            print(x)
flexcount(2,9,3)            
