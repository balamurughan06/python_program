'''
#append()
print("--- append() ---")
myList = [1, 2, 3]
myList.append(4)
print(myList)

#clear()
print("--- clear() ---")
myList = [1, 2, 3]
myList.clear()
print(myList)

'''
#copy()
print("--- copy() ---")
myList = ['Bala','Murugan','Meghan']
myList2 = myList.copy()
print('list1',myList) #original
print('list2',myList2) #copy of original

#count()
print("--- count() ---")
myList = [1, 2, 3, 1, 2, 1]
print(myList.count(1)) #count of 1
print(myList.count(4)) #count of 4

#extend()
print("--- extend() ---")
myList = [1, 2, 3]
myList.extend([4, 5]) #extend the list by appending elements from the iterable
print(myList)

#index()
print("--- index() ---")
myList = [1, 2, 3]
print(myList.index(2)) #index of 2
# print(myList.index(4)) #index of 4 (will raise ValueError)

#insert()
print("--- insert() ---")
myList = [1, 2, 3] #insert 4 at index 1
myList.insert(1, 4)
print(myList)

#pop()
print("--- pop() ---")
myList = [1, 2, 3]
myList.pop() #remove last element
print(myList)
myList.pop(1) #remove element at index 1
print(myList)

#remove()
print("--- remove() ---")
myList = ["Bala", "Murugan", "Meghan"]
myList.remove("Murugan") #remove specified element
print(myList)

#reverse()
print("--- reverse() ---")
myList = [1, 2, 3]
print(myList) #original list
myList.reverse() #reverse the order of elements
print(myList)

#sort()
print("--- sort() ---")
myList = [3, 1, 2]
myList.sort() #sort the list in ascending order
print(myList)
myList.sort(reverse=True) #sort the list in descending order
print(myList)
