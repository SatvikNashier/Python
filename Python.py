# a='nitin'
# print(a[::-1])
# a=str(input())
# b=str(input())
# print(a+b+a[::-1]+b[::-1])
import math

# str1 = "This is my first String"
# print(str1)
# print(str1[11])
# print(str1[-6])
#



# str = "How are you?"
# print("String is", str)
# print(str[4:7])
# print(str[2:5])
# print(str[-4:-1])
# print(str[-2:-5:-1])
# print(str[-4:])




# str = input("input: ")
# if len(str) > 2:
# 	print("output:", str[:2] + str[-2:])
# else:
# 	print("output:", str)




# str = input("str: ")
# print("output:", str[1:-1])




# str = input("str: ")
# if len(str) > 1:
# 	print("output:", str[-1] + str[1:-1] + str[0])
# else:
# 	if len(str) == 1:
# 		print(str)
# 	else:
# 		print ("null")





# a='Python is easy'
# print(a.swapcase())



# str1 = input("str1: ")
# str2 = input("str2: ")
# l1 = len(str1)
# l2 = len(str2)
# if l1 == l2:
# 	print("strings are same length")
# elif l1 < l2:
# 	print(str1 + str2 + str1)
# else:
# 	print(str2 + str1 + str2)




#
# str = input("str: ")
# fstr = ""
# sstr = ""
# if len(str) == 0:
# 	print("null")
# else:
# 	if len(str) == 1:
# 		print(str)
# for i in range(0,len(str)):
# 	if i % 2 == 0:
# 		fstr = fstr + str[i]
# 	else:
# 		sstr = sstr + str[i]
# print("first:", fstr)
# print("second:", sstr)
# print("original:",str)





# a = input("str: ")
# length = len(a)
# b = ""
# for i in range(0, length+1):
# 	b = b + a[:i]
# print("incremental order:", b)



# import string
# print("Character\t ASCII Code")
# for x in string.ascii_letters:
# 	print (x, "\t\t", ord(x))





# a = input("str: ")
# b = sorted(a)
# c = []
# for char in b:
# 	if char not in c:
# 		print("'{0}'\t{1}".format(char, b.count(char)))
# 		c.append(char)
# print(c)




#
# a = (input("str: "))
# b = []
# for y in a:
# 	if(y not in b):
# 		print(y,"\t", a.count(y))
# 		b.append(y)



#
# data = input("data: ")
# print("type of data:",type(data))
# list1=data.split()
# print("list1:",list1)
# print("type of list:",type(list1))
#




# data = input("Data:")
# list1=data.split(',')
# print("list:",list1)
# print("type of list:",type(list1))




# data=input("data: ")
# list1=data.split(",")
# print("list:",list1)
# index=int(input("Index: "))
# if index<len(list1) and index>=-(len(list1)):
#     print("element:",list1[index])




# data=input("data:")
# list1=data.split(",")
# print("Before updation:",list1)
# index=int(input("Index: "))
# print("element:",list1[index])
# list1[index]=str(input("Element"))
# print("after updation:",list1)




# def my_function(num,digit,str1,len):
#   print(num,digit,str1,len)
# num=str(input())
# digit=str(input())
# str1=str(input())
# len=str(input())
# my_function(num,digit,str1,len)





# string = 'pythonhxamples'
# position = 6
# new_character = 'e'
#
# string = string[:position] + new_character + string[position+1:]
# print(string)

#
# list_a = [22,56,77,99,45,36,87,93,5,78,2,66]
#
# even_list_a = list(filter(lambda x: (x % 2 == 0), list1))
#
# print("Even numbers in the list: ", even_nos)


# def printCubes(a, b):
#     # Traverse through all numbers in given range
#     # and one by one check if number is prime
#     for i in range(a, b + 1):
#
#         # Check if current number 'i'
#         # is perfect cube
#         j = 1
#         for j in range(j ** 3, i + 1):
#
#             if (j ** 3 == i):
#                 print(j ** 3, end=" ")
#                 break
# a = 1
# b = 100
# print("Perfect cubes in given range: ")
# printCubes(a, b)






# data=input("data: ")
# list1=data.split(",")
# list2=[]
# for i in range(len(list1)):
#     if list1[i] not in list2:
#         list2.append(list1[i])
# print(list1)
# print("after removing duplicates:",list2)




# data=input("data: ")
# list1=data.split(",")
# size=len(list1)
# for i in range(size):
#     list1[i]=int(list1[i])
# max_val=max(list1)
# min_val=min(list1)
# print("min:",min_val)
# print("max:",max_val)




# data=input('Data: ')
# list1=data.split(",")
# size= len(list1)
# for i in range(size):
#     list1[i]=int(list1[i])
# count=0
# element=int(input("element: "))
# for i in range(0,len(list1)):
#     if list1[i] == element:
#         count=count+1
# print(element,"occurs",count,'times')



