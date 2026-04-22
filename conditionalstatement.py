#Print each word on a new line using loops.
n=input("enter name to split:")
for i in n.split():
    print(i)

#Find the second largest number in a list without sorting.
numbers=[3,4,2,7,9,1]
largest=numbers[0]
second_largest=numbers[0]
for i in numbers:
    if i>largest:
        second_largest=largest
        largest=i
    elif i>second_largest and i!=largest:
        second_largest=i
print("Second largest number is:",second_largest)

#Check if two strings are anagrams   
str1 = input("enter first string: ")
str2 = input("enter second string: ")
if sorted(str1) == sorted(str2):
    print ("the string is anagram")
else:  
    print("the string is not anagram")

#Create a list from 1–20 and store only numbers divisible by both 2 and 3.
divisiblenumbers =[]
for i in range(1,21):
    if i%2==0 and i%3==0:
        divisiblenumbers.append(i)
        print(divisiblenumbers)

#Given {'a':10,'b':25,'c':15}, find the key with the maximum value.
dic={'a':10,'b':25,'c':15}
max_value=max(dic.values())
for key,value in dic.items():
    if value==max_value:
        print("Key with maximum value is:",key)
        break
#positive,negative or zero.poistive (is even or odd).
n=int(input("enter num :"))
if n>0:
    print("positive")
    if n%2==0:
        print("even")
    else:
        print("odd")
else:
    if n==0:
        print("zero")
    else:
        print("negative")          

#Given a list of numbers, remove all duplicate values without using set().   
numbers_list=[1,2,3,4,2,5,1]
unique=[]
for i in numbers_list:
    if i not in unique:
      unique.append(i) 
    print(unique)     