def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1

    while first <= last:
        mid = (first + last) // 2
        if alist[mid] < item:
            first = mid + 1
        elif alist[mid] > item:
            last = mid - 1
        else: 
            return True
    return False
        
listy = [2, 3, 5, 6, 7, 8, 9, 10, 16, 20, 38, 100, 110001]
print(binarySearch(listy, 8))