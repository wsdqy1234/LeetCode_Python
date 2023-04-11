a = [5, 9, 1, 2, 10, 4, 3]

# 快速排序法
def quickSort(arr, left, right):    
    if left<right:
        partIdx = partition(arr, left, right)
        quickSort(arr, left, partIdx-1) #左边
        quickSort(arr, partIdx+1, right) #右边
    return arr

def partition(arr, left, right):
    pivot = left #最左边当作基准值
    idx = pivot + 1 
    i = idx
    while i<=right: #把比基准值小的换到idx这里来，到最后[pivot+1 : idx-1]都是比pivot小的数，所以把pivot和idx-1进行交换，则现在[pivot:idx-2]都是比基准值小的数
        if arr[i] < arr[pivot]:
            swap(arr, i, idx)
            idx = idx + 1
        i = i + 1
    swap(arr, pivot, idx-1) #，所以把pivot和idx-1进行交换，则现在[pivot:idx-2]都是比基准值小的数
    return idx-1 #返回pivot所在的位置

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

print(quickSort(a, 0, len(a)-1))