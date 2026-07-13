class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1]*len(nums)

        prefix = 1
        for idx, num in enumerate(nums):
            arr[idx]=prefix
            prefix*=num
        
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            arr[i]*=postfix
            postfix*=nums[i]

        return arr