#This program defines four functions: sum(x, y, z): returns the sum of three numbers.
#mult(x, y, z): returns the product of three numbers.
#string(): returns the text "SPFC".
#function(): calculates 10 + 20 and prints the result.
#Then calls each function to either display or return its result.

def sum(x, y, z):
    return x + y + z

def mult(x, y, z):
    return x * y * z

def string():
    return "SPFC"

def function():
    x = 10 + 20
    print("The result is ", x)


# function calls

# sum
result_sum = sum(2, 3, 4)
print("Sum:", result_sum)

# mult
result_mult = mult(2, 3, 4)
print("Product:", result_mult)

# string
team = string()
print("String function returns:", team)

#
function()
