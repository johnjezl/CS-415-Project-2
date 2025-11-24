from abc import ABC, abstractmethod
from collections import deque
import heapq

# Abstract base class for search queues
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

    # function: __init__
    # inputs: none
    # output: none
    # relationships:
    #  initializes an empty FIFO queue using deque
    # pseudocode:
    #   initialize an empty deque
    def __init__(self):
        self.queue = deque()
    
    # function: insert
    # inputs:
    #   vertex: (x, y) tuple representing pixel to insert
    #   priority: not used in FIFOQueue
    # output: none
    # relationships:
    #   adds vertex to the end of the queue
    # pseudocode:
    #   append vertex to the deque
    def insert(self, vertex, priority=None):
        self.queue.append(vertex)
    
    # function: pop
    # inputs: none
    # output:
    #   vertex: (x, y) tuple representing pixel removed from front of queue
    # relationships:
    #   removes and returns the vertex at the front of the queue
    # pseudocode:
    #   remove and return vertex from the front of the deque
    def pop(self):
        return self.queue.popleft()
    
    # function: is_empty
    # inputs: none
    # output:
    #   boolean: True if queue is empty, False otherwise
    # relationships:
    #   checks if the queue is empty
    # pseudocode:
    #   return True if deque is empty, else False
    def is_empty(self):
        return len(self.queue) == 0
    
class PriorityQueue(SearchQueue):
    # function: __init__
    # inputs: none
    # output: none
    # relationships:
    #  initializes an empty priority queue using a heap
    # pseudocode:
    #   initialize an empty list for the heap
    def __init__(self):
        self.queue_heap = []
    
    # function: insert
    # inputs:
    #   vertex: (x, y) tuple representing pixel to insert
    #   priority: not used in FIFOQueue
    # output: none
    # relationships:
    #   adds vertex to the priority queue with given priority
    # pseudocode:
    #   push (priority, vertex) onto the heap
    def insert(self, vertex, priority):
        heapq.heappush(self.queue_heap, (priority, vertex))
    
    # function: pop
    # inputs: none
    # output:
    #   vertex: (x, y) tuple representing pixel removed from front of queue
    # relationships:
    #   removes and returns the vertex with the highest priority (lowest priority value)
    # pseudocode:
    #   remove and return vertex with lowest priority from the heap
    def pop(self):
        return heapq.heappop(self.queue_heap)[1]
    
    # function: is_empty
    # inputs: none
    # output:
    #   boolean: True if queue is empty, False otherwise
    # relationships:
    #   checks if the queue is empty
    # pseudocode:
    #   return True if queue_heap is empty, else False
    def is_empty(self):
        return len(self.queue_heap) == 0
