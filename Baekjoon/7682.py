lst = []
while True:
    a = list(input().rstrip())
    if len(a) == 3:
        break
    lst.append(a)
print(lst)