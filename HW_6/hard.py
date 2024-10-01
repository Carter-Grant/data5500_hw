#Hard: (7 points)
#3. Write a function that takes an array of integers as input and 
# returns the maximum difference between any two numbers in the array.
#Analyze the time complexity of your solution using Big O notation, especially what is the Big O notation 
# of the code you wrote, and include it in the comments of your program.

import time

def max_difference(arr):
    
    start_time = time.time()  # Record the start time
    
    if len(arr) < 2:
        return None, time.time() - start_time  # Not enough elements for a difference

    min_value = min(arr)  # Find the minimum value in the array
    max_value = max(arr)  # Find the maximum value in the array
    max_diff = max_value - min_value  # Calculate the maximum difference
    
    end_time = time.time()  # Record the end time
    time_taken = end_time - start_time  # Calculate the time taken
    
    return max_diff, time_taken

# Time Complexity Analysis:
# The time complexity of this function is O(n), where n is the number of elements in the array.
# This is because we scan through the array twice: once to find the minimum and once to find the maximum.

# Example usage
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9]
max_diff, time_taken = max_difference(array)  # Store the returned values

print(f"Maximum difference: {max_diff}")
print(f"Time taken: {time_taken:.6f} seconds") 
