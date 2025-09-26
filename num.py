import numpy
arr=numpy.array([1, 2, 3, 4, 5])
print(arr) 
# Numpy is used to work with arrays
# we can create a numpy ndarray object by using the array()function
import numpy as np
arr=np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

import numpy as np
arr=np.array((1, 2, 3, 4, 5, 6))
print(arr)
# o-Darrays, or scalars, are the elements in an arry.
import numpy as np
arr=np.array(42)
print(arr)
# create a 2-D array containing two arrys with the values 1,2,3 and 4,5,6:
import numpy as np
arr=np.array([[1, 2,3], [4, 5, 6]])
print(arr)
# 3-D create a 3-D array with two 2-D arrays, both contining two arrays with the values 1,2,3and 4,5,6:
import numpy as np
arr=np.array([[[1, 2, 3], [4, 5, 6, ], [1, 2, 3], [4, 5, 6]]])
print(arr)
#check how many dimenstions the arrays have:
import numpy as np

a=np.array(42)
b=np.array([1, 2, 3, 4, 5])
c=np.array([[1, 2, 3], [4, 5, 6]])
d=np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
#Hgher Dimension Arrays
# create an array with 5 dimenstion and verify that it has 5 dimenstions:
import numpy as np
arr=np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimentions :', arr.ndim)

# NUMPY ARRAY INDEXING
# access array elements
import numpy as np # get the element from the following
arr=np.array([1, 2, 3, 4, ])
print(arr[0]) #1

import numpy as np
arr=np.array([1, 2, 3, 4])
print(arr[1])#2
print(arr[2] + arr[3]) # 7

# Access 2-D Arrays
import numpy as np
arr=np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on st row: ', arr[0, 1])
print('5th element on 2nd row: ', arr[1, 4])
# Access the third element of the second array of the first array:
import numpy as np
arr=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])

# NUMPY ARRAY SLICING
# slice elements from index 5 from the following array:
import numpy as np
arr=np.array([1, 2, 3, 4,5, 6, 7])
print(arr[1:5]) #[2 3 4 5]
print(arr[4:])#slice elements from index 4 to end of the array: [5 6 7]
print(arr[:4])#silce elements from the begining to index4 (not included):

import numpy as np
arr=np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1]) #[5 6]slice frome the index 3 from the end to index 1 from the end
#step return every other element from index 1 to index 5:
import numpy as np
arr= np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])
#return every other element from the entire array:
print(arr[::2])
# Slicing 2-D Arrays 
# from the second element, slice elements from indee 4(not included):
import numpy as np
arr=np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
print(arr[1, 1:4])# [7 8 9]
print(arr[0:2, 1:4])# [[2 3 4][7 8 9]]
##NOT: Remember that second element has index 1.

# NUMPY DATA TYPES
# Get the data type of an array object:
import numpy as np 
arr=np.array([1, 2, 3, 4])
print(arr.dtype)

import numpy as np
arr=np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

# creating Arrays with a Defined Data Type
import numpy as np
arr=np.array([1, 2, 3, 4], dtype='S')
print(arr) #[b'1' b'2' b'3' b'4']
print(arr.dtype) #|S1

# create an array with data type 4 bytes integer:
import numpy as np
arr=np.array([1, 2, 3, 4, 5], dtype='i4')
print(arr) #[1 2 3 4]
print(arr.dtype) # int32
# change data type fromfloat to integer by using 'i' as parameter value:
import numpy as np
arr=np.array([1.1, 2.1, 3.1])
newarr=arr.astype('i')
print(newarr) #[1 2 3]
print(newarr.dtype) # int32
# Change data type float to integer by using init as parameter value:
import numpy as np
arr=np.array([1.1, 2.1, 3.1])
newarr=arr.astype(int)
print(newarr)
print(newarr.dtype)

import numpy as np
arr=np.array([-1, 0, 3])
newarr=arr.astype(bool)
print(newarr)
print(newarr.dtype)

