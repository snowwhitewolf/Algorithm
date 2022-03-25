lst = list(i for i in range(10001))
result = list(i for i in range(1, 10001))
i = 1
for i in range(10001):
    n = lst[i]
    for j in range(len(str(lst[i]))):
        n += int(str(lst[i])[j])
    if n in result and n < 10001:
        result.remove(n)
for i in range(len(result)):
    print(result[i])
