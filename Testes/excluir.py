s = "IV"
m = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

ans = 0
tamanho = len(s)

for num in range(tamanho):
    if num + 1 < tamanho and m[s[num]] < m[s[num+1]]:
        ans -= m[s[num]]
    else:
        ans += m[s[num]]

print(ans)