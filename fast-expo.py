import time
import random

def naive_exponentiation(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

def fast_exponentiation(base, exp):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result *= base
        base *= base
        exp //= 2
    return result

def compare_methods(base, exp):
    start = time.time()
    naive_result = naive_exponentiation(base, exp)
    naive_time = time.time() - start

    start = time.time()
    fast_result = fast_exponentiation(base, exp)
    fast_time = time.time() - start
    
    assert naive_result == fast_result, "Results do not match!"
    
    print(f"Base: {base}, Exponent: {exp}")
    print(f"Naive Method Time: {naive_time:.6f} seconds")
    print(f"Fast Exponentiation Time: {fast_time:.6f} seconds")
    
    if naive_time > fast_time:
        speedup_factor = naive_time / fast_time if fast_time > 0 else 'Inf'
        print(f"Fast Exponentiation is {speedup_factor}x faster.")
    else:
        speedup_factor = fast_time / naive_time if naive_time > 0 else 'Inf'
        print(f"Naive Exponentiation is {speedup_factor}x faster.")

def main():
    choice = input("Choose input type: (1) Manual (2) Random: ")
    if choice == '1':
        base = int(input("Enter base: "))
        exp = int(input("Enter exponent: "))
    else:
        base = random.randint(2, 10)
        exp = random.randint(10, 1000)
        print(f"Generated Base: {base}, Exponent: {exp}")
    
    compare_methods(base, exp)

if __name__ == "__main__":
    main()
