class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        obj = {}
        arr=[]

        for i in nums:
            if i not in obj:
                obj[i]=1
            else:
                obj[i]+=1
        sort = sorted(obj.items(), key=lambda item: item[1], reverse=True)
        for i in range(k):
            arr.append(sort[i][0])
        return arr