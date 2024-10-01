#Easy: (3 points)
#1. Given an array of integers, write a function to calculate the sum of all elements in the array.
#Analyze the time complexity of your solution using Big O notation, especially what is the Big O notation 
# of the code you wrote, and include it in the comments of your program.

import time

def sum_of_array(ray):
    start_time = time.time()  # Record the start time
    total = 0
    for num in ray:
        total += num
    end_time = time.time()  # Record the end time

    time_taken = end_time - start_time  # Calculate the time taken
    return total, time_taken

# Example usage
array = [1, 9, 8, 7, 5]
total, time_taken = sum_of_array(array)  # Store the returned values

print(f"Total sum: {total}")
print(f"Time taken: {time_taken:.6f} seconds")  # Print the time taken

# The time complexity of this function is O(n), where n is the number of elements in the array.
# This is because we iterate through each element once.


