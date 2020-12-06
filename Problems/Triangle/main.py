n = int(input())
length = n + n - 1
i = 1
char_ = "#"

while i <= n:
    print((char_ * (i + i - 1)).center(length))
    i += 1
