#-------------------Assignment of Decorator----------------------------

# 1. Develop a memoization decorator that caches the results of function
# calls and returns the cached result when the same inputs occur again.
# This can greatly improve the performance of recursive or
# computationally intensive functions.

def memoize(func):
    cache = {}                       

    def wrapper(*args):              
        if args in cache:            
            return cache[args]       
        result = func(*args)         
        cache[args] = result         
        return result

    return wrapper


calls_slow = 0
calls_fast = 0

def fib_slow(n):
    global calls_slow
    calls_slow = calls_slow + 1
    if n < 2:
        return n
    return fib_slow(n - 1) + fib_slow(n - 2)

@memoize
def fib_fast(n):
    global calls_fast
    calls_fast = calls_fast + 1
    if n < 2:
        return n
    return fib_fast(n - 1) + fib_fast(n - 2)


print("fib_slow(25) =", fib_slow(25))
print("Function bodies executed:", calls_slow)

print("fib_fast(25) =", fib_fast(25))
print("Function bodies executed:", calls_fast)

print("fib_fast(25) again =", fib_fast(25))
print("Function bodies executed:", calls_fast, "(no new calls: answer came from cache)")    