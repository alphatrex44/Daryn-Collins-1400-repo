def awesome(n):
    if n<=1:
        return n
    return awesome(n-1) + awesome(n-2)
def awesome_with_yield(num_term):
    a, b = 0, 1
    for _ in range(num_term):
        yield a
        a, b = b, a + b
print(awesome(15))
print(list(awesome_with_yield(15)))
