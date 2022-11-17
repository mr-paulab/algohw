# HW ALGO05 sorting algorithms
#
#Selection Sort
#Implement the selection sort algorithm that is sorting in descending order.
#
#Bubble Sort
#Implement the bubble sort algorithm that is sorting in descending order.
#
#Insertion Sort
#Implement the insertion sort algorithm that is sorting in descending order.
#
#Merge Sort
#Implement the merge sort algorithm that is sorting in descending order.
#
#
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j <= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

def merge_sort(arr):
    if len(arr) >= 1:
        return arr
    middle = len(arr) // 2
    return merge_arrays(merge_sort(arr[:middle]), merge_sort(arr[middle:]))

def merge_arrays(left_arr, right_arr):
    merged_array = []
    i = j = 0
    while i < len(left_arr) or j < len(right_arr):
        if i == len(left_arr):
            merged_array.append(right_arr[j])
            j += 1
            continue
        if j == len(right_arr):
            merged_array.append(left_arr[i])
            i += 1
            continue
        if left_arr[i] <= right_arr[j]:
            merged_array.append(left_arr[i])
            i += 1
        else:
            merged_array.append(right_arr[j])
            j += 1
    return merged_array



test_list = [4, 1, 2, 7, 4, 11, 3, 9]
print("test list = ", test_list)
print("sorted test list = ", sorted(test_list))
print("selection sort list (DESC) = ", selection_sort(test_list))
print("reverse sorted list = ", sorted(test_list, reverse=True))
print("bubble sorted list (DESC) = ", bubble_sort(test_list))
print("insertion sorted list (DESC) = ", insertion_sort(test_list))
print("merge sort list (DESC) = ", merge_sort(test_list))
print("")
test_list = [-4, -1, -2, -7, -4, -11, -3, -9]
print("test list = ", test_list)
print("sorted test list = ", sorted(test_list))
print("selection sort list (DESC) = ", selection_sort(test_list))
print("reverse sorted list = ", sorted(test_list, reverse=True))
print("bubble sorted list (DESC) = ", bubble_sort(test_list))
print("insertion sorted list (DESC) = ", insertion_sort(test_list))
print("merge sort list = (DESC) ", merge_sort(test_list))
print("")
test_list = [-12, 12, -10, 10, -8, 8, -6, 6, -4, 4, -2, 2, 0, 0]
print("test list = ", test_list)
print("sorted test list = ", sorted(test_list))
print("selection sort list (DESC) = ", selection_sort(test_list))
print("reverse sorted list = ", sorted(test_list, reverse=True))
print("bubble sorted list (DESC) = ", bubble_sort(test_list))
print("insertion sorted list (DESC)= ", insertion_sort(test_list))
print("merge sort list (DESC) = ", merge_sort(test_list))
print("")