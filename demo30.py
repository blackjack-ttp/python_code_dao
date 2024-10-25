"""
Thuật toán tìm kiếm nhị phân: Viết hàm thực hiện thuật toán tìm kiếm nhị phân trên một mảng đã sắp xếp.
"""

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1

arr = sorted([int(x) for x in input("Nhập các số, cách nhau bằng khoảng trắng: ").split()])
target = int(input("Nhập số cần tìm: "))
result = binary_search(arr, target)
print("Số", target, "tìm thấy tại chỉ số" if result != -1 else "không có trong mảng", result)
