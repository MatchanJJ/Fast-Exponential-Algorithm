import time
import random
import json 

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

def run_simulation(start_exp=0, end_exp=1000000, step=50, base=2):
  
    # temp storages
    exponents = []
    naive_times = []
    fast_times = []
    
    print("\nStarting Simulation...")
    print(f"{'Exponent':<10} {'Naive Time':<15} {'Fast Time':<15} {'Speedup Factor':<15}")
    print("-" * 55)
    
    # JSON
    json_data = {
        "simulation_params": {
            "base": base,
            "start_exponent": start_exp,
            "end_exponent": end_exp,
            "step_size": step,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        },
        "results": []
    }
    
    
    for exp in range(start_exp, end_exp + 1, step):
        # Time for naive method
        start = time.time()
        naive_result = naive_exponentiation(base, exp)
        naive_time = time.time() - start
        
        # Time for fast method
        start = time.time()
        fast_result = fast_exponentiation(base, exp)
        fast_time = time.time() - start
        
        # Speedup calculation 
        speedup = naive_time / fast_time if fast_time > 0 else float('inf')
        
        # Store results to temp storage
        exponents.append(exp)
        naive_times.append(naive_time)
        fast_times.append(fast_time)
        
        # Add to JSON data
        json_data["results"].append({
            "exponent": exp,
            "naive_time": naive_time,
            "fast_time": fast_time,
            "speedup": speedup
        })
        
        # Print results
        print(f"{exp:<10} {naive_time:<15.6f} {fast_time:<15.6f} {speedup:<15.2f}x")
    
    # Saving to a JSON file
    json_filename = f'simulation_results_{time.strftime("%Y%m%d_%H%M%S")}.json'
    with open(json_filename, 'w') as f:
        json.dump(json_data, f, indent=4)
    
    # Saving results to a text file
    with open('simulation_results.txt', 'w') as f:
        f.write("Simulation Results\n")
        f.write(f"Base number: {base}\n")
        f.write("=" * 55 + "\n")
        f.write(f"{'Exponent':<10} {'Naive Time':<15} {'Fast Time':<15} {'Speedup Factor':<15}\n")
        f.write("-" * 55 + "\n")
        
        for i in range(len(exponents)):
            speedup = naive_times[i] / fast_times[i] if fast_times[i] > 0 else float('inf')
            f.write(f"{exponents[i]:<10} {naive_times[i]:<15.6f} {fast_times[i]:<15.6f} {speedup:<15.2f}x\n")

def main():
    choice = input("Choose operation: (1) Manual (2) Random (3) Run Simulation: ")
    if choice == '1':
        base = int(input("Enter base: "))
        exp = int(input("Enter exponent: "))
        compare_methods(base, exp)
    elif choice == '2':
        base = random.randint(2, 10)
        exp = random.randint(10, 1000)
        print(f"Generated Base: {base}, Exponent: {exp}")
        compare_methods(base, exp)
    else:
        base = int(input("Enter base (default=2): ") or "2")
        start = int(input("Enter start exponent (default=0): ") or "0")
        end = int(input("Enter end exponent (default=1000000): ") or "1000000")
        step = int(input("Enter step size (default=100): ") or "100")
        run_simulation(start, end, step, base)

if __name__ == "__main__":
    main()