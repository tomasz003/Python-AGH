def begin_with_vowel(words: list):
    return [x for x in words if x[0].lower() in ['a','e','i','o','u']]