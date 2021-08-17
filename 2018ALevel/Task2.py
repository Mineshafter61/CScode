def QuickSort(Scores):
  QuickSortHelper(Scores, 0, len(Scores)-1)
  return Scores

def QuickSortHelper(Scores, First, Last):
  if First < Last:
    SplitPoint = Partition(Scores, First, Last)
    QuickSortHelper(Scores, First, SplitPoint-1)
    QuickSortHelper(Scores, SplitPoint+1, Last)

  return Scores

def Partition(Scores, First, Last):
  PivotValue = Scores[First]
  LeftMark = First + 1
  RightMark = Last
  Done = False
  while Done == False:
    while LeftMark <= RightMark and Scores[LeftMark] <= PivotValue:
      LeftMark += 1
    while Scores[RightMark] >= PivotValue and RightMark >= LeftMark:
      RightMark -= 1
    if RightMark < LeftMark:
      Done = True
    else:
      Temp = Scores[LeftMark]
      Scores[LeftMark] = Scores[RightMark]
      Scores[RightMark] = Temp

  Scores[First], Scores[RightMark] = Scores[RightMark], Scores[First] # swap

  return RightMark

Scores = []
print(Scores)
Scores = QuickSort(Scores)
print(Scores)
