class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        num_l = moves.count('L')
        num_r = moves.count('R')
        num_unknown = moves.count('_')

        known_moves = abs(num_l - num_r)
        
        return known_moves + num_unknown
