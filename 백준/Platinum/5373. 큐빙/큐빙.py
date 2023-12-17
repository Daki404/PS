import sys; input = sys.stdin.readline
from typing import List, Tuple, Dict
from collections import deque

U, D = 2, -2
L, R = 1, -1


class CubePlane:
    def __init__(self, init_color: str) -> None:
        self.now_plane = [[init_color] * 3 for _ in range(3)]
        self.up_plane: CubePlane = None
        self.down_plane: CubePlane = None
        self.left_plane: CubePlane = None
        self.right_plane: CubePlane = None
        self.u_idx = self.d_idx = self.l_idx = self.r_idx = None 

        self.cw_stream = (R,L,U,D)
        self.ccw_stream = (L,R,D,U)
    
    def set_planes(self, planes:list['CubePlane']):
        self.up_plane, self.right_plane, self.down_plane, self.left_plane = planes
        self.planes = [self.up_plane, self.right_plane, self.down_plane, self.left_plane]

    def set_idxs(self, idxs: List[Tuple[int]]):
        self.u_idx = idxs[0]
        self.r_idx = idxs[1]
        self.d_idx = idxs[2]
        self.l_idx = idxs[3]
        self.idxs =[self.u_idx, self.r_idx, self.d_idx, self.l_idx]

    def rotate_cube(self, direct: str):
        if direct == 'CW':
            spin_stream = self.cw_stream
            weight = 1
        else:
            spin_stream = self.ccw_stream
            weight = -1
        u_row_stream = self.row_spin(0, spin_stream[0])
        d_row_stream = self.row_spin(2, spin_stream[1])
        l_col_stream = self.col_spin(0, spin_stream[2])
        r_col_stream = self.col_spin(2, spin_stream[3])

        if direct == 'CW':
            self.set_row(0, spin_stream[0], l_col_stream)
            self.set_row(2, spin_stream[1], r_col_stream)
            self.set_col(0, spin_stream[2], d_row_stream)
            self.set_col(2, spin_stream[3], u_row_stream)
        else:
            self.set_row(0, spin_stream[0], r_col_stream)
            self.set_row(2, spin_stream[1], l_col_stream)
            self.set_col(0, spin_stream[2], u_row_stream)
            self.set_col(2, spin_stream[3], d_row_stream)
        
        color_queue = deque()
        for i in range(4):
            row, col, spin = self.idxs[i]
            
            if row is not None:
                color_queue.append(self.planes[i].row_spin(row, spin * weight))
            
            else: # col
                color_queue.append(self.planes[i].col_spin(col, spin * weight))
        
        color_queue.rotate(weight)

        for i in range(4):
            row, col, spin = self.idxs[i]
            
            if row is not None:
                self.planes[i].set_row(row, spin * weight, color_queue[i])
            
            else: # col
                self.planes[i].set_col(col, spin * weight, color_queue[i])
    
    def row_spin(self, idx: int, direct: int) -> List[str]:
        if direct == R:
            return self.now_plane[idx][::-1]
        else: # L
            return self.now_plane[idx]

    def col_spin(self, idx: int, direct: int) -> List[str]:
        stream = []

        if direct == U:
            for i in range(3):
                stream.append(self.now_plane[i][idx])
        else: # D
            for i in range(2, -1, -1):
                stream.append(self.now_plane[i][idx])

        return stream

    def set_row(self, idx: int, direct: int, stream: List[str]) -> None:
        if direct == R:
            stream = stream[::-1]
            
        self.now_plane[idx] = stream

    def set_col(self, idx: int, direct: int, stream: List[str]) -> None:
        if direct == D:
            stream = stream[::-1]
        
        for i in range(3):
            self.now_plane[i][idx] = stream[i]
    
    def print_plane(self):
        for i in self.now_plane:
            print("".join(i))


def init_plane() -> Dict[str, CubePlane]:
    return {
        'u_plane': CubePlane('w'),
        'r_plane': CubePlane('b'),
        'd_plane': CubePlane('y'),
        'l_plane': CubePlane('g'),
        'f_plane': CubePlane('r'),
        'b_plane': CubePlane('o')}

def init_state(planes: Dict[str, CubePlane]):
    u_plane = planes['u_plane']
    r_plane = planes['r_plane']
    d_plane = planes['d_plane']
    l_plane = planes['l_plane']
    f_plane = planes['f_plane']
    b_plane = planes['b_plane']

    # CW 기준으로 방향 설정
    # U R D L 순 입력
    u_plane.set_planes([b_plane, r_plane, f_plane, l_plane])
    u_plane.set_idxs([(0, None, L), (0, None, L), (0, None, L), (0, None, L)])
    r_plane.set_planes([u_plane, b_plane, d_plane, f_plane])
    r_plane.set_idxs([(None, 2, U), (None, 0, D), (None, 0, D), (None, 2, U)])
    d_plane.set_planes([b_plane, l_plane, f_plane, r_plane])
    d_plane.set_idxs([(2, None, R), (2, None, R), (2, None, R), (2, None, R)])
    l_plane.set_planes([u_plane, f_plane, d_plane, b_plane])
    l_plane.set_idxs([(None, 0, D), (None, 0, D), (None, 2, U), (None, 2, U)])
    f_plane.set_planes([u_plane, r_plane, d_plane, l_plane])
    f_plane.set_idxs([(2, None, R), (None, 0, D), (2, None, R), (None, 2, U)])
    b_plane.set_planes([u_plane, l_plane, d_plane, r_plane])
    b_plane.set_idxs([(0, None, L), (None, 0, D), (0, None, L), (None, 2, U)])

    return {
        'U': u_plane,
        'D': d_plane,
        'L': l_plane,
        'R': r_plane,
        'F': f_plane,
        'B': b_plane,
    }


for _ in range(int(input())):
    att = int(input())
    cmds = input().split()
    plane_mapper = init_state(init_plane())

    for cmd in cmds:
        plane, direction = plane_mapper[cmd[0]], cmd[1]
        
        if direction == '+':
            direction = 'CW'
        else:
            direction = 'CCW'
        plane.rotate_cube(direction)

    plane_mapper['U'].print_plane()