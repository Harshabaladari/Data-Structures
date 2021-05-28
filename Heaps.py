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

# Leetode-1046
"""
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
 
"""
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
