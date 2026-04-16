import numpy as np 
 # give us the facility to make hetrogeneous array 

val = np.array([1,2,3,4.5], float)


ap = np.linspace(10, 20, 5) # ap arithimetic progression do 5 parts from 10 to 20 and store into the array 

aran = np.arange(10,20,5) # ap arithimetic progresiion distance is 5 means array will be [10,15] 20 will not be included

zer = np.zeros(10)  # create 0 if size 10 array

ons = np.ones(10) # all element of size 1 

fll = np.full(10,5) # 10 size array with all 5
print(val)

print(ap)
print(aran)

print(zer)
print(ons)
print(fll)



# multi dimention array 

mul_array = np.array([[1,2,3],[4,5,6] , [7,8,9]])

print(mul_array)

three_d_array = np.array([[[1,2],[2,3]],[[3,4],[5,6]]])

print(three_d_array)



