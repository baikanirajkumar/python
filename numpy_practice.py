"""what is numpy:Numpy stands for numerical python.
                It is a python library used to work with :
                1.Numbers
                2.Arrays
                3.Matrices
                4.Mathematical calculations
                5.Statistics
                6.Machine learning data
        Without Numpy,Python uses lists
        With Numpy ,Python uses arrays,which are:
        1.Faster
        2.consume less memory
        3.Easier for mathematical operations"""

# #Why do we need Numpy?
# #Python list
# a=[1,2,3]
# b=[4,5,6]
# print(a+b)#here + joins the lists

# #Numpy Array
# import numpy as np
# a=np.array([1,2,3])
# b=np.array([4,5,6])
# print(a+b) #adds element by element
# #This is why Numpy is powerful

# #install Numpy
# """pip install numpy
# Check version: """
# import numpy as np
# print(np.__version__)

# #import numpy
# import numpy as np # np is just a shortcut

#what is an array?
#An array stores multiple values of same type
# import numpy as np
# arr=np.array([1,2,3])
# print(arr)
# print(type(arr)) #type of array

"""Difference Between List and Array
Python List	NumPy Array
Slower	        Faster
More memory	Less memory
Cannot perform  Supports mathematical operations
 mathematical 
operations directly"""

# #creating Array
# #1-D Array
import numpy as np
# a=np.array([1,2,3,4])
# print(a)


# #2-D array
# a=np.array([[1,2],[3,4]])
# print(a)

#3-D array
# a=np.array([
#     [[1,2],[3,4]],
#     [[5,6],[7,8]]
# ])
# print(a)

# print(type(a))

# print(a.shape)#(2, 2, 2)
"""First 2 → 2 layers
Second 2 → 2 rows in each layer
Third 2 → 2 columns in each row"""


"""1D → A line of numbers
2D → A table (rows and columns)
3D → A collection (stack) of tables"""
# a=np.array([1,2,3])
# b=np.array([[1,2,3],[4,5,6]])
# c=np.array([
#     [[1,2],[2,3]],
#     [[3,3],[6,7]]
#     ])
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)

# #shape means rows and columns
# a=np.array([[1,2,3],[4,5,6]])
# b=np.array([1,2,3])
# print(a.shape)
# print(b.shape)
# #size :Total elements
# print(a.size)

# #datatype
# print(a.dtype) #int64


# a=np.array([1.5,6.7,3.4])
# print(a.dtype) #float64


# #change data type
# a=np.array([1,2,3],dtype=float)
# print(a)
# print(type(a))


#creating arrays in Numpy

#np.zeros:creates an array filled with 0s
import numpy as np
# a=np.zeros(5) #by default Numpy creates arrays with the float64 datatype
# print(a)

#integer Zeros(1D)
# a=np.zeros(5,dtype=int)
# print(a)

# 2D
# b=np.zeros((2,3))
# print(b)
#3D
# b=np.zeros((2,3,4),dtype=int)
# print(b)

#np.ones:create an array filled with 1's
#1D
# a=np.ones(2)
# print(a)

# a=np.ones(2,dtype=int)
# print(a)
# #2D
# a=np.ones((2,3))
# print(a)

# a=np.ones((2,3),dtype=int)
# print(a)


#3D
# a=np.ones((2,3,4))
# print(a)
# a=np.ones((2,3,4),dtype=int)
# print(a)

#3.np.empty():Allocates memory without initialization
# a=np.empty((2,3))
# print(a)
# a.fill(10) #filling an empty array
# print(a)


#4.np.full():Fill with a custom value
# a=np.full((2,3),5)
# print(a)


# create values with a fixed step

# 1.np.arange()
# import numpy as np
# a=np.arange(1,10,1)#np.arange(start,stop,end)
# print(a)

# a=np.arange(2,10)
# print(a)

# a=np.arange(1,20,2)
# print(a)

# a=np.arange(10,1,-2)
# print(a)

#float step
# a=np.arange(1,10,0.5)
# print(a)

# a=np.arange(-5,6)
# print(a)


#2.np.linspace()
# a=np.linspace(1,10,5) #start value and stop value and number of values to generate
# print(a) #here stop value is included

"""Difference between values:

(10-1)/(5-1)
9/4
2.25
So:
1
3.25
5.5
7.75
10"""


# a=np.linspace(0,1,6)
# print(a)


# a=np.linspace(10,20,11)
# print(a)


# a=np.linspace(-5,5,5)
# print(a)

#endpoint=False
# a=np.linspace(1,10,5,endpoint=False)
# print(a)
#[1.  2.8 4.6 6.4 8.2]

#np.logspace()
# a=np.logspace(1,3,3) #(start,stop,number of values to generate)
# print(a) #[  10.  100. 1000.]
"""10^start
to
10^stop"""


#identity matrix
"""Definition
An Identity Matrix is a square matrix in which:
All diagonal elements are 1
All other elements are 0"""
# import numpy as np 
# a=np.eye(3) #square matrix(3 rows,3 columns)
# print(a)

# a=np.eye(4) #square matrix(4 rows,4 colums)
# print(a)

# #rectangular matrix 
# a=np.eye(3,4)
# print(a)

# #datatype
# a=np.eye(3,4,dtype=int)
# print(a)

#method 2:np.identity()
#It also creates an identity matrix
# a=np.identity(4)
# print(a)

# np.eye=can create rectangular matrices(3 rows,4 columns)
# np.identity:Can create square matrices(3 rows,3 columns)

#2.Diagonal matrix
"""A Diagonal matrix is a square matrix where:
only the diagonal contains values
Every other element is 0"""
# a=np.diag([1,2,3])
# print(a)

# a=np.diag([10,20,30,40,50])
# print(a)

# a=np.diag([50])
# print(a)


a=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(np.diag(a))

"""Difference Between Identity and Diagonal Matrix
Identity Matrix	                Diagonal Matrix
Diagonal values are always 1	Diagonal values can be any numbers
Others are 0	                Others are 0"""