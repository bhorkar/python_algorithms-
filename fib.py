
store = {};


def fib(n):
 global store;
 if n == 0:
     return 0;
 if n == 1:
     return 1;
 if n in store:
     return store[n];
 store[n] =  fib(n-1) + fib(n-2);
 return store[n]

if __name__ == "__main__":
    x =  fib(10)
    print x;
