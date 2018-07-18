#Basics

a = "hello"
a += " I'm a dog"
print(a)
print(len(a))
print(a[1:]) #Output: ello I'm a dog
print(a[:5]) #Output: hello(index 5 is not included)
print(a[2:5])#Output: llo(index 2 is included)
print(a[::2])#Step size 

#string is immutable so you can't assign a[1]= b
x = a.upper()
print(x)
x = a.capitalize()
print(x)
x = a.split('e')
print(x)
x = a.split() #splits the string by space
print(x)
x = a.strip() #removes any whitespace from beginning or the end
print(x)
x = a.replace('l','xxx')
print(x)

x = "Insert another string here: {}".format('insert me!')
x = "Item One: {} Item Two: {}".format('dog', 'cat')
print(x)
x = "Item One: {m} Item Two: {m}".format(m='dog', n='cat')
print(x)

#command-line string input

print("Enter your name:")
x = input()
print("Hello: {}".format(x))