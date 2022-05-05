def fibonacci_recursive(n):
    if(n <= 1):
        return n
    else:
        return (fibonacci_recursive(n-1) + fibonacci_recursive(n-2))

def fibonacci_while(n):
    a = 0
    b = 1
    sum = 0
    count = 1
    while(count <= n):
        count += 1
        a = b
        b = sum
        sum = a + b
    return sum


if __name__ == "__main__":
    n = 32
    fib_rec = fibonacci_recursive(n)
    print(fib_rec)

    fib_while = fibonacci_while(n)
    print(fib_while)