a=[[1,14],[5,6],[8,23]]
a.sort(key=lambda x:x[1])
print(a)


nums = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, nums))
print(result)


nums = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)


from functools import reduce
nums = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, nums)
print(result)


def apply_func(x, func):
    return func(x)

print(apply_func(5, lambda x: x * x))