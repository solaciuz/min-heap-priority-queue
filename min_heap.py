import heapq
class PriorityQueue:
    def __init__(self): self.q = []
    def push(self, item, p): heapq.heappush(self.q, (p, item))
    def pop(self): return heapq.heappop(self.q)[1]
