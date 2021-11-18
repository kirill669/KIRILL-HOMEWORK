from random import randint
nums = [randint(10, 30) for i in range(10)]
print(nums)
# Take any random 10 integers (randint)
nums = [i for i in nums if i%2 == 0 ]
# Condition in list generator
print(nums)