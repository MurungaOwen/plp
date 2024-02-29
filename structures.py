my_list=[]#create an empty list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

list2=[50, 60, 70]
my_list.insert(1,15) #insert 15 at kindex number 1 that is the second position

my_list.extend(list2)#add contents of list2 to mylist


#remove last element from my list
del my_list[-1]
#sort my list in ascending order
my_list_sorted=(sorted(my_list,reverse=False))
#find and index 30
print(my_list.index(30))

