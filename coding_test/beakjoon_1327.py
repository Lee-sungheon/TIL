# 소트게임

# N, K = map(int, input().split())
# sort_list = list(input().split())
# visited = set()
# sort_dict = {''.join(sort_list): 0}
# sort_answer = sorted(sort_list)
# result = -1
# while sort_dict:
#     sample_list = list(sort_dict.keys())[0]
#     cnt = sort_dict.pop(list(sort_dict.keys())[0])
#     # print(sample_list, cnt)
#     if sample_list == ''.join(sort_answer):
#         result = cnt
#         break
    
#     for i in range(N-K+1):
#         tmp_list = list(sample_list)
#         target_list = tmp_list[i:i+K]
#         tmp_list = tmp_list[:i]+target_list[::-1]+tmp_list[i+K:]
#         tmp_str = "".join(tmp_list)
#         if tmp_str not in visited:
#             visited.add(tmp_str)
#             sort_dict.setdefault(tmp_str, cnt+1)

# print(result)


N, K = map(int, input().split())
sort_list = list(input().split())
visited = set()
q = [(''.join(sort_list[:]), 0)]
sort_answer = sorted(sort_list)
result = -1
while q:
    sample_list, cnt = q.pop(0)
    if sample_list == ''.join(sort_answer):
        result = cnt
        break
    
    for i in range(N-K+1):
        target_list = sample_list[i:i+K]
        tmp_list = sample_list[:i]+target_list[::-1]+sample_list[i+K:]
        tmp_str = "".join(tmp_list)
        if tmp_str not in visited:
            visited.add(tmp_str)
            q.append((tmp_str, cnt+1))

print(result)