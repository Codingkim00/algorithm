import sys
input = sys.stdin.readline

student = set()

while True:
    try:
        num = int(input())
        student.add(num)

    except:
        break

for i in range(1, 31):
    if i not in student:
        print(i)
