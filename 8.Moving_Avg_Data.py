

#8
from collections import deque

class MovingAverage:
    def __init__(self, k: int):
        self.k = k
        self.queue = deque()  
        self.sum = 0  

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.sum += val

        
        if len(self.queue) > self.k:
            self.sum -= self.queue.popleft()


        return self.sum / len(self.queue)

# Example usage
ma = MovingAverage(3)
print(ma.next(10)) 
print(ma.next(20))  
print(ma.next(30))  
print(ma.next(40))  