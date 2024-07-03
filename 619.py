import pandas as pd
from collections import Counter

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    list_nums = my_numbers['num'].to_numpy()
    counter = Counter(list_nums)
    appears_once = [key for key, value in counter.items() if value == 1]
    if appears_once:
        max_value = max(appears_once)
    else:
        max_value = None
    data = {'num': [max_value]}
    return pd.DataFrame(data)

    # better solution would be return my_numbers.drop_duplicates(keep=False).max().to_frame(name='num')
