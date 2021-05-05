from random import sample
def insertionsort(arr):  # Mr Fong's algorithm
  n = len(arr);
  i = 0;
  while i < n-1:
    if arr[i] > arr[i+1]:
      temp = arr[i+1];
      j = i;
      while j >= 0 and arr[j] > temp:
        arr[j+1] = arr[j];
        j -= 1;
      arr[j+1] = temp;
    i += 1;
  return arr;


def bubblesort(arr):  # My algorithm with inspiration from Mr Fong's algorithm
  n = len(arr);
  done = True;  # flag
  passNo = 1; i = 0;
  while done and i < n:  # for the less efficient bubblesort, use a for loop instead
    done = False;
    for j in range(n-passNo):  # inner loop
      if arr[j] > arr[j+1]:
        arr[j],arr[j+1] = arr[j+1],arr[j];
        done = True;
    i+=1;  # For loop increment
  return arr;


def quickSort(arr, first, last):  # Recursive function
  low = first;
  high = last;
  pivot = arr[last];
  while not low > high:
    while arr[low] < pivot:
      low += 1;
    while arr[high] > pivot:
      high -= 1;
    if low <= high:
      arr[low], arr[high] = arr[high], arr[low];
      low += 1; high -= 1;
  if first < high:
    quickSort(arr,first,high);
  if last > low:
    quickSort(arr,low,last);
  return arr;
quicksort = lambda arr: quickSort(arr, 0, len(arr)-1);  # When sorting, first and last are usually not specified; this lambda function specifies them.


# def merge(left, right):
#   c = [None for i in range(len(left) + len(right))]
#   i, j, k = 0,0,0;
#   while i <= len(left) and j <= len(right):
#     if right[j] < left[i]:
#       c[k] = right[j];
#       j+=1
#     else:
#       c[k] = left[i];
#       i+=1
#     k+=1;
#   while i<=len(left):
#
#
# def mergesort(arr, low, high):
#   n = high - low + 1;
#   if low == high:
#     return arr[low];
#   mid = int((high - low)/2);
#   arrL = mergesort(arr, low, mid);
#   arrR = mergesort(arr, mid+1, high);
#   return merge(arrL, arrR);


if __name__ == '__main__':
  unsorted = sample(range(100), k=100)
  print("Sorted by InsertionSort:", insertionsort(unsorted))
  print("Sorted by BubbleSort:", bubblesort(unsorted))
  print("Sorted by QuickSort:", quicksort(unsorted))
