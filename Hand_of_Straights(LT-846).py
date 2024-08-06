class Solution:
     def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        count = Counter(hand)

        unique_cards = sorted(count)

        for card in unique_cards:
            while count[card] > 0:
                for i in range(groupSize):
                    if count[card + i] > 0:
                        count[card + i] -= 1
                    else:
                        return False
        
        return True
'''        
    def isNStraightHand(self, hand: List[int], GS: int) -> bool:
        n= len(hand)
        if((n %GS )== 0):
            return True
        else:
            return False    
'''            
        