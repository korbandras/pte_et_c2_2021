import math
#másodfokú egyenlet
def f1():
    a=int(input("Kérem az 'a' együtthatót a másodfokú egyenlethez: "))
    b=int(input("Kérem a 'b' együtthatót a másodfokú egyenlethez: "))
    c=int(input("Kérem a 'c' együtthatót a másodfokú egyenlethez: "))
    d=b*b-4*a*c
    if b*b<4*a*c:
        print("Nincs valós megoldás")
    elif b*b==4*a*c:
        print("%.2f a megoldás az egyenletre" %((-b+math.sqrt(d))/(2*a)))
    else:
        print("%.2f az első megoldás az egyenletre" %((-b+math.sqrt(d))/(2*a)))
        print("%.2f a második megoldás az egyenletre" %((-b-math.sqrt(d))/(2*a)))
#kisbetunagybetu
def f2():
    string2=''
    string=input("Kérek egy sor szöveget:\n")
    for betu in string:
        if betu.isupper():
            string2+=betu.lower()
        if betu.islower():
            string2+=betu.upper()
        if betu==" ":
            string2+=betu
    print(string2)

#f1()
f2()
