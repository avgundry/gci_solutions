from typing import Collection

def cut_rod(p, n):
    if n == 0:
        return 0
    q = float('-inf')

    for i in range(1, n + 1):
        q = max(q, p[i - 1] + cut_rod(p, n - i))

    return q

if __name__ == "__main__":
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 30, 31, 33, 45, 48, 49, 50, 51, 55, 58, 60, 67, 69, 70, 71]
    for i in range(len(p) + 1):
        print(cut_rod(p, i))