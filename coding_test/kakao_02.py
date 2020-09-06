# 파일명 정렬
def solution(files):
    answer, result = [], []
    N = len(files)
    head, number = ['']*N, ['']*N
    for i in range(len(files)):
        for j in range(len(files[i])):
            if len(number[i]) != 0 and '0' > files[i][j] or files[i][j] > '9':
                break
            # elif len(number[i]) == 5:
            #     break
            elif '0' <= files[i][j] <= '9':
                number[i] += files[i][j]
            elif '0' > files[i][j] or files[i][j] > '9':
                head[i] += files[i][j].upper()
        number[i] = int(number[i])
        result.append((head[i], number[i], i))
        result.sort()
    for i in range(N):
        answer.append(files[result[i][2]])
    return answer


# print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# print(solution(["IMG123456.jpg", "img12345 2.png", "img55555555.jpg"]))
# print(solution(["--F15.jpg", "F14.png", "F016.jpg"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))