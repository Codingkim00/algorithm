import sys
sys.setrecursionlimit(10**6)

pre = []

while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    pre.append(int(line))

def post(start, end):

    if start > end:
        return

    root = pre[start]
    mid = start + 1

    while mid <= end and pre[mid] < root:
        mid += 1

    post(start+1, mid-1)
    post(mid, end)
    print(root)

post(0, len(pre)-1)