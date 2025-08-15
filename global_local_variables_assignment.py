x = 20
print("global variable x")
print('x:',x)

def addition():
    global x
    x = 15
    y = 15
    print("inside func global variable x")
    print('x:',x)
    print("inside func local variable y")
    print('y:',y)
    print('x+y:',x+y)

print("---- Addition --------")
addition()
print("outside func global variable x")
print('x:',x)

x = 25
def subtraction():
    global x
    x = 30
    y = 10
    print("inside func global variable x")
    print('x:',x)
    print("inside func local variable y")
    print('y:',y)
    print('x-y:',x-y)

print("-------- Subtraction --------")
subtraction()
print("outside func global variable x")
print('x:',x)

def multiplication():
    global x
    x = 10
    y = 5
    print("inside func global variable x")
    print('x:',x)
    print("inside func local variable y")
    print('y:',y)
    print('x*y:',x*y)

print("-------- Multiplication --------")
multiplication()
print("outside func global variable x")
print('x:',x)

def division():
    global x
    x = 60
    y = 5
    print("inside func global variable x")
    print('x:',x)
    print("inside func local variable y")
    print('y:',y)
    print('x/y:',x/y)

print("-------- Division --------")
division()
print("outside func global variable x")
print('x:',x)
