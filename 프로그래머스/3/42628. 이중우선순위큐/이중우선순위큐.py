from heapq import heappop, heappush


def solution(operations):
    def sync_heappop(heap):
        while heap\
                and heap[0][1] in del_idxes:
            heappop(heap)
        # 뽑아서 return, 없으면 0
        val = 0
        if heap:
            val, idx = heappop(heap)
            del_idxes.append(idx)
        
        return val
    
    max_heap = []
    min_heap = []
    # 동기화를 위한 삭제 노드 고유인덱스
    del_idxes = []
    
    for idx, oper in enumerate(operations):
        cmd, val = oper.split()
        # 삽입
        if cmd == 'I':
            heappush(max_heap, (-int(val), idx))
            heappush(min_heap, (int(val), idx))
        # 추출
        else:
            # 최대힙 추출
            if int(val) == 1:
                sync_heappop(max_heap)
            # 최소힙 추출    
            else:
                sync_heappop(min_heap)
    
    return [-sync_heappop(max_heap), sync_heappop(min_heap)]
    
          