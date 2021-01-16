# 직사각형

for _ in range(4):
    A_left, A_down, A_right, A_up, B_left, B_down, B_right, B_up = map(int, input().split())
    if A_left > B_right or A_right < B_left or A_up < B_down or A_down > B_up:
        print('d')
    elif (A_up == B_down and A_right == B_left) or (A_up == B_down and A_left == B_right) or (A_down == B_up and A_right == B_left) or (A_down == B_up and A_left == B_right):
        print('c')
    elif A_down == B_up:
        if (A_left <= B_left <= A_right or A_left <= B_right <= A_right) or (B_left <= A_left <= B_right or B_left <= A_right <= B_right):
            print('b')
    elif A_left == B_right:
        if (A_down <= B_down <= A_up or A_down <= B_up <= A_up) or (B_down <= A_down <= B_up or B_down <= A_up <= B_up):
            print('b')
    elif A_up == B_down:
        if (A_left <= B_left <= A_right or A_left <= B_right <= A_right) or (B_left <= A_left <= B_right or B_left <= A_right <= B_right):
            print('b')
    elif A_right == B_left:
        if (A_down <= B_down <= A_up or A_down <= B_up <= A_up) or (B_down <= A_down <= B_up or B_down <= A_up <= B_up):
            print('b')
    else:
        print('a')
