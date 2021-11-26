def upper_case(szoveg: str)->None:
    print(szoveg.upper())
    for char in szoveg:
        if char>='a' and char<='z':
            print(chr(ord(char)-ord('a')+ord('A')),end="")
        else:
            print(char, end="")