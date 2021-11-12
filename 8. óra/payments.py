brutto_netto=0.665
def bruttonetto():
    salary=int(input("How much you earn?\n"))
    if type(salary)==int or type(salary)==float:
        neto=salary*brutto_netto
        print(f"{neto} is how much you earn with taxas removed")
bruttonetto()

def netto(n):
    ertek = 0
    if type(n) == int or type(n) == float:
        ertek = n*brutto_netto
    return ertek
print(netto(200000))

def nettobrutto():
    salary = int(input("How much you earn?\n"))
    if type(salary) == int or type(salary) == float:
        brutto = salary / brutto_netto
        print(f"{brutto} is how much you earn with taxas removed")
nettobrutto()

def brutto(n):
    ertek = 0
    if type(n)== int or type(n)== float:
        ertek = n / brutto_netto
    return ertek
print(brutto(133000))