my_income = 100 # int
tax_rate = 0.1 #float
my_taxes = my_income * tax_rate #float

#comment
print(my_taxes)#comment
"""This is a single line docstring"""
"""This is a 
multiline docstring"""


if my_taxes < 50: 
    print("you are such a poor guy")
# no single line if so the next line will get an invalid syntax error
# print(my_taxes < 50 ? 'yes you are poor':'no you are not poor')


#use type() function to verify the type of any object
print(type(my_income))
print(type(tax_rate))
print(type(my_taxes))

#Complex numbers: didn't get it. no idea when to use them

x = complex(1,2)
print(x)
y = complex(3,4)
print(y)
z = x + y
print(z)
z = x * y
print(z)
print(type(z))

#Casting
x = int(2.8)
y = int("3")
z = int(10)
print(x)
print(y)
print(z)
x = float('300')
y = float(3.23490)
z = float(2)
print(x)
print(y)
print(z)

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

print(x)
print(y)
print(z)

#Operators

x = 31
y = 5
print( x + y )
print( x - y )
print( x * y )
print( x / y )
print( x % y )
print( x ** y ) #x to the power of y(^ is xor operator in pyton)
print( x // y ) #floor devision, floor(x/y)