import random

r = random.randint(1,100)
print(r)
n = 0
while True:
    X = input('猜猜看數字為何?')
    X = int(X)
    n = n + 1
    if X == r:
        break
    if X <= r:
    	print('要大一點歐!')
    if X >= r:
    	print('要小一點歐!')
    print('你已經猜了',n,'次囉!')
print('恭喜猜對囉!!!')
