# !Day 3 — Indexing, Iteration & Problem Solving

#? 1. Find an element's index — Find the first occurrence without index() or in.

# target = int(input("Enter your number: "))
# numbers = [12, 34, 45, 54, 23]

# found = False

# for i in range(len(numbers)):
#     if target == numbers[i]:
#         print(i)
#         found = True
#         break

# if not found:
#     print(-1)

#* we assumed that we didn't found the number and used boolean  
#* without using boolean >
           
# target = int(input("Enter your number: "))
# numbers = [12, 34, 45, 54, 23]

# for i in range(len(numbers)):
#     if target == numbers[i]:
#         print(i)
#         break
# else:
#     print(-1)



#? 2. Count descending adjacent pairs — Count elements greater than their immediate next element.
# example: a = [9, 5, 7, 3, 2, 8]

# Compare neighboring elements, one pair at a time:
# Pair	Condition	Count
# 9, 5	9 > 5 True	1
# 5, 7	5 > 7 False	1
# 7, 3	7 > 3 True	2
# 3, 2	3 > 2 True	3
# 2, 8	2 > 8 False	3


# a = [72,23 ,34, 78 ,90 ,89]
# count = 0

# for i in range(len(a)-1):
#     if a[i]>a[i+1]:
#         count+=1

# print(count)

# *simple as me !!! ha ha ha...


#? 3. Move all zeros to the end — Preserve the relative order of non-zero elements.
# ! GOOD PROBLEM !!!
#  example : a = [0, 5, 0, 3, 8, 0, 2]

# !common mistake !!!

# a = [0, 5, 0, 3, 8, 0, 2]
# for i in range(len(a)):
#     if a[i] == 0:
#         a.remove(a[i])
#         a.append(0)  
# print(a)

#! When you remove an element:
#* - The list becomes shorter.
#* - The indexes of the remaining elements shift.
#* - But range(len(a)) was calculated using the original length.

# a = list(map(int,input("enter your number :\n").split()))
# result = []
# zero_count = 0
# for i in range(len(a)):
#     if a[i] != 0:
#         result.append(a[i])
#     else: 
#         zero_count +=1  
# for i in range(zero_count):
#     result.append(0)

# print(result)






#? 4. Check whether two strings are anagrams — Ignore spaces and case; don't use sorting.
# ! GOOD QUESTION !!!

#* Two strings are called anagrams when they contain exactly the same characters,
#* with exactly the same frequency(occurance of latter in word), but possibly in a different order.

# example : String 1	String 2	Result
#          listen	    silent	   True
#          hello	    world	  False

# ! important concept 


# str1 = input("Enter your word: ")
# str2 = input("Enter your second word: ")

# # * Convert both strings to lowercase and remove spaces
# # * replace(" ", "") replaces every space with an empty string
# str1 = str1.lower().replace(" ", "")
# str2 = str2.lower().replace(" ", "")

# # * Initially assume both strings are anagrams
# is_anagram = True

# # ! Anagrams must have equal lengths
# if len(str1) != len(str2):
#     is_anagram = False

# else:
#     # * Traverse every character in the first string
#     for char in str1:

#         # * count(char) returns the frequency of that character
#         # ! If even one frequency differs, they are not anagrams
#         if str1.count(char) != str2.count(char):
#             is_anagram = False

#             # ! Stop checking once a mismatch is found
#             break

# # * Print the final result after checking all characters
# if is_anagram:
#     print("The given words are anagrams")
# else:
#     print("The given words are not anagrams")


#* str1.count(char) here char is equal for both like 
#* str1 = "sb" and str2 = "bd" the condition checks like -> 
#* if str1.count(s) != str2.count(s)




#? 5. Find the longest increasing continuous sequence
#* — Find the length of the longest strictly increasing contiguous sequence.

a = list(map(int,input("enter your number :\n").split()))
count = 0
for i in range(len(a)-1):
    if a[i] < a[i+1]:
        count +=1
print(count)       