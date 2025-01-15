# Asynchronous I/O, or async for short, is a programming pattern that allows for high-performance I/O operations in a concurrent and 
# non-blocking manner. In Python, async programming is achieved through the use of the asyncio module and asynchronous functions.

# Here is the basic syntax for creating an asynchronous function in Python:

import asyncio
import time
import requests


async def function1():
  print("func 1") 
  URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
  response = requests.get(URL)
  open("instagram.ico", "wb").write(response.content)
   
  return "Harry"
  
async def function2():
  print("func 2") 
  URL = "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"
  response = requests.get(URL)
  open("instagram2.jpg", "wb").write(response.content)
  
async def function3():
  print("func 3")
  URL = "https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
  response = requests.get(URL)
  open("instagram3.ico", "wb").write(response.content)

async def main():
  # await function1()      one by one run
  # await function2()
  # await function3()
  # return 3
  L = await asyncio.gather(        # simultaneous run
        function1(),
        function2(),          
        function3(),
    )
  print(L)
  # task = asyncio.create_task(function1())
  # # await function1()
  # await function2()
  # await function3()




asyncio.run(main())

async def my_async_function():
    # asynchronous code here
    await asyncio.sleep(1)
    return "Hello, Async World!"

async def main():
    result = await my_async_function()
    print(result)

asyncio.run(main())


# Another way to schedule tasks concurrently is as follows:

async def main():
   L = await asyncio.gather(
        my_async_function(),
        my_async_function(),
        my_async_function(),
    )
   print(L)

# Async IO is a powerful programming pattern that allows for high-performance and concurrent I/O operations in Python. With the asyncio module and asynchronous functions, you can write efficient and scalable code that can handle large amounts of data and I/O operations without blocking the main thread. Whether you're working on web applications, network services, or data processing pipelines, async IO is an essential tool for any Python developer





'''Coroutines are mostly used in cases of time-consuming programs, such as tasks related to machine learning or deep learning algorithms, or in cases where the program 
has to read a file containing a large number of data. In such situations, we do not want the program to read the file or data again and again, so we use coroutines to 
make the program more efficient and faster. Coroutines run endlessly in a program because they use a while loop with a true or 1 condition, 
so it may run until infinite time. Even after yielding the value to the caller, it still awaits further instruction or calls. We have to stop the execution of the coroutine 
by calling the coroutine.close() function. It is crucial to close a coroutine because its continuous running can take up memory space, as we have discussed in function caching .
We can define a coroutine using the following statements.'''


def myfunc():
    while True:
        value = (yield)
# The while block continues the execution of the coroutine for as long as it receives values. The value is collected through the yield statement.

# Coroutine Execution:- 

'''Execution is the same as of a generator. When you call a coroutine, nothing happens. They only run in response to the next() and send() methods. Coroutine requires 
the use of the next statement first so it may start its execution. Without a next(), it will not start executing. We can search a coroutine by sending it the keywords 
as input using object name along with send(). The keywords to be searched are send inside the parenthesis. 
When we run the next() function the first time, the coroutine executes and waits for new input. After the input is sent to it using the send() function, 
it executes it and again waits for next input, and the process goes on like this because we have set the while loop as true, so it will never exit its execution. 
In order to make the execution stop, we have to close the coroutine using coroutine.close() function.'''

# send() — used to send data to coroutine
#  close() — to close the coroutine

# Example:

def myfunc():
    print("Code With Harry")
    while True:
        value = (yield)
        print(value)

coroutine =myfunc()
next(coroutine)
coroutine.send("Python")
coroutine.send(" Tutorial ")
coroutine.close()



# After closing the coroutine, if we send values, it will raise the StopIteration exception. Coroutines are used for data processing mechanisms. 
# Coroutines are similar to generators, except they wait for information to be sent to it using send() function.


def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "This is a book on harry and code with harry and good"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()
print("search started")
next(search)
print("Next method run")
search.send("harry")

search.close()
search.send("harry")
# input("press any key")
# search.send("harry and")
# input("press any key")
# search.send("thi si")
# input("press any key")
# search.send("joker")
# input("press any key")
# search.send("like this video")

