import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salaries = list(employee['salary'].unique())
    salaries.sort()
    try:
        second_salary = salaries[-2]
    except IndexError:
        second_salary = None
    return pd.DataFrame({'SecondHighestSalary': [second_salary]})
