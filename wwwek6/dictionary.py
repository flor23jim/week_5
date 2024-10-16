#dictionary= a collection of (key: value) pairs ordered and changable. No duplications 
capitals ={"USA": "washignton dc", "india": "New Delhi", "China ": "Deijing" , " Russia": "Moscoa "}
#print(dir(capital))
#dir- gives you the 
#print(help(capital))
#help- gives you 
print(capitals.get("USA")) 
if capitals.get("japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")
capitals.update({"Germany": "berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop("China")
#pop will remove and item
#popitem revomes the last item of the dictionary
capitals.popitem()
capitals.clear()
#.clear clears the dictionary leaving it blank 
print( capitals)
keys=-capitals.keys()
for key in capitals.keys():
    print(keys)
#returns all the keys and not the values 
values= capitals.values()
print(values)
#returns all the values but not the keys 
values= capitals.values()
print(values)
for value in capitals.values:
    print(values)
    capitals.items()
for key,value in capitals.item():
    print(f"{key}:{value}") 
