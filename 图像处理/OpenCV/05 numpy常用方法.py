import numpy

array1 = numpy.zeros([3, 3], numpy.uint8)
print(array1)
array2 = array1.reshape([1, 9])
print(array2)
array2.fill(256)
print(array2)