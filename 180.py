import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    arr = list(logs['num'])
    ConsecutiveNums = [arr[index] for index in range(2, len(arr)) if \
                       arr[index] == arr[index-1] and arr[index] == arr[index-2]]
    return pd.DataFrame({'ConsecutiveNums': list(set(ConsecutiveNums))})
