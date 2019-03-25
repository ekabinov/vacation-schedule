# алгоритм сортировки пузырьком
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

assert bubble_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
print(bubble_sort([4, 3, 2, 1]))


# 2
def BubbleSort(A):
    for j in range(len(A) - 1):
        for i in range(len(A) - 1 - j):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
    return(A)


print(BubbleSort([1, 10, 13, -9]))


# 3
li = [5, 2, 7, 4, 0, 9, 8, 6]
n = 1
while n < len(li):
     for i in range(len(li)-n):
          if li[i] > li[i+1]:
               li[i], li[i+1] = li[i+1], li[i]
     n += 1
print(li)


# 4
lst = [5, 2, 7, 4, 0, 9, 8, 6, -100]
k = 0
n = 1
while n < (len(lst)):
    while k < (len(lst)-n):
        if lst[k] > lst[k+1]:
            lst[k], lst[k+1] = lst[k+1], lst[k]
            print(lst)  # чтоб видеть "эволюцию" списка :-)
        k += 1
    k = 0
    n += 1


# 5
a = [1, 0, 9, 5, 3, 8, 4, 6, 2]
print(a)
n = len(a)
m = n-1
while m > 0:
    for i in range(m):
        if (a[i] > a[i+1]):
            x = a[i]
            a[i] = a[i+1]
            a[i+1] = x
        m = m-1
print(a)

# *******************************


# алгоритм сортировки слиянием
def mergeSort(alist):
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i+1
            else:
                alist[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    print("Merging ", alist)

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print(alist)

"""Merge sort."""

# слиянием
def merge(left, right):
    """Merge two lists in ascending order."""
    lst = []
    while left and right:
        if left[0] < right[0]:
            lst.append(left.pop(0))
        else:
            lst.append(right.pop(0))
    if left:
        lst.extend(left)
    if right:
        lst.extend(right)
    return lst


def mergesort(lst):
    """Sort the list by merging O(n * log n)."""
    length = len(lst)
    if length >= 2:
        mid = int(length / 2)
        lst = merge(mergesort(lst[:mid]), mergesort(lst[mid:]))
    return lst

print(''.join(mergesort(list("defgaabcdef"))))

print(''.join(mergesort(list("12348723400023498234"))))

# ********************************


# сортировка перемешиванием
sample = [0, -1, 5, -2, 3]
left = 0
right = len(sample) - 1

while left <= right:
    for i in range(left, right, +1):
        if sample[i] > sample[i + 1]:
            sample[i], sample[i + 1] = sample[i + 1], sample[i]
    right -= 1

    for i in range(right, left, -1):
        if sample[i - 1] > sample[i]:
            sample[i], sample[i - 1] = sample[i - 1], sample[i]
    left += 1

print(sample)


def raschet2():
    days_in_year = 365
    sotr_count = 5
    sotr = []
    days = []

    for i in range(0, sotr_count+1):
        for j in range(0, days_in_year+1):

            days[i][j] = 1
        print(days)

#raschet2()


#a = [[1,2,3], [4,5,6]]
#print(a)


b = []

b.append("00000111")
b.append("11111000")

for i in range(0, 2):
    print(b[i])
