# import array

from array import *


# create array in python using array module 
val = array('i' , [1,2,3,4,5,6])  # here i is typecode please check it in type_code.png file
# val = array('d', [1,2,3,4,5.0])
# val = array('u', ['a','b'])
for i in range(0,len(val)):
    print(val[i] , end = " ") 

print("\n")




# Copy of array
copyArray = array(val.typecode, (x for x in val))

copyArray.pop(2)  # particular index to delete

copyArray.remove(15) # remove a particular element 

for x in val:
    print(x, end = " , ")

print()
print(array.typecode) # to find the typecode for the array 



val.insert(1,5)    # first arg = index to insert and 2nd arg what to insert 

val.append(10)      

val.reverse()
print(val)






# Array Slicing  arr[start_ind:end_ind:skip]




