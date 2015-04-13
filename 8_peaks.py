# Poor solution.

def solution(A):
    # Get a list of peak indices.
    l = len(A)
    peaks = []
    for i in xrange(1, l-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            peaks.append(i)
    if not peaks:
        return 0
    
    for num_blocks in xrange(len(peaks), 0, -1):
        if l % num_blocks != 0:
            continue
        b_len = l / num_blocks
        last_peak_i = 0
        
        for block_i in xrange(num_blocks):
            lo = block_i * b_len
            hi = lo + b_len - 1
            found = False
            while last_peak_i < len(peaks) and peaks[last_peak_i] >= lo and peaks[last_peak_i] <= hi:
                found = True
                last_peak_i += 1
            if not found:
                break
        if found:
            return num_blocks
    return 0
