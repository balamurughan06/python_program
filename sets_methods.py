'''
#add()
print("--- add() ---")
thisSet = {"apple", "mango", "banana"}
thisSet.add("orange")
print(thisSet)

#clear()
print("--- clear() ---")
thisSet = {"apple", "mango", "banana"}
thisSet.clear()
print(thisSet)

#copy()
print("--- copy() ---")
thisSet = {"apple", "mango", "banana"}
thisSet2 = thisSet.copy()
print('set1', thisSet) #original
print('set2', thisSet2) #copy of original

#difference
print("--- difference() ---")
thisSet = {"apple", "mango", "banana"}
thisSet2 = {"banana", "kiwi", "orange"}
print(thisSet.difference(thisSet2)) #elements in thisSet but not in thisSet2

#difference_update()
print("--- difference_update() ---")
thisSet = {"apple", "mango", "banana"}
thisSet2 = {"banana", "kiwi", "orange"}
print(thisSet) #original
print(thisSet2) #another set
thisSet.difference_update(thisSet2)
print(thisSet) #elements in thisSet but not in thisSet2


#discard()
print("--- discard() ---")
thisSet = {"apple", "mango", "banana"}
print(thisSet)
thisSet.discard("mango") #remove "mango"
print(thisSet)
thisSet.discard("kiwi") #remove "kiwi" (no error if not found)
print(thisSet)

#intersection
print("--- intersection() ---")
thisSet = {"apple", "mango", "banana"}
thisSet2 = {"banana", "kiwi", "orange"}
print(thisSet) #original set
print(thisSet2) #another set
print(thisSet.intersection(thisSet2)) #elements common to both sets

#intersection_update()
print("--- intersection_update() ---")
thisSet = {"apple", "mango", "banana"}
thisSet2 = {"banana", "kiwi", "orange"}
thisSet.intersection_update(thisSet2)
print(thisSet) #elements common to both sets and updated in thisSet

#isdisjoint()
print("--- isdisjoint() ---")
thisSet = {"apple", "mango", "banana"}
thisSet2 = {"banana", "kiwi", "orange"}
print(thisSet.isdisjoint(thisSet2)) #True if no elements in common
thisSet2 = {"kiwi", "orange"}
print(thisSet.isdisjoint(thisSet2)) #False if elements in common

#issubset()
print("--- issubset() ---")
thisSet = {"apple", "mango"}
thisSet2 = {"banana", "kiwi", "orange"}
print(thisSet.issubset(thisSet2)) #True if thisSet is a subset of thisSet2
thisSet2 = {"apple", "mango", "banana", "kiwi", "orange"}
print(thisSet.issubset(thisSet2)) #False if thisSet is not a subset of thisSet2

#issuperset()
print("--- issuperset() ---")
thisSet = {"apple", "mango", "banana"}
thisSet2 = {"banana"}
print(thisSet.issuperset(thisSet2)) #True if thisSet is a superset of thisSet2
thisSet2 = {"banana", "kiwi"}
print(thisSet.issuperset(thisSet2)) #False if thisSet is not a superset of thisSet2

#pop()
print("--- pop() ---")
thisSet = {"apple", "mango", "banana"}
print(thisSet)
thisSet.pop() #remove an arbitrary element
print(thisSet)

#remove()
print("--- remove() ---")
thisSet = {"apple", "mango", "banana"}
print(thisSet)
thisSet.remove("mango") #remove "mango"
print(thisSet)
thisSet.remove("kiwi") #remove "kiwi" (error if not found)
print(thisSet)

#symmetric_difference()
print("--- symmetric_difference() ---")
thisSet = {"apple", "mango", "banana"}
thisSet2 = {"banana", "kiwi", "orange"}
print(thisSet.symmetric_difference(thisSet2)) #elements in either set but not both

#symmetric_difference_update()
print("--- symmetric_difference_update() ---")
thisSet = {"apple", "mango", "banana"}
thisSet2 = {"banana", "kiwi", "orange"}
thisSet.symmetric_difference_update(thisSet2)
print(thisSet) #elements in either set but not both and updated in thisSet

#union()
print("--- union() ---")
thisSet = {"apple", "mango", "banana"}
thisSet2 = {"banana", "kiwi", "orange"}
print(thisSet.union(thisSet2)) #elements in either set

#update()
print("--- update() ---")
thisSet = {"apple", "mango", "banana"}
thisSet2 = {"banana", "kiwi", "orange"}
thisSet.update(thisSet2)
print(thisSet) #elements in either set and updated in thisSet
'''