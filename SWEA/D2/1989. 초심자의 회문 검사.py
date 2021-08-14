def func(word):
        for i in range(len(word)//2):
            if word[i] != word[len(word)-i-1]:
                return 0
        return 1

for t in range(int(input())):
    w = str(input())
    print(f'#{t+1} {func(w)}')