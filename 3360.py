class Solution:
    def canAliceWin(self, n: int) -> bool:
        alice_turn = True
        stone_removal = 10
        while True:
            n -= stone_removal
            if n < 0:
                return not alice_turn
            stone_removal -= 1
            alice_turn = not alice_turn
