def average(array):
    # your code goes here
  set1=set(array)  
  res=sum(set1)/len(set1)
  return res

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
