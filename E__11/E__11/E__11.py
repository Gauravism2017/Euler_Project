
array = []

arr2d = [[j for j in input().split(' ')] for i in range(20)] 
       
for y in range(20):
    for x in range(20):
        if x < 17:
            array.append(int(arr2d[y][x])*int(arr2d[y][x+1])*int(arr2d[y][x+2])*int(arr2d[y][x+3]))
        if y < 17:
            array.append(int(arr2d[y][x])*int(arr2d[y+1][x])*int(arr2d[y+2][x])*int(arr2d[y+3][x]))
        if x >= 3 and y < 17:
            array.append(int(arr2d[y][x])*int(arr2d[y+1][x-1])*int(arr2d[y+2][x-2])*int(arr2d[y+3][x-3]))
        if x < 17 and y < 17:
            array.append(int(arr2d[y][x])*int(arr2d[y+1][x+1])*int(arr2d[y+2][x+2])*int(arr2d[y+3][x+3]))
            
print(max(array))