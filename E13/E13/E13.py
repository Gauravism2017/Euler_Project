N = int(input())
sum = 0
for i in range(N):
    num = int(input())
    sum += num
array = []
for s in str(sum):
    array.append(s)
new_li = array[:10]

new_num = ("".join(str(li) for li in new_li))
print(new_num)