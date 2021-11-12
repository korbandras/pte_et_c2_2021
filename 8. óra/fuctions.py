import datetime
import time as time_module
def parose(szam):
    if type(szam)==int:
        if szam%2==0:
            print('Páros szám')
        else:
            print('Páratlan szám')
def tipus(szam):
    if type(szam)==int or type(szam)==float:
        if szam<0:
            print('Negatív')
        elif szam>0:
            print('Pozitív')
        else:
            print('Nulla')

"""
szam=11
parose(szam)
parose(20)
parose("alma")
tipus(szam)
tipus(0)
tipus(-13)
tipus(43.3)
tipus("alma")
"""

def ido():
    print(datetime.datetime.now())
def wait(seconds):
    ido()
    print(f"Várunk {seconds} másodpercet")
    time_module.sleep(seconds)
    ido()

ido()
wait(1)
wait(10)