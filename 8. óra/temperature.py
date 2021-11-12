temperatures=[]
def temperature():
    temp=0
    is_real_temp=True
    while is_real_temp:
        temp=input("Temperature: ")
        try:
            temp=float(temp)
            if temp<=40 and temp>=-40:
                temperatures.append(temp)
            else:
                is_real_temp=False
        except ValueError:
            is_real_temp=False
    #print(temperatures)
def examine(raw_number):
    result=False
    if type(raw_number)==str:
        result=True
        for i in range(len(raw_number)):
            if not str(raw_number[i]).isnumeric():
                if not (i==0 and (raw_number[i]=='+' or raw_number[i]=='-')):
                    result=False
    return result
def avg():
    summary=0
    for i in range(len(temperatures)):
        summary=summary+temperatures[i]
    global average
    average=summary/len(temperatures)
    print("The average temperature is %d" %average)
def lower_or_higher():
    lower=set()
    higher=set()
    for i in range(len(temperatures)):
        if temperatures[i]>average:
            higher.add(temperatures[i])
        else:
            lower.add(temperatures[i])
    print(f"{lower} are lower than the average")
    print(f"{higher} are higher than the average")
def highest():
    highest=temperatures[0]
    for i in range(len(temperatures)):
        if temperatures[i]>highest:
            highest=temperatures[i]
    print("%d is the highest temperature" %highest)
def first_higher_than_avg():
    firsthigher=0
    for i in range(len(temperatures)):
        if temperatures[i]>average:
            firsthigher=temperatures[i]
            break
    print("%d was the first higher than average temperature" %firsthigher)
temperature()
avg()
lower_or_higher()
highest()
first_higher_than_avg()