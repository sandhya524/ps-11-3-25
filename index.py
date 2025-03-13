# Print all numbers from 1 to 100 using a for loop.
for i in range(1,101):
    print(i)

# # Write a program to print the sum of the first n natural numbers. (n*n+1/ 2)
n = int(input("enter a nutural num: "))
sum = 0
for j in range(1,n+1):
    sum += j 
print(sum)   

# Print all even numbers between 1 and 50 using a while loop
numbers = 1
while numbers < 52:
    if numbers % 2 == 0:
        print(numbers,"is even")
    numbers += 1         

# Write a program to display the multiplication table of a given number. First 20 
user_mul = int(input("enter a multiplication num: "))
mul = 1
for m in range(1,11):
    mul = user_mul * m
    print(f"{user_mul}*{m}={mul}") 

# Write a program to calculate the factorial of a number using a while loop.
facto = int(input('enter a number to factorial: '))
mul1 = 1
while facto != 0:
      mul1 = mul1 * (facto)
      facto -= 1
print(mul1)      

# Print all numbers from 1 to 100 that are divisible by 3 and 5 using a for loop.

for l in range(1,101):
    if (l % 5 == 0) and (l % 3 == 0):
        print(l,"is divisible by 5 and 3")
    
#task   
num1 = 10 #integer
print(num1)

num2 = 20.5 #float value
print(num2)

num3 = 3+5j # complex 
print(num3)

bool1 = True#
print(type(bool1))

list1 =[2,3,5,7]
print(type(list1))
print(list[0])

tup1 =(2,3,4,(3,6))
print(type(tup1))

print(range(1,11))
print(list(range(1,11)))

str1 ="sandhya"
print(str1)

set1 ={2,3,4,5,6,7,8}
print(set1)

dict1 ={1:'sandhya',2:'10k coders',3:'python'}
print(dict1[3])

# operators
num1 = 5
num2 = 10
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 % num2)
print(num1 ** num2)
print(num1 / num2)
# relational operators
print(3>5)#false
print(3==5)#false
print(3<4)
print(2<=6)
print(7>=4)
print(2!=6) #true
# logical operators
print(2 and 3)#3
print(0 and 4)#0
print(True or False)
print(-1 or -7)
#bitwise operator
print(2 & 3)#and operation
print(2 | 3)#or
print(2 ^ 3)#xor
print(2, ~ 3)
print(89 << 2)#left shift
print(76 >> 3)#right shift
#conditional statements
age= 20
if age > 18:
    print('you can vote')
else:
    print('you are minor,you can not vote')   
# for loop
for cls in range(1,11):#to print classes 1 to 10
    for roll in range(1,16):#to print roll no 1 to 15
        print(cls,roll)

        
#while loop to adding the numbers and come from the loop when it is 0
total = 0
number1 = int(input("enter a number to add and ('0 to quit')"))
while number1 != 0:
    total =total + number1
    number1 = int(input("enter a number and (0 to quit)"))
print(total)


    


#break
for i in range(0,11):
    print(i)
    if i == 5:
        break

for j in range(0,11):
    print(j)
    if j == 5:
        break#only loop terminated
    print(j)
#continue
for k in range(1,11):
    print(k)
    if k > 4:
        continue#only after contineous iterations are skipped
    print(k)
#function
def example(x,y):
    res = x+y
    print(res)    
example(2,3)    
#return statement
def find_gretest(a,b):
    if a > b:
        return a
    else:
        return b    

print(find_gretest(49,45))


#PERFECT NUMBER
# A perfect number is a positive integer 
# that is equal to the sum of its divisors, excluding the number itself. 
# For example, 6 is a perfect number because 1 + 2 + 3 = 6. 
num = int(input("enter a number to find the perfect num: "))
sum1 = 0
if num > 0:
    for i in range(1,num):
        if num % i == 0:
            sum1 += i
    if sum1 == num:
        print(num, "is a perfect number ")
    else:
        print(num, "is not a perfect number")
else:
    print("enter a positive number")

# HCF /GCD:
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

num1 = int(input("enter1:"))
num2 = int(input("enter2:"))
print(gcd(num1,num2))

# 2nd method for HCF:
a = int(input("enter:"))
b = int(input("enter:"))
hcf = 1
for i in range(1,min(a,b)+1):
    if a % i == 0 and b % i == 0:
        hcf = i
print(hcf)       

# LCM:
a = int(input("enter1:"))
b = int(input("enter1:"))
max_num = max(a,b)
while True:
    if max_num%a == 0 and max_num%b == 0:
        print(max_num)
        break
    max_num += 1

#sum of non prime digits in a given number:
num = (input("enter1:"))
flag = True
sum1 = 0
len_num = len(num)
for i in range(0,len_num):
    non_prime = num[i]
    for j in range(2,(int(non_prime) // 2)+1):
        if int(non_prime) % j == 0:
            flag = False
            # print("non pime:",non_prime)
            sum1 += int(non_prime)
            break
print(sum1)   

# 2nd method:
num = input("Enter a number: ") 
sum1 = 0  
for i in num:
    if i in "014689":
        sum1 += int(i)
print(sum1)   

# 1. Find the sum of all elements in a nested list.
list_sum = [[1,2,3],[4,5,6],[6,8,9]]
sum1 = 0
for i in range(len(list_sum)):
    sum1 = 0
    for j in list_sum[i]:
        sum1 += j
    print(sum1)
    

# 2. Find the minimum and maximum values in a nested list
   list_sum = [[1,2,3],[4,5,6],[6,8,9]]
# max1 = 1
# min1 = 0
list_sum = [[1,2,3],[4,5,6],[6,8,9]]

for i in range(len(list_sum)):
    max1 = list_sum[i][i]
    min1 = list_sum[i][i]
   
    for j in list_sum[i]:
        if j > max1:
            max1 = j
        elif j < min1:
            min1 = j
    print(list_sum[i],"max",max1)
    print(list_sum[i],"min",min1)
    
    
    



        