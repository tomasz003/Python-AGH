def counter(max_value: int):
    number = 0
    while number <= max_value:
        yield number
        number += 1


if __name__ == "__main__":
    numbers = counter(10)
    print("First value:")
    print(next(numbers))
    print("Second value:")
    print(next(numbers))

    print('*' * 10)

    numbers = counter(1)
    print(next(numbers))
    print(next(numbers))
    # StopIteration exception
    # print(next(numbers))

    print('*' * 10)
    # classical use of the generator without exception

    for i in counter(1):
        print(i)
