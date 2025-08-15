#Create a string made of the first, middle and last character
str = "james"
length = len(str)
res = str[0]
mid = int(length/2)
# res = res + str[mid]+str[-1]
res = res+str[mid]+str[-1]
# print(res)


# Write a program to create a new string made of the middle three characters of an input string. Output=DipSon
str1 = "JhonDipPeta"
str2 = "JaSonAy"
len1 = len(str1)
len2 = len(str2)
mid1 = int(len1/2)
mid2 = int(len2/2)
res1 = str1[mid1-1:mid1+2]
res2 = str2[mid2-1:mid2+2]
# print(res1+res2)


# Append new string in the middle of a given string. Output = AuKellylt
s1 = "Ault"
s2 = "Kelly"
len_str = int(len(s1)/2)
res3 = s1[:len_str]+s2+s1[len_str:] 
# print(res3)


#Create a new string made of the first, middle, and last characters of each input string. Output = AJrpan
s1 = "America"
s2 = "Japan"
len_str1 = int(len(s1)/2)
len_str2 = int(len(s2)/2)
res4 = s1[0]+s2[0]+s1[len_str1]+s2[len_str2]+s1[-1]+s2[-1]
print(res4)