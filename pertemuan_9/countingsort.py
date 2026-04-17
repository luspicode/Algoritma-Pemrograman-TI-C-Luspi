#counting sort
def countingSort(arr):
  max_val = max(arr)
  count = [0] * (max_val + 1)

  while len(arr) > 0:
    num = arr.pop(0)
    count[num] += 1

  for i in range(len(count)):
    while count[i] > 0:
      arr.append(i)
      count[i] -= 1

  return arr

n = int(input('masukkan banyak data : '))
mylist  = []

while n>0:
  sementara = int(input('masukkan elemen : '))
  if sementara < 0:
    print('input harus besar dari 0')
    continue
  n-=1
  mylist.append(sementara)

mysortedlist = countingSort(mylist)
print(mysortedlist)