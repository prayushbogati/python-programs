import numpy as np
# MATRICES

# unlike arrays, matrices can't have more than 2 dimensions

# create matrices using np.array() or np.matrix()[not recommended though]
# matrices are special as they can have  * and ** operations between them

# using arrays there are methods like np.dot for matrix mul as np.matrix is not suggested 

# transposition using np.transpose()

# create identity matrix using np.eye(n) or np.identity(n)


# array filtering
    # 1. using boolean indexing as before..
    # 2. using where methods
    #     ex: 
    #     array1 = np.array([[1,2,-1,-2,10,12,20],[1,2,3,-6,1,-10,-1]])
    #     # replace negative values with 0
    #     print(np.where(array1 > 0, array1, 0))
    # 3. use np.any(arr_condition) to show any elements matching the condition using bool values
    # 4. use np.all(arr_condition) to show if all elements match the condition
    #         for 3 and 4, use another attribute 'axis' 0(for col) and 1(for row) to perform on rows and cols
    # 5. np.stack((arr1, arr2, ..), axis) to merge arrays axis 0 for default merge and 1 for merge in cols (..lil confusing)
    # 6. mask same as normal filtering using boolean indexing
    # 7. use MaskedArray from numpy.ma as,
    #     masked_arr = MaskedArray(array1, mask_condition) 
    #     to mask the array and hide the elements satisfying the condition


# broadcasting
    # - method of performing operations on arrays with different dimensions
    # - An array with a smaller shape is expanded to match the shape of a larger one
    # - A set of dimension lengths is compatible when
    #     one of them has a length of 1 or
    #     they are equal
    #     ex.
    #         array1 = shape(6, 7)
    #         array2 = shape(6, 1)