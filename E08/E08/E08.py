time_iteration = int(input())
if time_iteration >= 1 and time_iteration <= 100:
    for i in range(time_iteration):
        N, K = map(int, input().split())
        if K >= 1 and K <= 7 and N >= K and N <= 1000:
            num = input()
            lis = [int(i) for i in str(num)]
            array = []
            for j in range(N- K + 1):
                mult = 1
                for l in range(K):
                    mult = mult * lis[j +l]
                array.append(mult)
            array = sorted(array)
            print(array[-1])
        else:
            continue

else:
    quit

