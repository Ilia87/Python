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

'''#Посмотри интересное решение при помощи генераторов (они не хранят значение в памяти).
from typing import Generator
def fibonachi_withgenerator(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0: yield 1
    last: int = 0 # начальное значение fibonachi_withgenerator(0)
    next: int = 1 # начальное значение fibonachi_withgenerator(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next
if __name__ == "__main__":
    for i in fibonachi_withgenerator(10000):
        print(i)'''
