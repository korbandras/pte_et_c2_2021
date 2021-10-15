import random
import math
def kmhmps():
    speed1=int(input("Kérek egy sebességet  km/h-ban: "))
    valtoszam=3.6
    speed2=speed1//valtoszam
    print("A megadott sebesség (%d km/h) egyenlő %d m/s-vall" %(speed1,speed2))
def veletlenszamokbol():
    list=[]
    even=[]
    odd=[]
    for i in range(100):
        list.append(int(random.randint(0,500)))
        i+=1
    #print(list)
    for i in list:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print("odd:",odd)
    print("even:",even)
def haromszog():
    a=int(input("Kérem a háromszög A oldalát (cm): "))
    b=int(input("Kérem a háromszög A oldalát (cm): "))
    c=int(input("Kérem a háromszög A oldalát (cm): "))
    kerulet=a+b+c
    print("A háromszög kerülete: %d cm" %kerulet)
    d=(a+b+c)/2
    terulet=math.sqrt(d*(d-a)*(d-b)*(d-c))
    print("A háromszög  területe: %.2f cm^2" %terulet)
def listaminmax():
    list=[]
    for i in range(20):
        e=random.randint(1,100)
        list.append(e)
    mini=0
    maxi=0
    for i in list:
        if mini>=i:
            mini=i
        if maxi<i:
            maxi=i
    print(sorted(list))
    print(sorted(list)[0], maxi)
def milyenharomszog():
    a = int(input("Kérem a háromszög A oldalát (cm): "))
    b = int(input("Kérem a háromszög A oldalát (cm): "))
    c = int(input("Kérem a háromszög A oldalát (cm): "))
    if a+b>c and a+c>b and b+c>a:
        if  a**2+b**2==c**2 or b**2+c**2==a**2 or c**2+b**2==a**2:
            print("Derékszögű")
        if a==b and a==c:
            print("Egyenlőoldalú")
        else:
            print("Általnos")
    else:
        print("Nem lehet háromszöget szerkeszteni")
def jegy():
    pontszam=''
    while type(pontszam)==type(''):
        try:
            pontszam=float(input("pontszám: "))
        except ValueError:
            print("Moron")
    if pontszam<1 and pontszam>100:
        print('Liar')
    elif pontszam>=85:
        print('Stréber')
    elif pontszam>=70:
        print('Okos')
    elif pontszam>=55:
        print('Átlagos')
    elif pontszam>=40:
        print('Épphogy átment')
    elif pontszam>=1:
        print('Újabb félév?')
'''
kmhmps()
veletlenszamokbol()
haromszog()
listaminmax()
milyenharomszog()
'''
jegy()