from bisect import bisect_left
from typing import List
import sys

input = sys.stdin.readline


def get_LIS(books: List[int]) -> int:
    result = [0]

    for book in books:
        if result[-1] < book:
            result.append(book)
        else:
            idx = bisect_left(result, book)
            result[idx] = book
    
    return result[1:]


n = int(input())
books = list(map(int, input().split()))

print(n - len(get_LIS(books)))