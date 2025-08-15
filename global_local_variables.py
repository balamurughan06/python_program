x = "awesome"
print("Python is " + x)

def myfunc():
  global x  
  x = "fantastic"
  print("Python is " + x)

print("Python is " + x)
myfunc()
print("Python is " + x)

x = "nice"

print("Python is " + x)


"""
    awesome
    awesome
    super
    fantastic
    fantastic
    nice
"""
    
