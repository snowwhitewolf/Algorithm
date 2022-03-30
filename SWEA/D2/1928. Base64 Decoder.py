import base64
for t in range(int(input())):
    enc = input()
    result = base64.b64decode(enc)
    total = result.decode('ascii')
    print('#{} {}'.format(t+1, total))
