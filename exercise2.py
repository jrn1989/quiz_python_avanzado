import time
import math
 

def timing_decorator(func):

    def wrapper(*args, **kwargs):

        start_time = time.time()  # Start time

        result = func(*args, **kwargs)  # Call the original function

        end_time = time.time()  # End time

        execution_time = end_time - start_time
        
        print("Process executed")
        
        with open("execution_times.log", 'a') as file:
            file.write(f"Execution time: {execution_time:.4f} seconds\n")

        return result

    return wrapper