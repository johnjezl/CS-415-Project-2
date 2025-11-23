from abc import ABC, abstractmethod
from collections import deque
import heapq

class SearchQueue(ABC):
    @abstractmethod
    def insert(self, vertex, priority=None):
        pass
    
    @abstractmethod
    def pop(self):
        pass
    
    @abstractmethod
    def is_empty(self):
        pass

class FIFOQueue(SearchQueue):
    def __init__(self):
        self.queue = deque()
    
    def insert(self, vertex, priority=None):
        self.queue.append(vertex)
    
    def pop(self):
        return self.queue.popleft()
    
    def is_empty(self):
        return len(self.queue) == 0
    
class PriorityQueue(SearchQueue):
    def __init__(self):
        self.queue_heap = []
    
    def insert(self, vertex, priority):
        heapq.heappush(self.queue_heap, (priority, vertex))
    
    def pop(self):
        return heapq.heappop(self.queue_heap)[1]
    
    def is_empty(self):
        return len(self.queue_heap) == 0
