class CircularBuffer(object):
    def __init__(self, cap, i_val):
        self.buffer = [i_val] * cap
        self.cap = cap
        self.next_i = 1
        self.cur_i = 0
    
    def AddValue(self, v):
        self.buffer[self.next_i] = v
        self.next_i, self.cur_i = (self.next_i + 1) % self.cap, self.next_i
    
    def GetMax(self):
        return max(self.buffer)
        

def solution(A):
    buf = CircularBuffer(6, A[0])
    for v in A[1:]:
        buf.AddValue(buf.GetMax() + v)
    return buf.buffer[buf.cur_i]
