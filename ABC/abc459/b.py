n = int(input())
s_list = input().split()

# 対応表の作成
m = {}
for c in 'abc': m[c] = '2'
for c in 'def': m[c] = '3'
for c in 'ghi': m[c] = '4'
for c in 'jkl': m[c] = '5'
for c in 'mno': m[c] = '6'
for c in 'pqrs': m[c] = '7'
for c in 'tuv': m[c] = '8'
for c in 'wxyz': m[c] = '9'

res = []
for s in s_list:
    # 先頭文字をキーに数字を取得
    res.append(m[s[0]])

# 連結して出力
print("".join(res))
