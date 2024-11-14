import time, os

# Dictionary to store analytics (compatible with Python, JavaScript, Java, C++)
analytics = {}

# Terminal Log Functions
def terminal_n1(n):
    for i in range(n):
        print(f"n1 : print {i + 1}")

def terminal_n2(n):
    count = 1
    for i in range(n):
        for j in range(n):
            print(f"n2 : print {count}")
            count += 1

def terminal_n3(n):
    count = 1
    for a in range(n):
        for b in range(n):
            for c in range(n):
                print(f"n3 : print {count}")
                count += 1

def terminal_n4(n):
    count = 1
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    print(f"n4 : print {count}")
                    count += 1

def terminal_n5(n):
    count = 1
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    for e in range(n):
                        print(f"n5 : print {count}")
                        count += 1


## Variable Increment Functions
def variable_n1(n):
    count = 1
    for i in range(n):
        count += 1
    return count

def variable_n2(n):
    count = 1
    for i in range(n):
        for j in range(n):
            count += 1
    return count

def variable_n3(n):
    count = 1
    for a in range(n):
        for b in range(n):
            for c in range(n):
                count += 1
    return count

def variable_n4(n):
    count = 1
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    count += 1
    return count

def variable_n5(n):
    count = 1
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    for e in range(n):
                        count += 1
    return count

def time_and_run(func, n, iterations, category):
    start_time = time.time() # Start the timer
    
    for i in range(iterations):
        func(n)
    
    end_time = time.time() # End the timer
    total_time = end_time - start_time
    avg_time = total_time / iterations

    # Store analytics in a nested dictionary structure
    if n not in analytics:
        analytics[n] = {'Terminal': {}, 'Variable': {}}

    if category not in analytics[n]:
        analytics[n][category] = {}
    
    os.system('clear') # clear console

    # Store analytics in the appropriate category
    analytics[n][category][func.__name__] = (f"Time taken for {iterations} iterations of {func.__name__} with n={n}: "
                                             f"{total_time:.10f} seconds, Average: {avg_time:.10f} seconds")

# Function to print analytics
def print_analytics():
    for n, categories in analytics.items():
        print(f"\nAnalytics for TEST_N = {n}:")
        for category, funcs in categories.items():
            print(f"  {category}:")
            for func_name, analysis in funcs.items():
                print(f"      {func_name}: {analysis}")



# Test Parameters
ITERATIONS = 50
TERMINAL_TEST_N = [3, 4, 5, 6, 7, 8, 9, 10]
VARIABLE_TEST_N = [10, 20, 30, 40, 50]

# Run tests
for n in TERMINAL_TEST_N:
    # Test Terminal Log Functions
    # time_and_run(terminal_n1, n, ITERATIONS, 'Terminal')
    # time_and_run(terminal_n2, n, ITERATIONS, 'Terminal')
    # time_and_run(terminal_n3, n, ITERATIONS, 'Terminal')
    time_and_run(terminal_n4, n, ITERATIONS, 'Terminal')
    # time_and_run(terminal_n5, n, ITERATIONS, 'Terminal')

for n in VARIABLE_TEST_N:
    # Test Variable Increment Functions
    # time_and_run(variable_n1, n, ITERATIONS, 'Variable')
    # time_and_run(variable_n2, n, ITERATIONS, 'Variable')
    # time_and_run(variable_n3, n, ITERATIONS, 'Variable')
    time_and_run(variable_n4, n, ITERATIONS, 'Variable')
    # time_and_run(variable_n5, n, ITERATIONS, 'Variable')



'''
- 8 different n's for each function, at 100 iternations each
- 10 functions

- 80 pieces of data per language
'''



print_analytics()