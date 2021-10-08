def f1():
    for i in range(1,11):
        print(i, end=' ')
def f2():
    j=0
    for i in range(1,20,2):
        if i/2!=0:
            print(i, end=' ')
            j+=1
            if j==6:
                break
        else:
            i+=1
def f3():
    sorozat=[]
    a1=0
    a2=1
    print(a1,a2,end=' ')
    i=0
    while i<8:
        an=a1+a2
        a1=a2
        a2=an
        print(an,end=' ')
        i+=1

f1()
print('\n-----------------')
f2()
print('\n--------------------')
f3()