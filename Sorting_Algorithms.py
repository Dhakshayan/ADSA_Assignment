def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
print("Sorting Algorithms")
arr= list(map(int,input("Enter an Array: ").split(",")))
print("Different Sorting Algorithms are: \n1. Bubble Sort\n2. Selection Sort\n3. Insertion Sort")
choice= int(input("Enter Choice: "))
if choice==1:
    bubble_sort(arr)
    print("Sorted array:", arr)
elif choice==2:
    selection_sort(arr)
    print("Sorted array:", arr)
elif choice==3:
    insertion_sort(arr)
    print("Sorted array:", arr)
else:
    print("Ivalid Choice")
'''
Time Complexity:

Worst-case time complexity: O(n^2) - Occurs when the input array is in reverse order or nearly sorted.
Best-case time complexity: O(n^2) - Occurs when the input array is in sorted order.
Average-case time complexity: O(n^2) - Expected time complexity for random input data.
Stability:

Selection Sort is not stable because it may change the relative order of equal elements.
Performance on Different Input Data:

Selection Sort performs similarly on already sorted and reverse-sorted arrays because it has to make the same number of comparisons and swaps in both cases.
It is not recommended for large datasets due to its quadratic time complexity. It's typically used for small lists or educational purposes.
In terms of performance, it is generally less efficient than more advanced sorting algorithms like Quick Sort or Merge Sort.
Comparison with Quick Sort:

Certainly! Let's compare Selection Sort with Bubble Sort, as you originally asked about Selection Sort.

**Selection Sort vs. Bubble Sort:**

1. **Algorithm Complexity**:
   - Selection Sort has a worst-case, best-case, and average-case time complexity of O(n^2). It makes n-1 comparisons for each of the n elements.
   - Bubble Sort also has a worst-case, best-case, and average-case time complexity of O(n^2). It repeatedly compares and swaps adjacent elements.

2. **Stability**:
   - Selection Sort is not stable because it may change the relative order of equal elements during swapping.
   - Bubble Sort can be stable if you make it so by not swapping elements if they are equal. In its standard form, it is not stable due to swapping adjacent elements.

3. **Adaptive Nature**:
   - Selection Sort is not adaptive. Its performance remains the same, regardless of whether the input data is partially sorted or not.
   - Bubble Sort can be adaptive to some extent. If the input data is nearly sorted, Bubble Sort can be more efficient than its worst-case time complexity.

4. **Number of Swaps**:
   - Selection Sort makes fewer swaps compared to Bubble Sort. It only swaps once per pass to place the minimum element in its correct position.
   - Bubble Sort can make a large number of swaps, especially when large elements "bubble" through the array.

5. **Space Complexity**:
   - Both algorithms have a space complexity of O(1) because they sort the array in place without requiring additional memory for data structures.

6. **Use Cases**:
   - Selection Sort and Bubble Sort are not efficient for large datasets due to their quadratic time complexity. They are typically used for educational purposes or small lists.
   - In practice, other sorting algorithms like Quick Sort, Merge Sort, or Python's built-in sorting functions are preferred for larger datasets because they have better average and worst-case time complexities (e.g., O(n log n)).

7. **Ease of Implementation**:
   - Both Selection Sort and Bubble Sort are relatively easy to implement and understand, making them suitable for teaching and learning sorting algorithms.

8. **Preference**:
   - In general, if you have to choose between Selection Sort and Bubble Sort for small lists or educational purposes, Selection Sort is often preferred because it makes fewer swaps.
'''

