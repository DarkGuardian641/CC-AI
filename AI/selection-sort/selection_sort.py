def greedy_selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Greedy choice: Find the minimum element in the unsorted part
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Place the chosen minimum at the current position
        arr[i], arr[min_index] = arr[min_index], arr[i]
        # Uncomment below to see the array after each greedy step
        # print(f"Step {i+1}: {arr}")
    return arr

arr = [64, 25, 12, 22, 11]
sorted_arr = greedy_selection_sort(arr)
print("Sorted array (Greedy Selection Sort):", sorted_arr)