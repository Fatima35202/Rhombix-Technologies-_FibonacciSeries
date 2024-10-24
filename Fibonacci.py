def fibonacci(n):
    """Generate a Fibonacci series of length n."""
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def main():
    try:
        n = int(input("Enter the number of Fibonacci numbers to generate: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            fib_sequence = fibonacci(n)
            print("Fibonacci Series:", fib_sequence)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
  
