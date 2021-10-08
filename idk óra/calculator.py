while True:
    print('1 - összeadás; 2 - kivonás; 3 - szorzás; 4 - osztás')
    choice=input('Kérlek válassz a fentiekből!: ')
    if choice in ('1','2','3','4'):
        num1 = float(input("Adj meg egy számot: "))
        num2 = float(input("Adj meg egy számot: "))
        if choice == '1':
            print('%d + %d = %d' %(num1, num2, num1+num2))
        if choice == '2':
            print('%d - %d = %d' %(num1, num2, num1-num2))
        if choice == '3':
            print('%d * %d = %d' %(num1, num2, num1*num2))
        if choice == '4':
            if num2 != 0:
                print('%d / %d = %d' %(num1, num2, num1/num2))
            else:
                print('0-val nem lehet osztani')
        next=input("Mégegyszer szeretnél számolni? (igen/nem)\n")
        if next == 'nem':
            break
    else:
        print('Nem jó az input')