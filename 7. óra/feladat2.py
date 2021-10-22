import easygui

yr=easygui.enterbox('Please give a year: ',title='Data input')
try:
    yr=int(yr)
    if yr%4==0:
        if yr%100==0:
            if yr%400==0:
                easygui.msgbox('This year is a leap year', title='Resoult')
            else:
                easygui.msgbox('This is not a leap year',title='Resoult')
        else:
            easygui.msgbox('This is not a leap year',title='Resoult')
    else:
        easygui.msgbox('This is not a leap year',title='Resoult')
except ValueError:
    easygui.msgbox('Wrong input',title='Error')