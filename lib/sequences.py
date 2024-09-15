#!/usr/bin/env python3

def print_fibonacci(length):
    
    if length == 0:
        print([])  # Print an empty list when length is 0
        return
    elif length == 1:
        print([0])  # Print only the first Fibonacci number when length is 1
        return
    
    fibonacci_sequence = [0, 1]
    
    # Generate the Fibonacci sequence up to the given length
    for i in range(2, length):
        next_value = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
        fibonacci_sequence.append(next_value)
    
    print(fibonacci_sequence)
