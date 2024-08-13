import random
def word_generator(characters: str, length: int, amount: int):
    yield from ("".join(random.choices(characters,k=length)) for i in range(amount))