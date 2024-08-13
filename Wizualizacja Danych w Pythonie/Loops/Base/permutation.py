import itertools

def all_permutations(sequence):
    return list(itertools.permutations(sequence))

if __name__ == "__main__":
    print(all_permutations(range(3)))
