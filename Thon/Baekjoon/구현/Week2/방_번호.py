### 방 번호
# 고민: 6분
# 코딩: 8분

room = input()

n_dict = {str(i):0 for i in range(9)}
n_dict

for s in room:

    if s == '9':
        n_dict['6'] += 1

    else:
        n_dict[s] += 1

MAX = 0
for k, v in n_dict.items():

    if k == '6':
        val = (v + 1) // 2
    else:
        val = v
    
    MAX = max(MAX, val)

print(MAX)