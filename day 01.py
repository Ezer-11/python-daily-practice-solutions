# !Day 1 — Basic Logic & Number Manipulation

#? 1. Largest of three numbers — Take three numbers and find the largest using conditional statements.

# a = int(input("enter your first number\n"))
# b = int(input("enter your second number\n"))
# c = int(input("enter your third number\n"))

# if(a ==b and b == c):
#     print("all are equal")
# elif(a>=b and a >=c):
#     print(f"{a} is the largest")

# elif(b>=c and b> a):
#     print(f"{b} is the largest ")

# else:
#     print(f"{c} is the largest")

#*learning python reads the code from top to bottom if the one condition satisfies it will stop.


#? 2. Positive, negative and zero counter — Take 10 integers and count positive, negative and zero values.

# a = list(map(int,input("enter your numbers\n").split()))
# *list will store all the inputs in -> [] 
# *map will convert all the input into integer 
# *split will seaprate everything

# positive = 0
# negative = 0
# zero = 0

# for i in range(len(a)):
  
#   if(a[i]>0):
#     print("positve")
#     positive +=1
#   elif(a[i]<0):
#     print("negative")
#     negative+=1
#   else:
#     print("zero") 
#     zero+=1   

# print(positive)
# print(negative)
# print(zero)

# *in list index starts from zero
# *a[i] to acess the element from the list

# !alternate solution
# !we can acces the element inside list without index 

#  *for num in a:
#  *    if num > 0:
#  *       positive += 1
#  *    elif num < 0:
#  *        negative += 1
#  *   else:
#  *     zero += 1

#? 3. Reverse a number — Reverse an integer mathematically without converting it into a string.

# a = int (input("enter your number\n"))
# digit = 0
# reverse = 0

# while (a>0):
#     digit = a%10
#     reverse = reverse  * 10 + digit
#     a = a//10

# print(reverse)

# *we used while loop because we don't know when to stop.
#* digit = a%10 gives the last digit (remainder).
#* reverse store the last digit. 
#* a = a//10 removes the last digit.
#! note: trace the code manually in the notebook






#? 4. Second-largest element — Find the second-largest distinct element in a list without using sort().


# a = set(map(int, input("Enter your numbers: ").split()))

# largest = float("-inf")
# second_largest = float("-inf")

# for i in range(len(a)):

#     if list(a)[i] > largest:
#         second_largest = largest
#         largest = list(a)[i]

#     elif list(a)[i] > second_largest:
#         second_largest = list(a)[i]

# if second_largest == float("-inf"):
#     print("No second-largest distinct number")
# else:
#     print("Second largest:", second_largest)
#     print("Largest:", largest)

# # ! Mistake 1:
# *largest = num
# *second_largest = largest

# *Why wrong?
#* Both variables now contain the same number.
#* Save the old largest FIRST.

# ! Mistake 2:
#* else:
# *    second_largest = num

#* Why wrong?
# *This can overwrite a valid second-largest number.
#* Use elif num > second_largest instead.

# ! Mistake 3:
#* Assuming set elements are sorted.
#* Sets are unordered collections, not sorted lists.

# ? set()
#* Removes duplicate elements from a collection.*
# *Example: {10, 20, 20, 30} becomes {10, 20, 30}
#* Sets do not support indexing.

# ? list()
#* Converts a set into a list.
#* Example: b = list(a)
# *Lists support indexing, such as b[0], b[1].

# ! Important:
#* A set does not guarantee sorted order.
#* Never assume its elements are arranged from smallest to largest.

# ? float("-inf")
#* Represents negative infinity.
#* Useful as an initial value when searching for the largest numbers.
#* Any ordinary integer is greater than negative infinity.


#? 5. Perfect number — Check whether a number is a perfect number.

#* A perfect number is a number whose sum of all its positive divisors, 
#* excluding itself, equals the number.
#* example : 6  = 1 ,2,3
# *         => 1+2+3 = 6    

n = int(input("enter your number\n"))
sum= 0
for i in range(1, n):
    if n == 0 :  
      print("not defined")

    elif n%i==0:
       sum +=i

if n ==sum:
    print("the number is perfect ")
else:
   print("not a perfect number")