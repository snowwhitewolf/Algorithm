a = list(range(int(input())+1))

for i in range(1,len(a)):
    if '3' in str(i):
        a[i] = '-'
    elif '6' in str(i):
        a[i] = '-'
    elif '9' in str(i):
        a[i] = '-'
print(a)