from library import tools


def csv_to_list(file_in):
    """
    Read file_in.
    Return the list of records

    :return: list province
    """
    list_rows = []

    try:
        with open(file_in) as f:
            list_rows = f.read().splitlines()
    except OSError as Error:
        str_msg = 'Error on csv_to_list(): ' + str(Error) + '\n'
        
        print(str_msg)

    return list_rows


def csv_up(file_in, lst_search):
    """
    Replace each value in list with UPPERCASE

    :return:
    """
    list_rows = []
    try:
        with open(file_in) as f:
            list_rows = f.read().splitlines()
    except OSError as Error:
        str_msg = 'Error on csv_up(): ' + str(Error) + '\n'
        
        print(str_msg)

    for row in list_rows:
        for val in lst_search:
            low = val.lower()
            row = row[0:3].replace(low, val) + row[3:]

        row = row.replace(';', '";"')
        row = row.replace('"NULL"', 'NULL')
        row = row.replace('"NULL', 'NULL')
        row = '"' + row
        print(row)


def csv_to_option(file_in):
    """
    Read file_in.
    Return the list of records like < option id = "AN" / >

    :return: list province
    """
    list_rows = []
    list_options = []

    try:
        with open(file_in) as f:
            list_rows = f.read().splitlines()
    except OSError as Error:
        str_msg = 'Error on csv_to_option(): ' + str(Error) + '\n'

        print(str_msg)

    for row in list_rows:
        list_options.append('<option id="' + row + '"/>')

    return list_options


def csv_to_language(file_in):
    """
    Read file_in.
    Return the list of records like SP.PROVINCE.<sigla>="<label=sigla>"

    :return: list province
    """
    list_rows = []
    list_options = []

    try:
        with open(file_in) as f:
            list_rows = f.read().splitlines()
    except OSError as Error:
        str_msg = 'Error on csv_to_language(): ' + str(Error) + '\n'
        
        print(str_msg)

    for row in list_rows:
        list_options.append('SP.PROVINCE.' + row.upper() + '="' + row + '"')

    return list_options


def list_to_file_insert(list_in, file_out, field_sep=';'):
    """
    Read list_in.
    Return file_out

    :return: list
    """
    # INSERT INTO ERSURB.dbo.MENSA_PIATTI
    # (Tipo, Codice, Descrizione, Riferimento, EscludiPrenotazione, Surgelato, Con_Surgelato, Suino, Vegetariano, Biologico, Grammi60, Pane, Dolce, Unico, PU_Comprende_Contorno, PU_Comprende_Frutta, PU_Comprende_Bevanda, PU_Comprende_Pane, CI_Dolce, CI_Salato, Extra, Flg_Obsoleta)
    # VALUES(N'10', N'E00001', N'SPAGHETTI ALLA LACRIMA + 1-9', N'RIF', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);

    # INSERT INTO ERSURB.dbo.MENSA_MENU
    # (Codice, Descrizione, Riferimento, Vegetariano, Biologico, SmartClient, NomePannello, Flg_Obsoleta, Flg_Standard)
    # VALUES(N'ES1LU_P', N' Estivo_Settimana1_Lun_Pranzo', N'RIF', 0, 0, 0, N'', 0, 1);
  
    # INSERT INTO ERSURB.dbo.MENSA_MENU_DETT
    # (Menu, Tipo, Posizione, Piatto)
    # VALUES('', '', 0, '');

    tools.print_obj('', 'w', file_out)

    for row in list_in:
        row = row.replace("'", "")
        record = row.split(field_sep)
        tools.print_obj("INSERT INTO ERSURB.dbo.MENSA_MENU_DETT VALUES('"
                        + record[0] + "', '" + record[1] + "', " + record[2] + ", '" + record[3] + "');",
                        'a',
                        file_out)

    tools.print_obj('file ' + file_out + ' created')


if __name__ == '__main__':
    '''
    plates_in = 'data/plates.csv'
    plates_out = 'data/plates.sql'
   
    plates = csv_to_list(plates_in)
    list_to_file_insert(plates_lst, plates_out)
   
    menu_in = 'data/menu.csv'
    menu_out = 'data/menu.sql'
   
    plates = csv_to_list(menu_in)
    list_to_file_insert(plates_lst, menu_out)
    '''
    menu_in = 'data/side_dish.csv'
    menu_out = 'data/side_dish.sql'
   
    plates = csv_to_list(menu_in)
    list_to_file_insert(plates, menu_out)
    



