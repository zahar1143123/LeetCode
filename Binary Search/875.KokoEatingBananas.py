from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        result=0

        while left<=right:
            speed = (left + right) // 2
            time = sum(ceil(p / speed) for p in piles)
                
            if time<=h:
                result=speed
                right = speed - 1
            else:
                left = speed + 1
        return result

