from library import tools, files


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

    '''
    INSERT INTO [Erdis_Read].[dbo].[in4_consumazioni](
        [DATA_REG_EBADGE]
           ,[DATA_REG_CASSA]
           ,[PRESIDIO]
           ,[IDANA]
           ,[UTENTE_ID]
           ,[COGNOME]
           ,[NOME]
           ,[IDCON]
           ,[CONSUMAZIONE_ID]
           ,[STATUS]
           ,[TESSERA_ID]
           ,[IDENTIFICAZIONE_ID]
           ,[TIPO_PAGAMENTO_ID]
           ,[OPERATORE_USER]
           ,[TURNO_ID]
           ,[RISTORANTE_PRESIDIO]
           ,[RISTORANTE]
           ,[CASSA]
           ,[ACQUISTO]
           ,[TIPO_LISTINO_ID]
           ,[PREZZO_TOTALE]
           ,[COSTO_TOTALE]
           ,[VALORE_PASTO]
           ,[OFFLINE]
           ,[PRENOTAZIONE]
           ,[BRUCIATURA_DATA]
           ,[BRUCIATURA_CASSA_ID]
           ,[BRUCIATURA_CASSA]
           ,[PRA_ANNO_ACCADEMICO]
           ,[PRA_PROFILO_ID]
           ,[PRA_PROFILO]
           ,[PRA_CATEGORIA_ID]
           ,[PRA_CATEGORIA]
           ,[PRA_RICAVO_MENSA]
           ,[PRA_MODALITA_ID]
           ,[PRA_MODALITA]
           ,[PRA_TIPO_LISTINO_ID]
           ,[PRA_TIPO_LISTINO])
     VALUES
           (<DATA_REG_EBADGE, varchar(50),>
           ,<DATA_REG_CASSA, varchar(50),>
           ,<PRESIDIO, varchar(50),>
           ,<IDANA, varchar(50),>
           ,<UTENTE_ID, varchar(50),>
           ,<COGNOME, varchar(50),>
           ,<NOME, varchar(50),>
           ,<IDCON, varchar(50),>
           ,<CONSUMAZIONE_ID, varchar(50),>
           ,<STATUS, varchar(50),>
           ,<TESSERA_ID, varchar(50),>
           ,<IDENTIFICAZIONE_ID, varchar(50),>
           ,<TIPO_PAGAMENTO_ID, varchar(50),>
           ,<OPERATORE_USER, varchar(50),>
           ,<TURNO_ID, varchar(50),>
           ,<RISTORANTE_PRESIDIO, varchar(50),>
           ,<RISTORANTE, varchar(50),>
           ,<CASSA, varchar(50),>
           ,<ACQUISTO, varchar(50),>
           ,<TIPO_LISTINO_ID, varchar(50),>
           ,<PREZZO_TOTALE, varchar(50),>
           ,<COSTO_TOTALE, varchar(50),>
           ,<VALORE_PASTO, varchar(50),>
           ,<OFFLINE, varchar(50),>
           ,<PRENOTAZIONE, varchar(50),>
           ,<BRUCIATURA_DATA, varchar(50),>
           ,<BRUCIATURA_CASSA_ID, varchar(50),>
           ,<BRUCIATURA_CASSA, varchar(50),>
           ,<PRA_ANNO_ACCADEMICO, varchar(50),>
           ,<PRA_PROFILO_ID, varchar(50),>
           ,<PRA_PROFILO, varchar(50),>
           ,<PRA_CATEGORIA_ID, varchar(50),>
           ,<PRA_CATEGORIA, text,>
           ,<PRA_RICAVO_MENSA, varchar(50),>
           ,<PRA_MODALITA_ID, varchar(50),>
           ,<PRA_MODALITA, varchar(50),>
           ,<PRA_TIPO_LISTINO_ID, varchar(50),>
           ,<PRA_TIPO_LISTINO, varchar(50),>)
    GO
    '''



    tools.print_obj('', 'w', file_out)

    for row in list_in:
        row = row.replace("'", "")
        row = row.replace('"', "")
        record = row.split(field_sep)
        tools.print_obj("INSERT INTO [Erdis_Read].[dbo].[in4_consumazioni]("
                        + "[DATA_REG_EBADGE] ,[DATA_REG_CASSA] ,[PRESIDIO] ,[IDANA] ,[UTENTE_ID] ,[COGNOME] ,[NOME] ,[IDCON] ,[CONSUMAZIONE_ID] ,[STATUS] ,[TESSERA_ID] ,[IDENTIFICAZIONE_ID] ,[TIPO_PAGAMENTO_ID] ,[OPERATORE_USER] ,[TURNO_ID] ,[RISTORANTE_PRESIDIO] ,[RISTORANTE] ,[CASSA] ,[ACQUISTO] ,[TIPO_LISTINO_ID] ,[PREZZO_TOTALE] ,[COSTO_TOTALE] ,[VALORE_PASTO] ,[OFFLINE] ,[PRENOTAZIONE] ,[BRUCIATURA_DATA] ,[BRUCIATURA_CASSA_ID] ,[BRUCIATURA_CASSA] ,[PRA_ANNO_ACCADEMICO] ,[PRA_PROFILO_ID] ,[PRA_PROFILO] ,[PRA_CATEGORIA_ID] ,[PRA_CATEGORIA] ,[PRA_RICAVO_MENSA] ,[PRA_MODALITA_ID] ,[PRA_MODALITA] ,[PRA_TIPO_LISTINO_ID] ,[PRA_TIPO_LISTINO]"
                        + ") VALUES ('"
                        + record[0] + "', '" + record[1] + "', '" + record[2] + "', '"
                        + record[3] + "', '" + record[4] + "', '" + record[5] + "', '"
                        + record[6] + "', '" + record[7] + "', '" + record[8] + "', '"
                        + record[9] + "', '" + record[10] + "', '" + record[11] + "', '"
                        + record[12] + "', '" + record[13] + "', '" + record[14] + "', '"
                        + record[15] + "', '" + record[16] + "', '" + record[17] + "', '"
                        + record[18] + "', '" + record[19] + "', '" + record[20] + "', '"
                        + record[21] + "', '" + record[22] + "', '" + record[23] + "', '"
                        + record[24] + "', '" + record[25] + "', '" + record[26] + "', '"
                        + record[27] + "', '" + record[28] + "', '" + record[29] + "', '"
                        + record[30] + "', '" + record[31] + "', '" + record[32] + "', '"
                        + record[33] + "', '" + record[34] + "', '" + record[35] + "', '"
                        + record[36] + "', '" + record[37]
                        + "');",
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
    menu_in = 'data/consuma.csv'
    menu_out = 'data/consuma.sql'
   
    plates = files.filetxt_to_list(menu_in)
    list_to_file_insert(plates, menu_out)
    



