my_dictionary={}
my_dictionary["kulcs"]="étrék"
my_dictionary["mouse"]="egér"
my_dictionary["cat"]="macska"
print(my_dictionary,len(my_dictionary))
print("A cat értéke:",my_dictionary["cat"])
print("A cat értéke:",my_dictionary.get("cat"))
#print("A dog értéke:",my_dictionary["dog"])
print("A dog értéke:",my_dictionary.get("dog"))
print("A dog értéke:",my_dictionary.get("dog","Nem ismerem ezt a szót."))
print(my_dictionary.keys(),type(my_dictionary.keys()))
print(my_dictionary.values(),type(my_dictionary.values()))