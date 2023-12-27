import sys; input = sys.stdin.readline
from collections import deque


def move_belt():
    belt.rotate(1)
    robot.pop()
    robot.appendleft(False)
    robot[-1] = False

    return False


def move_robot():
    for i in range(belt_len-1, -1, -1):
        if robot[i]\
                and not robot[i+1]\
                and belt[i+1] > 0:
            belt[i+1] -= 1
            robot[i+1] = True
            robot[i] = False
    
    return check_belt() >= dead_belt


def load_robot():
    if belt[0] > 0:
        belt[0] -= 1
        robot[0] = True
    
    return check_belt() >= dead_belt


def check_belt():
    return belt.count(0)


belt_len, dead_belt = map(int, input().split())

belt = deque(list(map(int, input().split())))
robot = deque([False] * belt_len)

turn = 1

while True:
    if move_belt():break
    if move_robot():break
    if load_robot():break
    
    turn += 1

print(turn)