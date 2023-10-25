def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] >= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_select(arr, low, high, k):
    if low <= high:
        pivot_index = partition(arr, low, high)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index < k:
            return quick_select(arr, pivot_index + 1, high, k)
        else:
            return quick_select(arr, low, pivot_index - 1, k)
    return None

def find_kth_largest(arr, k):
    if k > 0 and k <= len(arr):
        return quick_select(arr, 0, len(arr) - 1, len(arr) - k)
    else:
        return None


sequence = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
k = 3  # Find the 3rd largest number

kth_largest = find_kth_largest(sequence, k)
print(f"The {k}th largest number is: {kth_largest}")
