# A simple program that checks whether a given number is 
# prime or not by testing its divisibility.
# Author: Kaweny Ezidio

#declare variable and ask user to enter number
number=int(input("Please enter a whole number: "))

#declare a variable to check if remainder
div=2

#declare a variable and store value true or false
prime=True

#create a while loop to check remainders 
#while 2 <= num-1 and true
while(div<=number-1) and (prime):
        #if number remainder = 0
        if(number%div==0):
                prime= False
         #increase variable for remainder check       
        div=div+1
        
#now we check if prime is true and number input is different than 1       
if(prime and not number==1):
        print("Prime number!")
# else, if prime is false         
else:
        print("Not a prime number!")
        

        
        
        
