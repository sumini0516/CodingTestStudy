import math

result1 = list(map(int, [1.1, 2.2, 3.3]))
print(f'map(int, 리스트) : {result1}')

def func_pow(x):
    return pow(x,5)


result2 = list(map(func_pow, [1,2,3,4]))
print(f'map(func_pow, 리스트) : {result2}')
