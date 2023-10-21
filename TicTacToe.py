import sys

# Game Board
gameboard = [" " for _ in range(9)]

# Players
X = "X"
O = "O"

#Winning combinations
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                        (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                        (0, 4, 8), (2, 4, 6)]

#Empty Game Board
empty_gameboard = """
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
"""
print(empty_gameboard)