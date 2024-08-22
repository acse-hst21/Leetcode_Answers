import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    new_sex = []
    
    for value in salary['sex']:
        if value == 'f':
            new_sex.append('m')
        else:
            new_sex.append('f')
    salary['sex'] = new_sex

    return salary
