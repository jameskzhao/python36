mylist = ['a','b','c','d','e']
print(mylist)
print(len(mylist))
print(mylist[-1])
print(mylist[::3])
mylist[0] = 'NEW ITEM'
print(mylist)

# difference between append and extend
mylist.append('new item end')
print(mylist)
mylist.append(['x','y','z'])
print(mylist)
mylist.extend(['x','y','z'])
print(mylist)
item = mylist.pop();
print(mylist)
print(item)