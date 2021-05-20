import heapq
heap=[]
heapq.heappush(heap,10)
heap

heapq.heappush(heap,1)

arr=[1,3,5,2,4,6]

heapq.heapify(arr)

arr

heapq.heappushpop(arr,45)

arr

heapq.heapreplace(arr,89)

arr

heapq.nsmallest(4,arr)

heapq.nlargest(4,arr)

list1=[(1,"Harsha"),(4,"Minat"),(2,"Ria")]

heapq.heapify(list1)
list1

for i in range(len(list1)):
    print(heapq.heappop(list1))

class Solution(object):
    def lastStoneWeight(self, arr):
        arr=[-1*i for i in arr]
        heapq.heapify(arr)
        while len(arr)>1:
                y=-1*heapq.heappop(arr)
                x=-1*heapq.heappop(arr)
                if y-x>0:
                    heapq.heappush(arr,x-y)
        if len(arr)==1:
            return -1*heapq.heappop(arr)
        return 0
