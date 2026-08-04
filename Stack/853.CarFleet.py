class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        cars.sort(reverse=True)

        fleets=0
        slowestCarTime = 0
        
        for start, speed in cars:
            currCarTime = (target-start)/speed
            if slowestCarTime < currCarTime:
                fleets+=1
                slowestCarTime = currCarTime
        
        return fleets
