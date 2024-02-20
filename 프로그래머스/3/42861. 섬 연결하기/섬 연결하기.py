"""
MST 단순 구현하기
크루스칼 + 유니온 파인드로 가져간다
작은 숫자를 대표 노드로 만드는 구조.
이거 경로 압축 하는 방법이 있었는데...
"""
def solution(n, costs):
    # 연결 집합의 부모를 찾는다.
    def find_parent(idx):
        while parent[idx] != idx:
            idx = parent[idx]
        return idx
    
    # 집합을 합친다.
    def union(a, b):
        a_p = find_parent(a)
        b_p = find_parent(b)
        
        if a_p > b_p:
            parent[a_p] = b_p
        else:
            parent[b_p] = a_p
    
    # 크루스칼, greedy하게 간선 연결 및 서로소 집합 확인
    costs.sort(key = lambda x: x[2])
    parent = list(range(n))
    
    ret = 0
    for st, ed, cost in costs:
        if find_parent(st) == find_parent(ed):
            continue
        
        union(st, ed)
        ret += cost
    
    return ret