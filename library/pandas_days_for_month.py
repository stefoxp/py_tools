# Calculate number of days for each month between two dates
import pandas as pd

def main():
    ass = pd.read_csv("data/assegnazioni.csv", sep=';')

    # print(ass.head())

    # select columns

    # print("ASSE. DATA_ING")
    # date_in = ass["ASSE. DATA_ING"]

    # print(data_in.head())

    # print("ASSE. DATA_UN")
    # date_out = ass["ASSE. DATA_UN"]

    # print(data_out.head())

    df_final = add_days_for_month(ass, 'ASSE. DATA_ING', 'ASSE. DATA_UN')
    df_final.to_csv('data/assegnazioni_calc.csv', sep=';')

    '''
    ass['StartDate'] = pd.to_datetime(date_in)
    ass['EndDate'] = pd.to_datetime(date_out)

    # print("ass:", ass.head())

    df_days = ass[['StartDate', 'EndDate']].apply(days_of_month, axis=1).fillna(0)
    # print('df1:', df1.head())

    # df_final = ass[['NREC', 'StartDate', 'EndDate']].join([ass['StartDate'].dt.year.rename('Year'), df1])
    # df_final = ass[['NREC', 'StartDate', 'EndDate']].join(df_days)
    df_final = ass.join(df_days)

    print(df_final.head())
    '''

def add_days_for_month(df: pd.DataFrame, date_in: str, date_out: str) -> pd.DataFrame:
    df['date_start'] = pd.to_datetime(df[date_in])
    df['date_end'] = pd.to_datetime(df[date_out])

    df_days = df[['date_start', 'date_end']].apply(days_of_month, axis=1).fillna(0)
    df_final = df.join(df_days)

    # debug
    print(df_final.head())

    return df_final


def days_of_month(x) -> pd.Series:
    s = pd.date_range(*x, freq='D').to_series()
    return s.resample('ME').count().rename(lambda x: str(x.year) + fill_string(str(x.month), final_len=2))


def fill_string(str_in: str, final_len: int = 2):
    result = str_in
    missing_chars = final_len - len(str_in)
    
    for mc in range(0, missing_chars):
        result = '0' + result

    return result


if __name__ == '__main__':
    main()
