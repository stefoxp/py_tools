import datetime

def days(date_in: str, date_out: str) -> int:
    """
        Return number of days between two dates

        :date_in: 'yyyy-mm-dd'
        :date_out: 'yyyy-mm-dd' is >= date_in

        :return: number of days
    """

    date_in_dt = str_to_date(date_in)
    date_out_dt = str_to_date(date_out)

    return (date_out_dt - date_in_dt).days + 1


def str_to_date(date_in: str) -> datetime.date:
    """
        Convert a string into a date

        :date_in: str in format yyyy-mm-dd

        :return: date
    """
    date_lst = date_in.split('-')

    year = int(date_lst[0])
    month = int(date_lst[1])
    day = int(date_lst[2])

    return datetime.date(year, month, day)
