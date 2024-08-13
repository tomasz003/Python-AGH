def pairwise_combinations(seq1, seq2):
    yield from [(i,j) for i in seq1 for j in seq2]