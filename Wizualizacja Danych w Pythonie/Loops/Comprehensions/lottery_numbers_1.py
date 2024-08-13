def number_of_hits(correct_lottery_numbers:list, numbers: list):
    return len([x for x in numbers if x in correct_lottery_numbers])