def fibonacci(n):
    #print("n is", n)
    if n <= 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    for i in range(1, 10):
        print("fib(%d) is" % i)
        print(fibonacci(i))
