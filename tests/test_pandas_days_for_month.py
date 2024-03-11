from library import pandas_days_for_month
import pandas as pd

# def test_days_for_month():
def test_fill_string():
    test_cases = [('1', '01'),
                  ('11', '11')]
    
    for case in test_cases:
        result = pandas_days_for_month.fill_string(case[0], final_len=2)

        assert result == case[1]

def test_add_days_for_month():
    df = pd.DataFrame()

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

    assert df_result['20239'].iat[0] == df_mock['Expected-days'].iat[0]
    assert df_result['202310'].iat[1] == df_mock['Expected-days'].iat[1]
    assert df_result['202311'].iat[2] == df_mock['Expected-days'].iat[2]
