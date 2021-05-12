fibo = []
fibo.append(1,1)
for i in range(0,8) :
    number = fibo[i] + fibo[i+1]
    fibo.append(number)
print(fibo)
