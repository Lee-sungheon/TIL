def findRange(num):
    # Write your code here
    num = str(num)
    min_value = '1'
    for i in range(len(num)):
        if num[i] != '1':
            min_value = num[i]
            break
    max_value = '9'
    for i in range(len(num)):
        if num[i] != '9':
            max_value = num[i]
            break
    max_num = num.replace(max_value, '9')
    if num[0] == min_value:
        min_num = num.replace(min_value, '1')
    else:
        min_num = num.replace(min_value, '0')
    result = int(max_num) - int(min_num)
    return result

if __name__ == '__main__':
    num = int(input().strip())

    result = findRange(num)
    print(result)
