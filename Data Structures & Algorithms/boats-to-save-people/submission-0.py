class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        l = 0
        r = len(people) - 1
        people.sort()
        while l <= r:
            weight = people[l] + people[r]
            if weight > limit:
                r -= 1
            else:
                l += 1
                r -= 1
            count += 1
        return count
        