import pandas

#this is our dataframe
cars = pandas.read_csv('cars.csv')

columns = cars.columns
for i, col in enumerate(columns):
    print('%.2d: %s' %(i, col))

data = cars.values.astype('float')


import numpy
matrix_a = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_a[1]
array([4, 5, 6])
>>> matrix_a
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> matrix_a[1][2]
6
>>> matrix_a * 2
array([[ 2,  4,  6],
       [ 8, 10, 12],
       [14, 16, 18]])
>>> matrix_a.dot(marix_a)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    matrix_a.dot(marix_a)
NameError: name 'marix_a' is not defined
>>> matrix_a.dot(matrix_a)
array([[ 30,  36,  42],
       [ 66,  81,  96],
       [102, 126, 150]])
>>> 