# NUMPY ARRAY COPY VS VIEW
#COPY
# make a copy, change the original array, and display both arrays:
import numpy as np 
arr=np.array([1, 2, 3, 4, 5])
x=arr.copy() # The copy SHOULD NOT be affected by the changes made to the original array
arr[0]=42
print(arr) #[42 2 3 4 5]
print(x)  #[1 2 3 4 5]

#VIEW:
# make a view, change the original array, and display both arrays:
import numpy as np
arr=np.array([1, 2, 3, 4, 5])
x=arr.view()
arr[0]=42
print(arr) #[42 2 3 4  5]
print(x)  #[42 2 3 4 5]
# Check if Array Owns its Data
# print the value of the base attribute to check if an array owns it`s data or not:`
import numpy as np
arr=np.array([1, 2, 3, 4, 5])
x=arr.copy() # the copy returns none
y=arr.view() # The view returns the original array.
print(x.base) # None
print(y.base)  #[1 2 3 4 5]
# NUMPY ARRAY SHAPE
# print the shape of a 2-D array:
import numpy as np
arr=np.array([[1, 2, 3, 4], [5, 6, 7,8]])
print(arr.shape)  #(2, 4)
# create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:
import numpy as np 
arr=np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)

# NUMPY ARRAY ITERATING
# Iterate on the elements of the forllowing 1-D array:
import numpy as np
arr=np.array([1, 2, 3])
for x in arr:
    print(x)

# Iterate on the elements of the following 2-D array:
import numpy as np 
arr=np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    print(x) # [1 2 3]
            # [4 5 6]
# Iterate on each scalar element of the 2-D array:
import numpy as np 
arr=np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    for y in x:
        print(y) #it will print doun words
# Iterate on the elements of the following 3-D array:
import numpy as np
arr=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)
    print (x)
# Iterate through the array as a string:
import numpy as np
arr=np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)
# Enumerated iteration using ndenumerate()
import numpy as np
arr=np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
    print(idx, x)

import numpy as np
arr=np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)
# NUMPY JOINING ARRAY
# Join two arrays
import numpy as np
arr1=np.array([1, 2, 3])
arr2=np.array([4, 5, 6])
arr=np.concatenate((arr1, arr2))
print(arr)
# Join two 2-D arrays along rows (axis=1):
import numpy as np
arr1=np.array([[1, 2], [3, 4]])
arr2=np.array([[5, 6], [7, 8]])
arr=np.concatenate((arr1, arr2), axis=1)
print(arr)
# Joining Arrays Using stack Functions
import numpy as np 
arr1=np.array([1, 2, 3])
arr2=np.array([4, 5, 6])
arr=np.stack((arr1, arr2), axis=1)
print(arr)

#Stacking Along Rows
# Numpy provides a helper funcrion:hstack() to stack along row.
import numpy as np
arr1=np.array([1, 2, 3])
arr2=np.array([4, 5, 6])
arr=np.hstack((arr1, arr2))
print(arr) # [1 2 3 4 5 6]

# Stacking Alon Columns
# NUmpy provides a helper function:Vstack() to stack along columns.
import numpy as np 
arr1=np.array([1, 2, 3])
arr2=np.array([4, 5, 6])
arr=np.vstack((arr1, arr2))
print (arr)

# Stacking Along Height (depth)
# numpy provides a helper function:dstack()to stack along height,which is the same as depth
import numpy as np
arr1=np.array([1, 2, 3])
arr2=np.array([4, 5, 6])
arr=np.dstack((arr1, arr2))
print(arr)

# NUMPY SPLITTING ARRAY
# split the array in 3 parts
import numpy as np
arr=np.array([1, 2, 3, 4, 5, 6])
newarr=np.array_split(arr, 3)
print(newarr)
#Access the splitted arrays
import numpy as np
arr=np.array([1, 2, 3, 4, 5, 6])
newarr=np.array_split(arr, 3)
print(newarr[0]) #[1 2]
print(newarr[1]) #[3 4]
print(newarr[2]) #[5 6]

