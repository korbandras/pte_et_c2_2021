#file beolvasás
list=[]
def f1():
    be=open("EP2_3.txt",'r')
    i=0
    for sor in be:
        sor=sor.strip().split()
        i+=1
        list.append(sor)
    print("Lista elemei: ",list)
    print("Sorok száma a fileban: %d" %i)
#10x10 szorzótábla fileba
def f2():
    ki=open("10x10szt.txt",'w')
    for i in range(1,11):
        for j in range(1,11):
            ki.write("%d*%d=%d\n" %(i,j,i*j))
    ki.close()
#szam -> bin, okt, hex
#internet segítségével
def f3():
    num=int(input("Kérek egy számot: "))
    print("%d bináris alakban: %08d" %(num,int(bin(num)[2:])))
    print("%d oktális alakban: %08d" %(num,int(oct(num)[2:])))
    print("%d hexadecimális alakban: %08d" %(num,int(hex(num)[2:])))
f1()
f2()
f3()