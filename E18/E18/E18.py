for i in range(int(input())):
    t = []
    dp = []
    
    for i in range(int(input())):
        t.append(list(map(int, input().split())))

    for i in range(len(t)):
        dp.append([])
        
        if i == 0:
            dp[i].append(t[i][0])
            continue

        dp[i].append(dp[i - 1][0] + t[i][0])
        for j in range(1, len(t[i]) - 1):
            dp[i].append(max(dp[i - 1][j], dp[i - 1][j - 1]) + t[i][j])
        dp[i].append(dp[i - 1][-1] + t[i][-1])
        
    print(max(dp[-1]))
