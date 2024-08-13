def best_results(results: list):
    return [max(x[1], x[2], x[3]) for x in results]