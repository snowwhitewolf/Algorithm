for t in range(int(input())):
    word = str(input())
    for i in 'aeiou':
        word = word.replace(i,'')
    print(f'#{t+1} {word}')