import numpy as np
numbers = [12,34,5,3,10]
           
array = np.array(numbers)

add = array+20

sub = array-2

multiply = array*5

mean= np.mean(array)

print("Original List:", numbers)
print("Array:",array)
print("After Adding 5:", add)
print("After subtracting 5:",sub)
print("After Multiplying by 2:", multiply)
print("Mean of Array:", mean)
