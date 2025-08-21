'''
# If condition
a = 10
b = 20
if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else:
    print("a is equal to b")

# And condition
a = 20
b = 30
c = 10
if a < b and a < c:
    print("a is the smallest")
elif b < a and b < c:
    print("b is the smallest")
else:
    print("c is the smallest")

# OR condition
a = 30
b = 10
c = 20

if a < b or a < c:
    print("a is the smallest")
elif b < a or b < c:
    print("b is the smallest")
else:
    print("c is the smallest")

# NOT condition
a = 30
b = 10

if not (a < b):
    print("a is not less than b")

'''
# PASS statement
a = 33
b = 200

if b > a:
    pass
print("End")

