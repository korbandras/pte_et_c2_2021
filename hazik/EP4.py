from math import factorial
#10x10 szorzótábla
def f1():
    for i in range(1,11):
        for j in range(1,11):
            print("%d*%d=%d" %(i,j,i*j))
#sorozat eleme
def f2():
    elso=int(input("Kérem a mértani sorozat első elemét: "))
    masodik=int(input("Kérem a mértani sorozat masodik elemét: "))
    n=int(input("Hányadik elemre vagy kíváncsi?: "))
    q=masodik/elso
    n_elem=elso*q**(n-1)
    print("A mértani sorozat %d. eleme: %d" %(n,n_elem))
#pascal-háromszög
#internetről néztem, nem jöttem rá magamtól
def f3():
    n=int(input("Hányadik sorra vagy kíváncsi a Pascal-háromszögből?\n"))
    for i in range(n):
        for j in range(n - i + 1):
            # for left spacing
            print(end=" ")

        for j in range(i + 1):
            # nCr = n!/((n-r)!*r!)
            print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")

        # for new line
        print()
def f4():
    string=input("Kérek egy sor szöveget:\n")
    if string==string[::-1]:
        print("ez a szöveg palindrom")
    else:
        print("ez a szöveg nem palindrom")
f1()
f2()
f3()
f4()