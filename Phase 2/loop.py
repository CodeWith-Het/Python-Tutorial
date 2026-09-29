# Accept an integer and Print hello world n timesn
# ! answer
# num = int(input("Enter the number: "))

# for i in range(1,num+1,1):
#     print("Hello world")

# Print natural number up to n
# ! answer
# n = int(input("Enter the number: "))

# for i in range(1,n+1):
#     print(i)

# Reverse for loop. Print n to 1
# ! answer
# n = int(input("Enter the number: "))

# for i in range(n,0,-1):
#     print(i)

# Take a number as input and print its table
# ! answer
# num = int(input("Enter the number: "))

# for i in range(num,(num*10)+1,num):
#     print(i)

# Sum up to n terms
# ! answer
# num = int(input("Enter the number: "))
# sum=0

# for i in range(1,num+1,1):
#     sum+=i
# print(sum)

# Factorial of a number
# ! answer
# n = int(input("Enter the number: "))

# fact=1

# for i in range(n,0,-1):
#     fact*=i
# print(fact)

# Print the sum of all even & odd numbers in a range separately
# ! answer 
# n = int(input("Enter the number: "))
# evenSum=0
# oddSum=0

# for i in range(1,n+1,1):
#     if i%2==0:
#         evenSum+=i
#     else:
#         oddSum+=i

# print("Even Sum: ",evenSum)
# print("odd sumL ",oddSum)

# Print all the factors of a number
# ! answer
# n = int(input("Enter the number: "))

# for i in range(1,n+1,1):
#     if n%i==0:
#         print(i)

# Accept a number and check if it a perfect number or not.
# A number whose sum of factors is equal to the number itself
# Ex - 6 = 1, 2, 3 =
# ! answer

# n = int(input("Enter the number: "))
# sum=0

# for i in range(1,n):
#     if n%i==0:
#        sum+=i

# if sum==n:
#     print("Its perfect number")
# else:
#     print("Its not perfect number")