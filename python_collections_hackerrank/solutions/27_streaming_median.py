import heapq

def streaming_median(nums):
    low, high, out = [], [], []  # low is max-heap using negatives
    for x in nums:
        if not low or x <= -low[0]:
            heapq.heappush(low, -x)
        else:
            heapq.heappush(high, x)
        if len(low) > len(high) + 1:
            heapq.heappush(high, -heapq.heappop(low))
        elif len(high) > len(low):
            heapq.heappush(low, -heapq.heappop(high))
        if len(low) == len(high):
            out.append((-low[0] + high[0]) / 2)
        else:
            out.append(float(-low[0]))
    return out

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(*streaming_median(nums))
