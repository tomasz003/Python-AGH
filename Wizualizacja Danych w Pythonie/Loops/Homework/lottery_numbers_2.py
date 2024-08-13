def hits_in_place(correct_lottery_numbers:list, numbers: list):
    return [x if x in correct_lottery_numbers else -1 for x in numbers]