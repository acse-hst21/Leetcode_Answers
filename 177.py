import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salaries = list(employee.sort_values(by=['salary'], ascending=False)['salary'].unique())
    try:
        if N < 1:
            n_salary = None
        else:
            n_salary = salaries[N-1]
    except IndexError:
        n_salary = None
    return pd.DataFrame({f'getNthHighestSalary({N})': [n_salary]})
