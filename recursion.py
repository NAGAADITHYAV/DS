import random
def subsetSum(arr, k):
  n = len(arr)

  def backtrack(i, res, current_sum):
    if i == n:
      if current_sum == k:
        print(res)
      return
    # Include current element
    backtrack(i + 1, res + [arr[i]], current_sum + arr[i])
    # Exclude current element
    backtrack(i + 1, res, current_sum)

  backtrack(0, [], 0)

arr = [1,2,1]
k = 2
subsetSum(arr, k)


def anysubSetSum(arr, k):
    n = len(arr)

    def backtrack(i, currsum):
      if currsum == k:
        return True
      if i >= n:
        return False
      if backtrack(i + 1, currsum + arr[i]) or backtrack(i + 1, currsum):
        return True
      return False
        
    return backtrack(0, 0)

arr = [1,2,1]
k = 2
print(anysubSetSum(arr, k))


def Countsubsetswithsum(arr, k):
  #arr given array, k target sum
  n = len(arr)

  def backtrack(i, res, current_sum):
    if i == n:
      if current_sum == k:
        return 1
      return 0
    # Include current element
    left = backtrack(i + 1, res + [arr[i]], current_sum + arr[i])
    # Exclude current element
    right = backtrack(i + 1, res, current_sum)
    return left + right

  return backtrack(0, [], 0)

arr = [1,2,1]
k = 2
print(Countsubsetswithsum(arr, k))


 
def mergeSort(arr):
  if len(arr) <= 1:
    return arr
  mid = len(arr) // 2
  left = mergeSort(arr[:mid])
  right = mergeSort(arr[mid:])
  def merge(left, right):
    arr = []
    i,j=0,0
    n,m = len(left), len(right)
    while(i<n and j< m):
      if left[i] <= right[j]:
        arr.append(left[i])
        i += 1
      else:
        arr.append(right[j])
        j += 1
    while(i<n):
      arr.append(left[i])
      i += 1
    while(j<m):
      arr.append(right[j])
      j += 1
    return arr

  return merge(left, right)

arr = [5,4,3,2]
arr = mergeSort(arr)
print(arr)

def quickSort(arr):
  if len(arr)<= 1:
    return arr
  pivotindex = random.randint(0, len(arr)-1)  

  pivot = [arr[pivotindex]]
  left = []
  right = []
  for x in arr[1:]:
    if x == pivot[0]:
      pivot.append(x)
    elif x < pivot[0]:
      right.append(x)
    else:
      left.append(x)
  return quickSort(left) + pivot + quickSort(right)

arr = [5,4,3,2,12,43,1,0, 5]
arr = quickSort(arr)
print(arr)