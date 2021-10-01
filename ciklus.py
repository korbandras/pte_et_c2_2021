is_num=False
while not is_num:
    try:
        num=int(input('Number: '))
        is_num=True
        if num%2==0:
            print('even')
        else:
            print('odd')
    except ValueError:
        print('not int')