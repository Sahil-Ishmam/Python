numbers = [1,2,3,1,2,8,0]
number_tuple0 = 1,2,3,4,5,1919191,1211
number_tuple = tuple(numbers)
print(number_tuple)
# tuple is immutable , cannot be changed , 
# but if tuple is 2d then it can be changed 
tuple_2d = ([1,2,3,4],[6,7,8,9])
print(tuple_2d)
tuple_2d[0][2] = 33
print(tuple_2d)

print(number_tuple)
print(number_tuple0)

n_t = (64,534,232,2,12,3,3,343,3)
print(n_t)
print(n_t.size())