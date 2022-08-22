def fib(n):
    f1 = f2 = 1
    lst = []
    for i in range(0, n):
        if i <= 1:
            lst.append(i)
        else:
            f1, f2 = f2, f1 + f2
            lst.append(f1)
    print(lst)
    print(len(lst))  # узнаем длину


fib(20)