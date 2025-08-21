#clear()
print("--- clear() ---")
thisDict = {"name": "John", "age": 30, "city": "New York"}
thisDict.clear()
print(thisDict)

#copy()
print("--- copy() ---")
thisDict = {"name": "John", "age": 30, "city": "New York"}
thisDict2 = thisDict.copy()
print('dict1', thisDict) #original
print('dict2', thisDict2) #copy of original

#fromkeys()
print("--- fromkeys() ---")
keys = ("name", "age", "city")
thisDict = dict.fromkeys(keys)
print(thisDict)

#get()
print("--- get() ---")
thisDict = {"name": "John", "age": 30, "city": "New York"}
print(thisDict.get("name")) #access value by key
print(thisDict.get("country", "Unknown")) #default value if key not found

#items()
print("--- items() ---")
thisDict = {"name": "John", "age": 30, "city": "New York"}
print(thisDict.items()) #list of key-value pairs

#keys()
print("--- keys() ---")
thisDict = {"name": "John", "age": 30, "city": "New York"}
print(thisDict.keys()) #list of keys

#pop()
print("--- pop() ---")
thisDict = {"name": "John", "age": 30, "city": "New York"}
print(thisDict)
thisDict.pop("age") #remove key "age"
print(thisDict)

#popitem()
print("--- popitem() ---")
thisDict = {"name": "John", "age": 30, "city": "New York"}
print(thisDict)
thisDict.popitem() #remove last inserted key-value pair
print(thisDict)

#setdefault()
print("--- setdefault() ---")
thisDict = {"name": "John", "age": 30, "city": "New York"}
print(thisDict.setdefault("age", 31)) #existing key, no change
print(thisDict.setdefault("country", "USA")) #new key, set default value
print(thisDict)

#update()
print("--- update() ---")
thisDict = {"name": "John", "age": 30, "city": "New York"}
thisDict2 = {"age": 31, "country": "USA"}
thisDict.update(thisDict2)
print(thisDict) #elements in either dict and updated in thisDict

#values()
print("--- values() ---")
thisDict = {"name": "John", "age": 30, "city": "New York"}
print(thisDict.values()) #list of values