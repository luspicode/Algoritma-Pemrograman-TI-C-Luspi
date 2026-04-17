#quicksort
def partition(array, low, high):
  pivot = array[high]
  i = low - 1

  for j in range(low, high):
     if array[j] <= pivot:
       i += 1
       array[i], array[j] = array[j], array[i]

  array[i+1], array[high] = array[high], array[i+1]
  return i+1

def quicksort(array, low=0, high=None):
  if high is None:
    high = len(array) - 1

  if low < high:
    pivot_index = partition(array, low, high)
    quicksort(array, low, pivot_index-1)
    quicksort(array, pivot_index+1, high)


n = int(input('masukkan banyak data : '))
mylist  = []

while n>0:
  sementara = int(input('masukkan elemen : '))
  if sementara < 0:
    print('input harus besar dari 0')
    continue
  n-=1
  mylist.append(sementara)
  
quicksort(mylist)
print(mylist)