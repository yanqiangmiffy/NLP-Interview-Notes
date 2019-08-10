import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline.strip())
    for i in range(T):
        res = 0

        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        n, m = values[0], values[1]

        line = sys.stdin.readline().strip()
        nums = list(map(int, line.split()))
        for j in range(m):
            line = sys.stdin.readline().strip()
            values = list(map(int, line.split()))
            left, right = values[0], values[1]
            for num in nums:
                if num >= left and num <= right:
                    res += 1
        print(res)
