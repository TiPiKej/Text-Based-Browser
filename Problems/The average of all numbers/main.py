# put your python code here
a = int(input())
b = int(input())

count = 0
sum_ = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        count += 1
        sum_ += i

print(float(sum_) / count)
