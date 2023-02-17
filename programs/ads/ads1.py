def MergeSortK(n, k):

    if n<=1:
        return 0

    vysl = n

    vacsich = n%k

    nova_velkost = n//k

    vysl+=MergeSortK(nova_velkost, k)*(k - vacsich)

    if vacsich:

        vysl+=MergeSortK(nova_velkost + 1, k)*vacsich

    vysl+=(k-1)*n

    return vysl


n, k = map(int,input().split())

print(MergeSortK(n,k))
