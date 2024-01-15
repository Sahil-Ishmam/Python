numbers = [1,3,4,5,6,1,7,8,9,10,1]

print(numbers[:])
numbers.append(11)
print(numbers[:])



numbers.insert(1,2)
print(numbers[:])

numbers.remove(5)
print(numbers[:])

numbers.pop()
print(numbers[:])

# numbers.clear()
print(numbers[:])

numbers.reverse()
print(numbers[:])

print(numbers.count(1))
print(numbers.count(101))


print(numbers[:])


num2 = numbers.copy()
print(num2[:])
numbers.extend(num2)
print(numbers[:])
numbers.insert(9,999)

print(numbers[:])


numbers.sort()
print(numbers[:])
numbers.sort(reverse = True)
print(numbers[:])
