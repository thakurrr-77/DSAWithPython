from array import array


arr = array('i',[])

n = int(input('Enter a number'))


for i in range(0,n):
    arr.append(int(input('Enter next input')))

print(arr)

arr.index(45) # tell us the index where 45 exists 

