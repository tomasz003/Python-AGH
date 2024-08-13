def prime_numbers():
    yield 2
    n=3
    while True:
        for i in range(2, int((n**0.5)) + 1):
            if n % i == 0:
                break
        else: yield n
        n+=1
