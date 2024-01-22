import sys
N = int(sys.stdin.readline())
flower = list()
# 100을 곱해 날짜 형식으로 바꿈 (확실히 이 방식이 편하다)
for _ in range(N):
    date = list(map(int, sys.stdin.readline().split()))
    flower.append([date[0] * 100 + date[1], date[2] * 100 + date[3]])
# 오름차순으로 정렬
flower.sort(key=lambda x:(x[0], x[1]))
count = 0
# 꽃이 지는 날짜 저장
end = 0
# 마지막 꽃의 지는 날
target = 301
while flower:
    # 꽃이 지는 날이 12월1일보다 클 경우, 3월 1일 이후에 꽃이 필 경우 break
    if target >= 1201 or target < flower[0][0]:
        break
    for _ in range(len(flower)):
        if target >= flower[0][0]:
            if end <= flower[0][1]:
                end = flower[0][1]
            #확인한 날짜는 없앰
            flower.remove(flower[0])
        # 꽃의 지는 날이 제일 빨리 피는 꽃보다 작으면 break
        else:
            break
    target = end
    count += 1
if target < 1201:
    print(0)
else:
    print(count)