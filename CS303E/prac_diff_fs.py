high = int()
second = int()
ans = int()

for x in range(0,5):
    num = int(input())
    if num > high:
        second = high
        high = num
    elif num < high and num > second:
        second = num

ans = high - second
print(ans)
