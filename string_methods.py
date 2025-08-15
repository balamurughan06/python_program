'''
#capitalize():
print("--- capitalize() ---")
x = "hello how are you?"
print(x)
print(x.capitalize())

#casefold():
print("--- casefold() ---")
x = "HELLO HOW ARE YOU?"
print(x)
print(x.casefold())

#center():
print("--- center() ---")
x = "balamurughan"
print(x)
print(x.center(10))
print("--- center() with filled character i (by default )---")
print(x.center(10,"i"))

#count()
print("--- count() ---")
x = "balamurughan"
print(x)
print(x.count("u"))
txt = "I love apples, apple are my favorite fruit"
print(txt)
print(txt.count("app",5,20))


#encode()
print("--- encode() ---")
x = "my nåme is bålamurughån"
print(x)
print(x.encode(encoding='ascii', errors='ignore'))
print(x.encode(encoding='ascii', errors='backslashreplace'))
print(x.encode(encoding='ascii', errors='namereplace'))
print(x.encode(encoding='ascii', errors='replace'))
print(x.encode(encoding='ascii', errors='xmlcharrefreplace'))
print(x.encode(encoding='ascii', errors='strict'))


#endswith()
print("--- endswith() ---")
text = "The world is so beautiful or wonderful."
print(text.endswith('beautiful.'))
print(text.endswith('beautiful'))
print(text.endswith(('beautiful.', 'wonderful.')))
print(text.endswith('beautiful', 5, 35))

#expandtabs()
print("--- expandtabs() ---")
text = "The\tworld\tis\tso\tbeautiful\tor\twonderful."
print(text)
print(text.expandtabs())
print(text.expandtabs(2))
print(text.expandtabs(4))
print(text.expandtabs(6))
print(text.expandtabs(8)) #default tab size
print(text.expandtabs(10))
print(text.expandtabs(12))

#find()
print("--- find() ---")
text = "The world is so beautiful or wonderful."
print(text.find('o'))
print(text.find('o',6,20))
print(text.find('k',6,20))

#format()
print("--- format() ---")
text = "The book is {price:.0f} rupees"
print(text.format(price=50))
text2 = "My name is {fname}, I'm {age}".format(fname = "Bala", age = 37)
text3 = "My name is {0}, I'm {1}".format("Murughan",37)
text4 = "My name is {}, I'm {}".format("Bala",36)
print(text2)
print(text3)
print(text4)

#index()
print('--- index() ---')
text = "The world is so beautiful or wonderful."
print(text.index('o'))
print(text.index('o',6,20))
print(text.index('k',6,20))


#isalnum()
print("--- isalnum() ---")
text = "Balamurughan123"
print(text.isalnum())
text2 = "Balamurughan 123"
print(text2.isalnum())

#isalpha()
print("--- isalpha() ---")
text = "Balamurughan"
print(text.isalpha())
text2 = "Balamurughan123abc"
print(text2.isalpha())

#isascii()
print("--- isascii() ---")
text = "Balamurughan"
print(text.isascii())


#isdecimal()
print("--- isdecimal() ---")
text = "12345"
print(text.isdecimal())
text2 = "12345abc"
print(text2.isdecimal())
text3 = "\u0030"
print(text3.isdecimal())
text4 = "\u004B"
print(text4.isdecimal())

#isdigit()
print("--- isdigit() ---")
number = "456"
print(number.isdigit())
text = "bac123"
print(text.isdigit())


#isidentifier()
print("--- isidentifier() ---")
text1 = "balamurughan123"
print(text1.isidentifier())
text2 = "bala_06"
print(text2.isidentifier())
text3 = "_bala_06"
print(text3.isidentifier())
text4 = "bala 06"
print(text4.isidentifier())


#islower()
print("--- islower() ---")
text1 = "Hello how are you?"
print(text1.islower())
text2 = "hello how are you?"
print(text2.islower())


#isnumeric()
print("--- isnumeric() ---")
text1 = "123"
print(text1.isnumeric())
text2 = "10^2"
print(text2.isnumeric())
text3 = "abc123"
print(text3.isnumeric())
text4 = "\u00b2" #unicode text for power of 2
print(text4.isnumeric())


#isprintable()
print("--- isprintable() ---")
text1 = "Hello! Are you fine?"
print(text1.isprintable())
text2 = "Hi, \n how are you?"
print(text2.isprintable())

#isspace()
print("--- isspace() ---")
text1 = "    "
print(text1.isspace())
print(text1.strip().isspace())
text2 = "Hi,how are you?"
print(text2.isspace())


#istitle()
print("--- istitle() ---")
text1 = "Hi, How Are You?"
print(text1.istitle())
text2 = "Hi, how Are You?"
print(text2.istitle())
text3 = "123 Hi,How Are You?&*&"
print(text3.istitle())


#isupper()
print("--- isupper() ---")
text1 = "Hi, How Are You?"
print(text1.isupper())
text2 = "HI, HOW ARE YOU?"
print(text2.isupper())
text3 = "123 HI, HOW ARE YOU?&*&"
print(text3.isupper())

#isjoin()
print("--- join() ---")
myTuple = ("Hi", "How", "Are", "You?")
print("*".join(myTuple))
myDict = {"name": "Bala", "age": 37}
print("%".join(myDict))


#ljust()
print("--- ljust() ---")
lText = "Hello"
result = lText.ljust(20)
print(result,"How are you?")

#lower()
print("--- lower() ---")
lower_text = "Hello, How Are YOU?"
lower_result = lower_text.lower()
print(lower_result)
'''

#lstrip()
print("--- lstrip() ---")
lstrip_text = "   Hello, How Are You?   "
lstrip_result = lstrip_text.lstrip()
print("Hi", lstrip_result, "I am fine.")


