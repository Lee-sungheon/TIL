def solution(code, day, data):
    result = []
    answer = []
    for da in data:
        tmp_data = da.split(" ")
        if tmp_data[1].split("=")[1] == code:
            if tmp_data[2].split("=")[1][:8] == day:
                result.append([tmp_data[2].split("=")[1], tmp_data[0].split("=")[1]])
    result.sort();
    for data in result:
        answer.append(int(data[1]))
    return answer

solution("012345", "20190620", ["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014","price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"])