def rendezes_buborek(lista: list[int])->list[int]:
    rendezett_lista=lista.copy()
    for i in range(len(rendezett_lista)):
        for j in range(i+1,len(rendezett_lista)):
            if rendezett_lista[i]>rendezett_lista[j]:
                seged=rendezett_lista[i]
                rendezett_lista[i]=rendezett_lista[j]
                rendezett_lista[j]=seged
        #print(i,j,rendezett_lista)
    return rendezett_lista
def min(lista: list[int])->list[int]:
    mini=lista[0]
    for szam in lista:
        if szam<mini:
            mini=szam
    return mini
def max(lista: list[int]) -> list[int]:
    maxi=lista[0]
    for szam in lista:
        if szam>maxi:
            maxi=szam
    return maxi
def sum(lista: list[int]) -> list[int]:
    global szumma
    szumma=0
    for szam in lista:
        szumma+=szam
    return szumma
def avg(lista: list[int]) -> list[int]:
    atlag=0
    db=0
    for szam in lista:
        db+=1
    atlag=szumma/db
    return atlag

lista=[24,45,231,3,134,0,54]

print(rendezes_buborek(lista))
print(min(lista))
print(max(lista))
print(sum(lista))
print(avg(lista))