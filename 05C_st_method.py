b=set()
print(type(b))
#1 adding value to an empty set
b.add(3)
b.add(4)
b.add(2)
b.add(3)#adding value repeatedly
b.add((17,3,56))
#b.add([1,3,4,5])
#b.add({4,5})#cannot add dictionary and list in sets



#2 
print(len(b))

#3
#b.remove(2)
#b.remove(7)#throws an error if not a present element in sets
print(b)

#4 pop
#print(b.pop())

#5 clear
#print(b.clear())

#6 union
c={1,3,4,5,7}
print(type(c))
