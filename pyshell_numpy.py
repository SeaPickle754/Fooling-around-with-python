Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> arr = np.zeros(5)
>>> print(arr)
[0. 0. 0. 0. 0.]
>>> arr = np.zeros((5,4,5))
>>> arr
array([[[0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.]],

       [[0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.]],

       [[0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.]],

       [[0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.]],

       [[0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.]]])
>>> arr=np.ones((5,4,2))
>>> arr
array([[[1., 1.],
        [1., 1.],
        [1., 1.],
        [1., 1.]],

       [[1., 1.],
        [1., 1.],
        [1., 1.],
        [1., 1.]],

       [[1., 1.],
        [1., 1.],
        [1., 1.],
        [1., 1.]],

       [[1., 1.],
        [1., 1.],
        [1., 1.],
        [1., 1.]],

       [[1., 1.],
        [1., 1.],
        [1., 1.],
        [1., 1.]]])
>>> arr = np.array([[1,2,3],[4,5,6],[7,8,9],[0]])
>>> arr
array([list([1, 2, 3]), list([4, 5, 6]), list([7, 8, 9]), list([0])],
      dtype=object)
>>> print(arr)
[list([1, 2, 3]) list([4, 5, 6]) list([7, 8, 9]) list([0])]
>>> """
thank you for checking this out! please leave an issue with an idea for a new
project!
"""
'\nthank you for checking this out! please leave an issue with an idea for a new\nproject!\n'
>>> 