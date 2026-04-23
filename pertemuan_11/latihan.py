data = [78, 90, 65, 97, 882, 360, 21, 9, 1, 36, 67, 99, 420, 510, 443, 38, 505, 123, 404, 45, 5, 300, 250, 220, 15, 5, 33, 256, 10, 20, 44, 421, 234, 42, 32, 37, 80, 0, 54, 14, 71, 19, 121, 96, 126, 84, 155, 110, 18, 76, 166, 2, 6, 51, 31, 59, 98, 55, 99, 280, 303, 16, 25, 321]


# radix sort

rdx = data.copy()
print("Original array:", rdx)
radixArray = [[], [], [], [], [], [], [], [], [], []]
maxVal = max(rdx)
exp = 1

while maxVal // exp > 0:

  while len(rdx) > 0:
    val = rdx.pop()
    radixIndex = (val // exp) % 10
    radixArray[radixIndex].append(val)

  for bucket in radixArray:
    while len(bucket) > 0:
      val = bucket.pop()
      rdx.append(val)

  exp *= 10

print()
print('hasil radix :', rdx)


# merge sort

def mergeSort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  leftHalf = arr[:mid]
  rightHalf = arr[mid:]

  sortedLeft = mergeSort(leftHalf)
  sortedRight = mergeSort(rightHalf)

  return merge(sortedLeft, sortedRight)

def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

mrg = data.copy()
mysortedlist = mergeSort(mrg)
print()
print("hasil merge :", mysortedlist)


# linear search

def linearSearch(arr, targetVal):
  for i in range(len(arr)):
    if arr[i] == targetVal:
      return i
  return -1


target = 11
result = linearSearch(rdx, target)
print()
print('linear  search')

if result != -1:
  print(f"{target} Found at index {result}")
else:
  print("Not found")
  
  
# binary search

def binarySearch(arr, targetVal):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == targetVal:
      return mid

    if arr[mid] < targetVal:
      left = mid + 1
    else:
      right = mid - 1

  return -1

target = 14
result = binarySearch(rdx, target)
print()
print('binary search')

if result != -1:
  print(f"{target} Found at index {result}")
else:
  print("Not found")