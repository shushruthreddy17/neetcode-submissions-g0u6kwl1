class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = defaultdict(int)

        for h in hand:
            count[h] += 1
        
        for card in sorted(count):
            while count[card] > 0:
                for i in range(card, card + groupSize):
                    if count[i] == 0:
                        return False
                    count[i] -= 1
        return True