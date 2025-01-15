# The time module in Python provides a set of functions to work with time-related operations, such as timekeeping, formatting, and time conversions.

'''time.time()'''
 
# The time.time() function returns the current time as a floating-point number, representing the number of seconds since the epoch (
# the point in time when the time module was initialized). The returned value is based on the computer's system clock and is affected 
# by time adjustments made by the operating system, such as daylight saving time.

import time
print(time.time())
# Output: 1602299933.233374 always changes

# can be used for measuring the duration of an operation or the elapsed time since a certain point in time.


# def usingWhile():
#   i = 0
#   while i<50000:
#     i = i +1
#     print(i) 

# def usingFor():
#   for i in range(50000):
#     print(i)

# init = time.time()
# usingFor()
# t1 = time.time() - init   

# time.time (epoch) - time.time (init) vo bhi epoch wala hi do bar called, but in mid we called the function for loop, so if we subtract both time.time , we get the diffference time equal to time taken by loop for execution

# init = time.time()         # called here
# usingWhile()         # called loop
# print(time.time() - init)        # called here - init to get loop execution time
# print(t1)

'''minor differnce in execution of for and while loop'''


'''The time.sleep() function suspends the execution of the current thread for a specified number of seconds. This function can be used to pause 
the program for a certain period of time, allowing other parts of the program to run, or to synchronize the execution of multiple threads.'''

import time

print("Start:", time.time())
time.sleep(2)
print("End:", time.time())
# Output:
# Start: 1602299933.233374
# End: 1602299935.233376



print(4)
time.sleep(3)
print("This is printed after 3 seconds")
 
#As you can see, the function time.sleep() suspends the execution of the program for 2 seconds, allowing other parts of the program to run during that time.


'''The time.strftime() function formats a time value as a string, based on a specified format. This function is particularly useful for formatting dates and times in a human-readable format, 
such as for display in a GUI, a log file, or a report. Here's an example:'''

import time

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time)
# Output: 2022-11-08 08:45:33
# time.strftime() formats the current time (obtained using time.localtime()) as a string, using a specified format. 
# The format string contains codes that represent different parts of the time value, such as the year, the month, the day, the hour, the minute, and the second.