class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets, lasttime = 0, 0
        for pos, spd in cars:
            arr = (target - pos) / spd
            if arr > lasttime:
                fleets += 1
                lasttime = arr
        return fleets