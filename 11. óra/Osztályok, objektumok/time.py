class Time:
    def __init__(self,hour: int,minute: int, second: int):
        self.hour=hour
        self.minute=minute
        self.second=second
    def print(self):
        print(number_w_lead_zero(self.hour),number_w_lead_zero(self.minute),number_w_lead_zero(self.second),sep=":")

def number_w_lead_zero(number: int)->str:
    result=str(number)
    if number<10:
        result='0'+result
    return result

ora=int(input("Hour: "))
perc=int(input("Minute: "))
mp=int(input("Second: "))
ido=Time(ora,perc,mp)
ido.print()