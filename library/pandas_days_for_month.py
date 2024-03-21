import pandas as pd


def main():
    FILE_IN = 'data/assegnazioni.csv'
    FILE_OUT = 'data/assegnazioni_calc.csv'
    # TODO calculate index from DataFrame
    START_COLUMN_INDEX = 48

    print("Debug - Elaborazione dei dati contenuti su:", FILE_IN,  "iniziata")

    ass = pd.read_csv(FILE_IN, sep=';')

    df_final = add_days_for_month(ass, 'ASSE. DATA_ING', 'ASSE. DATA_UN')

    df_final = price_for_month(df_final, START_COLUMN_INDEX)
    df_final = replace_char_in_dataframe_columns(df_final, START_COLUMN_INDEX, '.', ',')

    df_final.to_csv(FILE_OUT, sep=';')

    print("Debug - Elaborazione terminata. I risultati sono disponibili nel file:", FILE_OUT)


def add_days_for_month(df: pd.DataFrame, date_in: str, date_out: str) -> pd.DataFrame:
    """
        Add columns with number of days for each month between dates columns

        :df: original DataFrame
        :date_in: name of date_in column
        :date_out: name of dat_out column

        :return: Dataframe modified
    """
    
    df['date_start'] = pd.to_datetime(df[date_in])
    df['date_end'] = pd.to_datetime(df[date_out])

    df_days = df[['date_start', 'date_end']].apply(days_of_month, axis=1).fillna(0)
    df_final = df.join(df_days)

    return df_final


def days_of_month(x) -> pd.Series:
    """
        Calculate number of days for each month between dates columns

        :x:

        :return: Series
    """

    s = pd.date_range(*x, freq='D').to_series()
    return s.resample('ME').count().rename(lambda x: str(x.year) + fill_string(str(x.month), final_len=2))


def fill_string(str_in: str, final_len: int = 2):
    result = str_in
    missing_chars = final_len - len(str_in)
    
    for mc in range(0, missing_chars):
        result = '0' + result

    return result


def price_for_month(df_in: pd.DataFrame, from_column: int) -> pd.DataFrame:
    """
        Calculate price for each month

        :df_in:         Dataframe
        :from_column:   start column index

        :return:        Dataframe with new price columns
    """
    MONTH_DAYS_STANDARD: float = 30.00
    MONTH_PRICE: float = 250.00
    DAY_PRICE: float = MONTH_PRICE / MONTH_DAYS_STANDARD

    for col in df_in.iloc[:, from_column:].columns:
        new_col_name = col + 'price'
        df_in[new_col_name] = round(pd.to_numeric(df_in[col]) * DAY_PRICE, 2)
        df_in[new_col_name] = df_in[new_col_name].apply(lambda price: MONTH_PRICE if price > MONTH_PRICE else price)
    
    return df_in.iloc[:, :]


def replace_char_in_dataframe_columns(df_in: pd.DataFrame, from_column: int, char_old: str, char_new: str) -> pd.DataFrame:
    """
        Replace char in dataframe columns

        :df_in:         original Dataframe
        :from_column:   start column index
        :char_old:      char to replace
        :char_new:      new char 

        :return:        Dataframe with updated columns
    """
    for col in df_in.iloc[:, from_column:].columns:
        df_in[col] = df_in[col].apply(lambda value: str(value).replace(char_old, char_new))

    return df_in


if __name__ == '__main__':
    main()
