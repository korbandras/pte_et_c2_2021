def time():
    num = int(input('Insert a number (>0): '))
    if num < 0:
        print('Invalid')
    elif num == 0:
        print('now')
    else:
        yr = num // (60*60*24*365)
        num = num % (365*24*3600)
        day2 = num // (60*60*24)
        num = num % (24*3600)
        hr = (num // 3600)
        num %= 3600
        minute = num // 60
        num %= 60
        sec = num
        print('%d év, %d nap, %d óra, %d perc, %d másodperc' %(yr, day2, hr, minute, sec))
time()