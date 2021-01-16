# 줄 세우기

N = int(input())
num_list = list(map(int, input().split()))
students = []
for i in range(N):
    students.insert(len(students) - num_list[i], i+1)
print(*students)