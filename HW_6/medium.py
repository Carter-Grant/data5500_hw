#Medium: (5 points)
#2. Given an array of integers, write a function that finds the second largest number in the array.
#Analyze the time complexity of your solution using Big O notation, especially what is the Big O notation 
# of the code you wrote, and include it in the comments of your program.

import time

def second_largest(lst):
    start_time = time.time()  # Record the start time
    
    if len(lst) < 2:
        return None, time.time() - start_time  # Not enough elements for a second largest

    for j in range(len(lst) - 1):
        for i in range(len(lst) - 1 - j):  # Optimize to reduce comparisons
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]

    second_largest_num = lst[-2]  # Second largest will be the second last element in a sorted list
    end_time = time.time()  # Record the end time
    time_taken = end_time - start_time  # Calculate the time taken
    
    return second_largest_num, time_taken

# Time Complexity Analysis:
# The time complexity of this function is O(n^2) due to the bubble sort implementation.

# Example usage
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9]
second_largest_num, time_taken = second_largest(lst)  # Store the returned values

print(f"Second largest number: {second_largest_num}")
print(f"Time taken: {time_taken:.6f} seconds")  
