# 912 - Sort an Array (medium)

# Sort an array nums in ascending order without using any built in functions with time O(nlog(n)) and the smallest space possible.

# Wouldn't this literally just be implementing any sorting algorithm with O(nlong(n)) from scratch?

# Merge sort has a space complexity of O(n), we could use heap sort to have no space complexity.


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


arr = [12, 11, 13, 5, 6, 7]
print("Given array is:", arr)

mergeSort(arr, 0, len(arr) - 1)
print("Sorted array is:", arr)
