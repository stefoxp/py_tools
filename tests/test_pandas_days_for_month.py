from library import pandas_days_for_month
import pandas as pd


def test_replace_char_in_dataframe_columns():
    df_mock = pd.DataFrame(
        {
            'date_start': ['1', '2', '3', ],
            'date_end': ['1', '2', '3', ],
            '202310': [0.0, 1.0, 31.0, ],
        }
    )

    df_result_expected = pd.DataFrame(
        {
            'date_start': ['1', '2', '3', ],
            'date_end': ['1', '2', '3', ],
            '202310': ['0,0', '1,0', '31,0', ],
        }
    )

    df_result = pandas_days_for_month.replace_char_in_dataframe_columns(df_mock, 2, '.', ',')

    assert df_result_expected.equals(df_result)


def test_price_for_month():    
    df_mock = pd.DataFrame(
        {
            'date_start': ['1', '2', '3', ],
            'date_end': ['1', '2', '3', ],
            '202310': [0.0, 1.0, 31.0, ],
        }
    )

    df_result_p = pd.DataFrame(
        {
            'date_start': ['1', '2', '3', ],
            'date_end': ['1', '2', '3', ],
            '202310': [0.0, 1.0, 31.0, ],
            '202310price': [0.0, 8.33, 250.0, ],
        }
    )
    
    s_result = pandas_days_for_month.price_for_month(df_mock, 2)

    assert df_result_p.equals(s_result)


def test_fill_string():
    test_cases = [('1', '01'),
                  ('11', '11')]
    
    for case in test_cases:
        result = pandas_days_for_month.fill_string(case[0], final_len=2)

        assert result == case[1]


def test_add_days_for_month():
    df_mock = pd.DataFrame(
        {
            'ASSE. DATA_ING': [
                '2023-09-18',
                '2023-10-01',
                '2023-11-01',
            ],
            'ASSE. DATA_UN': [
                '2023-09-30',
                '2023-10-31',
                '2023-11-30',
            ],
            'Expected-days': [
                13,
                31,
                30,
            ],
        }
    )

    df_result = pandas_days_for_month.add_days_for_month(df_mock, 'ASSE. DATA_ING', 'ASSE. DATA_UN')

    assert df_result['202309'].iat[0] == df_mock['Expected-days'].iat[0]
    assert df_result['202310'].iat[1] == df_mock['Expected-days'].iat[1]
    assert df_result['202311'].iat[2] == df_mock['Expected-days'].iat[2]
