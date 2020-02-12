def average(array):
  setFromMap= set(array)
  sum=0
  for i in setFromMap:
    sum=sum+i
  result=sum/len(setFromMap)
  return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)