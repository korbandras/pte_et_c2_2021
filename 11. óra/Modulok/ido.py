import random
import time
def szamlalo(hossz: int,leptek: int)->None:
    for i in range(hossz//leptek):
        print(random.randint(0,1000))
        time.sleep(leptek)