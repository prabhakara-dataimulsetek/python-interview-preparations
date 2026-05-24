from collections import Counter

def top_claim_codes(codes, n):
    counts = Counter(codes)
    return sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:n]

if __name__ == "__main__":
    codes = input().split()
    n = int(input())
    for code, cnt in top_claim_codes(codes, n):
        print(code, cnt)
