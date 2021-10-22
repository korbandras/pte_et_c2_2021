import random
import easygui

game=easygui.buttonbox('Wanna play a game?\nYou have 6 chances of guessing the random number between 0-100',title='Guess the number',choices=["Let's go!","Another time"],default_choice="Let's go!")
if game==easygui.buttonbox("Let's go"):
    random_number=random.randint(0,100)
    i=0
    while i<6:
        guess=int(easygui.enterbox('Make a guess:'))
        if guess>random_number:
            easygui.msgbox('Higher number')
            i=i+1
        elif guess<random_number:
            easygui.msgbox('Lower number')
            i=i+1
        else:
            easygui.msgbox('You guessed correctly')
            break
    else:
        easygui.msgbox('You lost')