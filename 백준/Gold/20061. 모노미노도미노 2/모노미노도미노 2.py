import sys; input = sys.stdin.readline
from typing import Tuple
from collections import deque


class Matrix:
    def __init__(self) -> None:
        self.score = 0
        self.field = deque([0] * 4 for _ in range(6))
    
    def add_block(self, x: int, width: int, height:int) -> None:
        max_height = 0
        for i in range(x, x+width):
            max_height = max(max_height, self.check_height(i))
        
        for h in range(height):
            for i in range(x, x+width):
                self.field[5-max_height-h][i] = 1

    def fill_row(self) -> None:
        for h in range(6):
            if all(self.field[h]):
                del self.field[h]
                self.field.appendleft([0] * 4)
                self.score += 1
        
    def check_height(self, x: int) -> int:
        for h in range(6):
            if self.field[h][x]:
                return 6 - h
        return 0

    def process_turn(self) -> None:
        self.fill_row()
        max_height = 0
        
        for x in range(4):
            max_height = max(max_height, self.check_height(x))

        if max_height > 4:
            for _ in range(max_height - 4):
                self.field.pop()
                self.field.appendleft([0] * 4)

    def count_blocks(self) -> int:
        return sum(map(sum, self.field))


def get_block_size(block_type: int) -> Tuple[int]:
    if block_type == 1:
        width, height = 1, 1
    elif block_type == 2:
        width, height = 2, 1
    elif block_type == 3:
        width, height = 1, 2
    
    return (width, height)


green_matrix = Matrix()
blue_matrix = Matrix()

n = int(input())
for _ in range(n):
    block_type, y, x = map(int, input().split())
    block_w, block_h = get_block_size(block_type)

    green_matrix.add_block(x, block_w, block_h)
    blue_matrix.add_block(y, block_h, block_w)

    green_matrix.process_turn()
    blue_matrix.process_turn()

print(green_matrix.score + blue_matrix.score)
print(green_matrix.count_blocks() + blue_matrix.count_blocks())