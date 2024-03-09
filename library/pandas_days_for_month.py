# Calculate number of days for each month between two dates
"""
TODO: tests and library
"""

import pandas as pd

def main():
    ass = pd.read_csv("data/assegnazioni.csv", sep=';')

    print(ass.head())

    # select columns

    print("ASSE. DATA_ING")
    data_in = ass["ASSE. DATA_ING"]

    print(data_in.head())

    print("ASSE. DATA_UN")
    data_out = ass["ASSE. DATA_UN"]

    print(data_out.head())


    ass['StartDate'] = pd.to_datetime(data_in)
    ass['EndDate'] = pd.to_datetime(data_out)

    print("ass:", ass.head())

    df1 = ass[['StartDate', 'EndDate']].apply(days_of_month, axis=1).fillna(0)
    print('df1:', df1.head())

    df_final = ass[['StartDate', 'EndDate']].join([ass['StartDate'].dt.year.rename('Year'), df1])
    print(df_final.head())

def days_of_month(x):
    s = pd.date_range(*x, freq='D').to_series()
    return s.resample('ME').count().rename(lambda x: x.month)

if __name__ == '__main__':
    main()
