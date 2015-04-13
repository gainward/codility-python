def solution(H):
    seen_heights = [0]
    num_blocks = 0
    for v in H:
        if v == seen_heights[-1]:
            continue
        elif v > seen_heights[-1]:
            seen_heights.append(v)
        else:
            while seen_heights[-1] > v:
                seen_heights.pop()
                num_blocks += 1
            if seen_heights[-1] == v:
                continue
            else:
                seen_heights.append(v)

    return num_blocks + len(seen_heights) - 1