# Splittin 2-D Arrays
import numpy as np
arr=np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 2]])
newarr=np.array_split(arr, 3)
print(newarr)
# Split the 2-D array into three 2-D arrays along columns.
import numpy as np
arr=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
newarr=np.array_split(arr, 3, axis=1)
print(newarr)
# use the hsplit() method to split the 2-D array into three 2-D arrays along columns.
import numpy as np
arr=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(newarr)
newarr=np.hsplit(arr, 3)
# NUMPY SEARCHING ARRAY
# Find the indexes where the value is 4
import numpy as np
arr=np.array([1, 2, 3, 4, 5, 4, 4])
x=np.where(arr == 4)
print(x) # (array([3, 5, 6]),)
# find the indexes where the  value are even:
import numpy as np 
arr=np.array([1, 2, 3, 4, 5, 6, 7, 8])
x=np.where(arr%2 == 0)
print(x) # (array([1, 3, 5, 7]),)
# Find the indexes where the values are odd:
import numpy as np
arr=np.array([1, 2, 3, 4, 5, 6, 7, 8])
x=np.where(arr%2 == 1)
print(x) # (array([0, 2, 4, 6]),)
# search sorted
# find the indexes where the value 7 should be inserted
import numpy as np
arr=np.array([6, 7, 8, 9])
x=np.searchsorted(arr, 7)
print(x)# 1
# Find
import numpy as np
arr=np.searchsorted(arr, 7, side='right')
print(x) #1

import numpy as np
arr=np.array([1, 3, 5, 7])
x=np.searchsorted(arr,[2, 4, 6])
print(x)  # [1 2 3]

# NUMPY SORTIN ARRAY
# sort the array
# NOTE: This method returns a copy of the array, leaving the original array unchanged
import numpy as np
arr=np.array([3, 2, 0, 1])
print(np.sort(arr)) # [0 1 2 3]


# NUMPY FILTER ARRAY
# create an array from the elements on index 0 and 2
import numpy as np
arr=np.array([41, 42, 43, 44])
x=[True, False, True, False]
newarr=arr[x]
print(newarr) # [41 43]

# Create a filter array that will return only values higher than 42
import numpy as np
arr=np.array([41, 42, 43, 44])
#create an empty list
filter_arr= []
# go through each element in arr
for element in arr:
    # if the element is higher than 42, set the value to Tue, otherwise False:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False) 
newarr=arr[filter_arr]
print(filter_arr) # [False, False, True, True]
print(newarr)   #[43 44]

# create a filter array that will return only even elements from the original array:
import numpy as np
arr=np.array([1, 2, 3, 4, 5, 6, 7])

#create an empty list
filter_arr=[]
# go through each element in arr
for element in arr:
    # if element is completely divisble by 2, set the value to True, otherwise False
    if element % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr=arr[filter_arr]
print(filter_arr) # [Fase True False True False]

print(newarr) # [2 4 6]
# Create a filter array that will return only values higher than 42:
import numpy as np
arr=np.array([41, 42, 43, 44])
filter_arr=arr > 42
newarr=arr[filter_arr]
print(filter_arr) # [False False True True]
print(newarr)  # [43 44]

import numpy as np
arr=np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr=arr % 2 == 0
newarr=arr[filter_arr]
print(filter_arr) # [False True False True False True False]
print(newarr) # [2 4 6]


# NUMPY UNFUNCS

# check you own ufunc for addition:
import numpy as np
def myadd(x, y):
    return x+y
myadd=np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))
# check if a function is a ufunc:
import numpy as np 
print(type(np.add))# <class `numpy.unfunc`>
# check the type of another function:concatenate():
import numpy as np
print(type(np.concatenate))

 # Add the values in arr1 to the values in 2:
import numpy as np
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2)
print(newarr)

# Subtract the value in arr2 from the value in arr1
import numpy as np
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.subtract(arr1, arr2)
print(newarr)

# Divide the value  in arr1 with the values in arr2

import numpy as np
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.subtract(arr1, arr2)
print(newarr)






















