import numpy as np
my_list = [1, 2, 3, 4, 5]
my_vector = np.array(my_list)
print(my_list, type(my_list))
print(my_vector, type(my_vector))
print(f"First element of list: {my_list[0]}")
print(f"First element of vector: {my_vector[0]}")
#array slicing and intro
my_2d_array = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D array:\n{my_2d_array}")
print(f"Slice of 2D array: \n{my_2d_array[1][1:3]}")
#array indexing and reassigning indices
my_3d_array = np.array([[[9, 10], [11, 12]], [[13, 14], [15, 16]]])
print(f"3d array: \n{my_3d_array}\n")
print(f"slice of 3d array: \n{my_3d_array[0][1][1]}\n")
my_3d_array[1][1][0] = 5
print(f"New 3d array: \n{my_3d_array}\n")
#array arithmetic
u = np.array([1, 2, 3])
v = np.array([4, 5, 6])
print(u * 3)
print(u + 2)
print(u / 2)
print(f"smol element is: {np.min(my_3d_array)}")
print(f"smol element location: {np.argmin(my_3d_array)}")
my_flat_3d_array = my_3d_array.flatten()
print(f"flattened 3d array: {my_flat_3d_array}")
my_array= np.array([[1, 2], [3, 4]])
print(f"first question: {my_array[-1]}")
print(f"second question: {my_array[::-1]}")
print(f"third question: {np.sort(my_array)[0]}")
print(f"np.max(my_array)[0]: {np.max(my_array)[0]}")
print(f"np. max(my_array, axis=0): {np.max(my_array, axis=0)[0]}")
print(f"np.max(my_array, axis=1): {np.max(my_array, axis=1)[0]}")