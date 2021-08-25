def Mergesort(A):
  if len(A) != 1:
    mid = len(A) // 2
    left = [0 for i in range(mid)]
    right = [0 for i in range(mid, len(A) )]
    for i in range(mid):
      left[i]  = A[i]
    for i in range(mid, len(A)):
      right[i-mid] = A[i]
    left = Mergesort(left)
    right = Mergesort(right)
    return Merge(left, right)
  else:
    return A

def Merge(L, R):
  # final array
  A = [0 for i in range(len(L)+len(R))]
  # i is index for L, j is index for R, k is index of new array
  i, j, k = 0,0,0
  # copy the smallest of Li, Rj to the new array, and increment k
  while i < len(L) and j < len(R):
    if L[i] <= R[j]:
      A[k] = L[i]
      i += 1
    else:
      A[k] = R[j]
      j += 1
    k += 1
  # add the rest of the remaining items to the new array
  while i < len(L):
    A[k] = L[i]
    i += 1
    k += 1
  while j < len(R):
    A[k] = R[j]
    j += 1
    k += 1
  return A

print(Mergesort([3,2,4,5,3,1,4,3]))
