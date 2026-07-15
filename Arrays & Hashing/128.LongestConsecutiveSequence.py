class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nms = sorted(list(set(nums)))
        longest_count = 1
        curr_count = 1
        for i in range(len(nms)-1):
            if nms[i]+1==nms[i+1]:
                curr_count+=1
            else:
                longest_count = max(curr_count, longest_count)
                curr_count = 1
        return max(longest_count, curr_count)
