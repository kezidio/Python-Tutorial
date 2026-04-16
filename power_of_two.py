#A simple program that asks the user for a number of iterations and then prints powers of 2 from 
# 2^0 to 2^n. It uses a while loop to incrementally compute and display each value.
# Author: Kaweny Ezidio

#declare a variable to store the amount of numbers to print
n = int(input("Enter a positive number of iterations: "))

#declare the initial iteration
i=0

#create a while loop to print n+1 calculations
while i<=n:
	#display 2^i
	print(2**i)
	i=i+1 #adding 1 to i makes the loop keep going
