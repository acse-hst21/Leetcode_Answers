import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    # employees.drop(['out_time', 'in_time'], axis=1, inplace=True)
    res = employees.groupby(['emp_id', 'event_day'])['total_time'].sum().reset_index()
    res.rename(columns={'event_day': 'day'}, inplace=True)
    return res
