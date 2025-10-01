n, w = map(int, input().split())

array = list([list(map(int, input().split())) for _ in range(n)])


d = [0] * (w+1)

for weight, value in array:
    for j in range(w, weight-1, -1):
        d[j] = max(d[j], d[j - weight] + value)
print(d[w])