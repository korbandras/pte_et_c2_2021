#nagybetőre írás
def f1():
    k="Programozni tanulok."
    print(k.upper())
#kedvezmeny
def f2():
    ar=int(input("Kérem a termék árát: "))
    kedvar10kalatt=ar*0.9
    kedvar10kfelett=ar*0.8
    if ar>10000:
        print("Erre a termékre 20 százalék kedvezmény jár, kedvezményes ár: %d" %(kedvar10kfelett))
    else:
        print("Erre a termékre 10 százalék kedvezmény jár, kedvezményes ár: %d" %(kedvar10kalatt))
#focicsapat
def f3():
    gender=input("Neme? (m - férfi, f - nő): ")
    if gender=="f":
        age=int(input("Kérem a korát: "))
        if age>=10 and age<=12:
            print("Játszhat a csapatban")
        else:
            print("Nem játszhat a csapatban")
    else:
        print("Csak lányok játszhatnak ebben a csapatban")
f1()
f2()
f3()