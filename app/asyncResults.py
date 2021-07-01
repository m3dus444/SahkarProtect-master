""" This script explain how is used ThreadPool around the whole script
    we won't use map/map async. Only apply_async for now.
    The usage is following:
    pool = ThreadPool(processes=X) attribute X process to our object pool.
    For each process we can give it work as pool.apply_async(script.fucntion,('X', Y, ...))
    Where apply_async take non used thread to execute function from script.
    X , 'Y', etc are args for the function called.

    When we know a pool is not gonna be used after its call anymore we can do
    a pool.close() right after the async calls. We won't be able to get result
    from it but it will terminate itself when work is done.
    To get possibly errors we can do a pool.join() which will give us errors usually impossible
    to know their existence.
    When a job is started with an async call, we can continue to do stuff.
    When can check at every time is the work is finished with
    async.result.ready() boolean state. When it's true, we grab result with
    async.result.get(). After that we can terminate/close pool or wait to
    callback an async function"""




from multiprocessing.pool import ThreadPool
import time
import SuspiciousHandler
from sys import getsizeof
pool = ThreadPool(processes=3)
print(getsizeof(pool))
print(pool)


class Person:

    # init method or constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Sample Method

    def say_hi(self, test):
        print('Hello, my name is' + self.name + " " + test)

def creatPerson(name):
    return Person(name)
def sayhi(Person, message):
    Person.say_hi(message)


p = Person('Nikhil', 22)
p.say_hi("this is the test")
"""nom = " Batsien"

result_async = pool.apply_async(Person, ("awee", 22))
time.sleep(1)
bastien = result_async.get()
print(bastien)
bastien.say_hi("je bagaye")"""

#returnval = async_result.get()
#print(returnval)
#print(A.returning(2))
"""async_result = pool.apply_async(white.bigtest, ('2', 1)) # tuple of args for foo
async_result2 = pool.apply_async(white.bigtest, ('3', 2))
async_result3 = pool.apply_async(white.bigtest, ('4', 3))
#pool.close()
print(getsizeof(pool))
time.sleep(1)

while not async_result3.ready():
    time.sleep(0.4)
    print("no 3")
    if not async_result2.ready():
        print("no 2")
    if not async_result.ready():
        print("no 1")
    # do some other stuff in the main process


return_val = async_result.get()  # get the return value from your function."""

"""pool.terminate()
print("terminate state :", pool)
pool = ThreadPool(processes=2)
pool.terminate()
print("redefinbed pool : ", pool)
sync_result = pool.apply_async(white.bigtest, ('2', 4))
print("redefinbed pool started new process : ", pool)
#del pool
pool.close()
time.sleep(1)
print(return_val)
pool.close()
print(pool.join())"""