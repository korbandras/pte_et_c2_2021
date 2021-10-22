from easygui import *

msgbox('Hello there!', title="Hello there!", ok_button="General Kenobi")
flavor=buttonbox('What is ur fav icecream flavor?',title='icecream',choices=['im gay[1]','chokobiskit[2]'], default_choice='im gay[1]')
msgbox('U picked '+flavor)