#-------------------------------------------------------------------------------
# Name:        NIKHIL KUMAR SAH
# Purpose:     Question Solving
#
# Author:      NIKHIL KUMAR SAH
#
# Created:     02-09-2022
# Copyright:   (c) NIHIL KUMAR SAH 2022
# Licence:     <TROMS'S licence>
#-------------------------------------------------------------------------------

#Program to enter two number and print the arithmetic operation like =,-,*,/,//?

num1 = float(input("Enter the First value :"))
num2 = float(input("Enter the second value :"))

#Add two number
add = num1 + num2

#subtract two number
sub = num1 - num2

#multiplication of two number
multi = num1 * num2

#division of two number
div = num1 / num2

#modulous of two number
mod = num1 % num2

#exponenet of two number
expo = num1 ** num2


print("The sum of two number is = {2}".format(num1, num2,add))
print("The subtraction  of two number is :",sub)
print("The multiplication of {0} and {1} = {2}".format(num1,num2,multi))
print("The division of two number is = {2}".format(num1,num2,div))
print("The modulus is = {2}".format(num1,num2,mod))
print("The exponential is = {2}".format(num1,num2,expo))