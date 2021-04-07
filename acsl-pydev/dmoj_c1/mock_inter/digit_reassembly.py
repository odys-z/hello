
inp = ['834127903876541 3', '2424424442442420 1']

for i in range(len(inp)):
    pn = inp[i].split()
    p, n = pn[0], int(pn[1])
    reslt = 0
    for j in range(len(p) - n + 1):
        reslt += int(p[j:j+n])
    print('{}. {}'.format(i, reslt))
        
