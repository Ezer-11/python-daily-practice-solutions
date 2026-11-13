# !Day 2 — Lists, Strings & Logical Conditions

#? 1. Sum elements at even indexes — Calculate the sum of elements at indexes 0, 2, 4, 6...


# a = list(map(int,(input("enter your number\n").split())))

# sum = 0
# for i in range(len(a)):
#     if i %2==0:
#         sum += a[i]

# print(sum)



#? 2. Count numbers divisible by 3 but not 5 — Count qualifying integers in a list.

# a = list(map(int,input("enter your number\n").split()))
# print(a)
# count = 0
# for num in a :
#     if num%3==0 and num %5 != 0:
#         count+=1
# print(count)        


#? 3. Count vowels in a string — Count English vowels regardless of case.
# word = input("Enter a word: ")

# count = 0

# for character in word:
#     if character.lower() in "aeiou":
#         count += 1

# print(count)

# !One important programming concept to remember:
#* - for i in range(len(a)) → iterates over indexes.
#* - for character in word → iterates directly over characters.

# 4. Find the first non-repeating character — Find the first character appearing exactly once.


# a = str(input("enter yout name "))
# find = 0
# for char in a:
#     if a.count(char)==1:

#       print(char)
#       break

    # *loop iterates for every character in the string 
    #*and a.count(char) counts every character in the string 
    # *like a = "samuel"
    # *first it wil character is s it will check the occurance and then stop if it finds 


# ? 5. Check whether a list is sorted — Check non-decreasing order without sort() or sorted().

# a = list(map(int, input("Enter numbers: ").split()))

# is_sorted = True

# for i in range(len(a) - 1):

#     if a[i] > a[i+1]:
#         is_sorted = False
#         break

# if is_sorted:
#     print("Sorted")
# else:
#     print("Not sorted")

#* we assumed that the initial list is sorted and on the basis of that we checked and whenever 
#* this type of question comes like it is sorted or not like you have to give answer 
#* in yes or no go with this approach assume it and then break it
