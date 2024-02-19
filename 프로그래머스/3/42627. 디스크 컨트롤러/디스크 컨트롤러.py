from heapq import heappop, heappush


def solution(jobs):
    job_cnt = len(jobs)
    jobs.sort(key=lambda x:(x[0], x[1]), reverse=True) 
    ret = -sum(i[0] for i in jobs)
    
    job_idx = 0
    end_work = 0
    
    # 작업 heap이 없어질 때 까지 반복
    while end_work < job_cnt:
        first_job = jobs.pop()
        time = first_job[0]
        work_time_heap = [first_job[1]]
        
        while work_time_heap:
            # 작업 마친 시간 및 누적 시간 합
            time += heappop(work_time_heap)
            end_work += 1
            ret += time

            # 가능한 녀석을 heap에 추가
            while jobs\
                    and jobs[-1][0] < time:
                heappush(work_time_heap, jobs.pop()[1])

    return ret // job_cnt