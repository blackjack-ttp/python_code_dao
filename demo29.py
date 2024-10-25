"""
Sắp xếp nhanh (Quick Sort): Viết hàm thực hiện thuật toán sắp xếp nhanh.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = [int(x) for x in input("Nhập các số, cách nhau bằng khoảng trắng: ").split()]
print("Mảng đã sắp xếp:", quick_sort(arr))
