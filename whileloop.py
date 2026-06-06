#while loop ->  condition true hai.

#we have to make while condition false at some point otherwise it will become infinite loop.

# i = 0  #jab tk condition true while will keep executing


# while i < 11:
#     if i == 5:
#         break
#     print(i)
#     i = i +1



# num = 1054
# sum = 0
# while num > 0:
#     last = num % 10  #last digit ko print krdega
#     sum = sum + last
#     num = num // 10   #last digit ko remove krdega
# print ("num is", num)
# print("sum is:-",sum)




#q- check a no is pailindrome or not?

#(pailindrome no is the no jo aange se or peeche se dono se side se parhne pe same hoga, for ex. 1221)

# num = 1221
# copy = num
# reverse = 0
# while num > 0:
#     last = num % 10
#     reverse = reverse * 10+ last
#     num = num // 10

# if copy == reverse:
#     print(f"{copy} is a pailindrome number")
# else:
#     print(f"{copy} is not a palindrome number")





#qu= number is armstrong or not.
# 153 -> 1 5 3 -> 1^3 + 5^3 + 3^3 = 153

# num = 153
# power = len(str(num))
# sum = 0
# copy = num

# while num > 0:
#     last = num % 10
#     print(last**power)
#     num = num // 10
# if copy == sum:
#     print(f"{copy} is an armstrong number")
# else:
#     print(f"{copy} is not an armstrong number")





#perfect number

# num = 6
# sum = 0
# for i in range (1,num):
#     if num % i == 0:
#         sum += i
# if sum == num:
#     print(f"{num} is a perfect number")
# else:
#     print(f"{num} is not a perfect number")




# *
# **
# ***
# ****
# *****

# row = 5 
# for i in range (1, row+1):
#     print("*" * i)




