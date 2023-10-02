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

