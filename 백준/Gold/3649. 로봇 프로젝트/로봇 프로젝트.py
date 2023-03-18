import sys

input = sys.stdin.readline

while True:
    try:
        aim = int(input()) * 10000000
        lego_num = int(input())

        legos = [int(input()) for _ in range(lego_num)]
        legos.sort()


        pt1, pt2 = 0, lego_num - 1
        while pt1 < pt2:
            if (tmp_size := legos[pt1] + legos[pt2]) == aim:
                print(f"yes {legos[pt1]} {legos[pt2]}")
                break
            elif tmp_size < aim:
                pt1 += 1
            else:
                pt2 -= 1
        else:
            print('danger')
    except:
        break