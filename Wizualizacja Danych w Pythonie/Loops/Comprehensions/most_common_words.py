def most_common_words(text: str, lower_limit: int):
    list = text.split(' ')
    return {x: list.count(x) for x in list if list.count(x)>=lower_limit}