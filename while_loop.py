'''
i = 1
while i <= 5:
    print(i)
    i += 1


#break
i = 1
while i <= 5:
    print(i)
    if i == 4:
        break
    i += 1

#continue
i = 1
while i <= 5:
    i += 1
    if i == 4:
        continue
    print(i)
'''
#else
i = 1
while i <= 5:
   print(i)
   i += 1
else:
   print("Loop completed")