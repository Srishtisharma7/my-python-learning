'''Generators in Python are special type of functions that allow you to create an iterable sequence of values. A generator function returns a 
generator object, which can be used to generate the values one-by-one as you iterate over it. Generators are a powerful tool for working with 
large or complex data sets, as they allow you to generate the values on-the-fly, rather than having to create and store the entire sequence in memory.'''

# In Python, you can create a generator by using the yield statement in a function. The yield statement returns a value from the generator 
# and suspends the execution of the function until the next value is requested.

def my_generator():
    for i in range(5):
        yield i

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# Output:
# 0
# 1
# 2          everytime next request is passed, gets next output
# 3
# 4
# The next() function is used to request the next value from the generator, and the generator resumes its execution until it encounters 
# another yield statement or until it reaches the end of the function.


'''Once you have created a generator, you can use it in a variety of ways, such as in a for loop, a list comprehension, or a generator expression'''

gen = my_generator()
for i in gen:
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

# As you can see, the generator can be used in a for loop, just like any other iterable sequence. The generator is used to generate the values one-by-one as the loop iterates over it.


'''One of the main benefits of generators is that they allow you to generate the values on-the-fly, rather than having to create and store 
the entire sequence in memory. This makes generators a powerful tool for working with large or complex data sets, as you can generate the 
values as you need them, rather than having to store them all in memory at once.

Another benefit of generators is that they are lazy, which means that the values are generated only when they are requested. This allows you 
to generate the values in a more efficient and memory-friendly manner, as you don't have to generate all the values up front.'''



# Function caching

'''Function caching is a technique for improving the performance of a program by storing the results of a function call so that you can reuse 
the results instead of recomputing them every time the function is called. This can be particularly useful when a function is computationally 
expensive, or when the inputs to the function are unlikely to change frequently.
In Python, function caching can be achieved using the functools.lru_cache decorator. The functools.lru_cache decorator is used to cache 
the results of a function so that you can reuse the results instead of recomputing them every time the function is called. Here's an example:'''

import functools

@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(20))
# Output: 6765

# the functools.lru_cache decorator is used to cache the results of the fib function. The maxsize parameter is used to specify 
# the maximum number of results to cache. If maxsize is set to None, the cache will have an unlimited size.

'''Function caching can have a significant impact on the performance of a program, particularly for computationally expensive functions. 
By caching the results of a function, you can avoid having to recompute the results every time the function is called, which can save a 
significant amount of time and computational resources.

Another benefit of function caching is that it can simplify the code of a program by removing the need to manually cache the results of a 
function. With the functools.lru_cache decorator, the caching is handled automatically, so you can focus on writing the core logic of your program.'''


# use lrucache when there are limited and chances of getting repetive no of values , and the program is computationally expensive , so when next time executing it does not take much time

# do not waste memory bulding lrucache when u have to print program like sqaure of numbers from 1 to 100 , hardly any value will repeat  so no need to store each value in memory

from functools import lru_cache
import time

@lru_cache(maxsize=None)     # can set the max sixe , lru cache takes memory of its own
def fx(n):
  time.sleep(5)
  return n*5
    

print(fx(20))
print("done for 20")
print(fx(2))                         # takes 5 sec sleep
print("done for 2")
print(fx(6))
print("done for 6")
print(fx(20))

print("done for 20")
print(fx(2))                        # this time run quickly as do not calculate , but memoize and retrieves from the cache memory
print("done for 2")               # this cache retrival is valid on one run , if we run again cache gets empty and it again calculates for 20, 2, 6 with 5 sec sleep then , cache builds up and here 20,2,6 gets quick execution
print(fx(6)) 
print("done for 6")

print(fx(61))
print("done for 61")           # here again takes 5 sec as 61 is executed first time , so no cache funcn helping