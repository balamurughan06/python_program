'''
#looping through a list
veggies = ["carrot", "broccoli", "spinach"]
for veg in veggies:
    print(veg)

#looping through a string
for str in "balamurughan":
    print(str)

#break
veggies = ["carrot", "broccoli", "spinach"]
for veg in veggies:
    print(veg)
    if(veg == "broccoli"):
        break

veggies = ["carrot", "broccoli", "spinach"]
for veg in veggies:
    if veg == "broccoli":
        break
    print(veg)

#continue
veggies = ["carrot", "broccoli", "spinach"]
for veg in veggies:
    if veg == "broccoli":
        continue
    print(veg)

#range
for i in range(5):
    print(i)

#range with starting value (default is 0)
for i in range(2, 5):
    print(i)

#range with increment steps
for i in range(2, 10, 2):
    print(i)

#else
for i in range(5):
    print(i)
else:
    print("Loop completed")

#break
for i in range(5):
    if i == 2:
        break
    print(i)
else:
        print("Loop completed")

# Nested loop
veggies = ["carrot", "broccoli", "spinach"]
fruits = ["apple", "banana", "cherry"]
for veg in veggies:
    for fruit in fruits:
        print(veg, fruit)

# Pass statement
for i in range(5):
    pass
'''