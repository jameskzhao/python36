mylist = ['a','b','c','d','e']
print(mylist)
print(len(mylist))
print(mylist[-1])
print(mylist[::3])

#lists are mutable
mylist[0] = 'new item'
print(mylist)


mylist.append('new item end')
print(mylist)

# difference between append and extend
mylist.append(['x','y','z'])
print(mylist)
mylist.extend(['x','y','z'])
print(mylist)

#pop
item = mylist.pop();
print(mylist)
print(item)
item = mylist.pop(-3)
print(item)
print(mylist)
mylist.sort()
print('after sort')
print(mylist)

def mySortFunc(e):
    return len(e)

#reverse
mylist.reverse()
print('after reverse')
print(mylist)

#sort
mylist.sort(key=mySortFunc)
print(mylist)
mylist.sort(reverse=True, key=mySortFunc)
print(mylist)

numList = list()
for x in range(12):
    numList.append(x)
print(numList)
numList.sort(reverse=True)
print(numList)

#nested lists
matrix = [[1,2,3],[4,5,6],[7,8,9]]
first_col = [row[0] for row in matrix]
print(first_col)
print(type(first_col))