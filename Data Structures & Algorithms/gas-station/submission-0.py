class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        cur = 0
        start = 0
        for i, g in enumerate(gas):
            cur += g
            cur -= cost[i]
            if cur < 0:
                cur = 0
                start = i + 1
        return start