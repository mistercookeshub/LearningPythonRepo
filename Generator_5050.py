#Generator_5050.py
def first_n(n):
    x = 0
    while x <=n:
        yield x
        x += 1

sum_first_n = sum(first_n(100))
print(sum_first_n)
