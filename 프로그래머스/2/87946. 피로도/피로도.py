"""
던전 = (최소 필요 피로도, 소모 피로도)
던전을 최대한 많이 돌 때 값 구하기.

최소 필요 피로도가 높은 순서대로 간다?
-> 다 써버리는 곳이면 optimal이 아니다.

소모 피로도가 낮은 순서대로 간다?
-> [1, 1] [1, 1] [100, 2] 이런 경우에 optimal이 아니다.

탐욕 속성을 가지지 못한다.
greedy 하게 풀 수 없고, 완전 탐색을 해야 한다.

여기서 상태 공간의 중복이 발생하는가? 아니다. 순서에 영향이 있으므로 상태공간이 다르다.

순전한 완전 탐색으로 가야한다.
"""
def solution(k, dungeons):
    def dfs(k):
        ret = 0
        
        for i in range(len(dungeons)):
            if visited[i]\
                    or dungeons[i][0] > k:
                continue
            
            visited[i] = True
            ret = max(ret, dfs(k-dungeons[i][1])+1)
            visited[i] = False
        
        return ret
            
            
    visited = [False] * len(dungeons)
    return dfs(k)
    