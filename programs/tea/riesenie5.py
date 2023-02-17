n = int(input())
s = input()

kmp = [0, 0]
for i in range(1, len(s)):
    state = kmp[i]
    while state != 0 and s[i] != s[state]:
        state = kmp[state]
    if s[i] == s[state]:
        state += 1
    kmp.append(state)

def get_binary(num):
    if num == len(s):
        return [1] * 5
    res = []
    for _ in range(5):
        res.append(num % 2)
        num //= 2
    return res

def get_difference(num1, num2):
    return [1 if num1[i] != num2[i] else 0 for i in range(5)]

def print_move(state, c, diff):
    for i in range(5):
        print(f'{"-" if state[i] == 0 else ""}{i + 1} ', end='')
    print(c, end='')
    for i in range(5):
        if diff[i] == 1:
            print(f' {i + 1}', end='')
    print()

for i in range(len(s)):
    bin_state = get_binary(i)
    for j in range(n):
        c = chr(ord('a') + j)
        state = i
        while state != 0 and s[state] != c:
            state = kmp[state]
        if s[state] == c:
            state += 1
        fin_state = get_binary(state)
        print_move(bin_state, c, get_difference(bin_state, fin_state))
