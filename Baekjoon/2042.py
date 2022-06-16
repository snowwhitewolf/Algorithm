N, M, K = map(int,input().split())
tree = [0] * 4000000
lst = [0]
res = []
def func(node,s,e):
    if s == e:
        tree[node] = lst[s]
        return lst[s]
    else:
        tree[node] = func(node*2,s,(s+e)//2) + func(node*2+1,(s+e)//2+1,e)
        return tree[node]

def changing(node, s, e, index, change):
        if s <= index <= e:
            tree[node] += change
            if s != e:
                changing(node*2,s,(s+e)//2,index,change)
                changing(node * 2+1, (s + e) // 2+1, e, index, change)


def ssum(node,s,e,l,r):
    if l > e or s > r:
        return 0
    if l <= s and e <= r:
        return tree[node]

    return ssum(node * 2, s, (s+e)//2, l, r) + ssum(node * 2 + 1, (s + e) // 2 + 1, e, l, r)

for _ in range(N):
    lst.append(int(input()))
func(1,1,N)
for _ in range(M+K):
    a,b,c = map(int,input().split())
    if a == 1:
        change = c - lst[b]
        changing(1,1,N,b,change)
    else:
        print(ssum(1,1,N,b,c))