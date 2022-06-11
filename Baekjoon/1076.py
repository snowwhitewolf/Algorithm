lst = {
    'black' : 0,
    'brown' : 1,
    'red' : 2,
    'orange' : 3,
    'yellow' : 4,
    'green' : 5,
    'blue' : 6,
    'violet' : 7,
    'grey' : 8,
    'white' : 9,
}

lst3 = []
for _ in range(3):
    lst3.append(input())
res = ''
for i in range(3):
    if i == 2:
        if lst3[i] == 'black':
            break
        else:
            res += '0'*lst[lst3[i]]
    else:
        res += str(lst[lst3[i]])
if res[0] == '0':
    print(res[1:])
else:
    print(res)