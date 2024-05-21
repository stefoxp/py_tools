import configparser
from library import db_odbc

def main():
    config = configparser.ConfigParser()
    config.read(['config.cfg', 'config.dev.cfg'])
    db_settings = config['db']

    username = db_settings['username']
    password = db_settings['password']
    
    print("************ Collegamento al db ************")
    connection = db_odbc.connect('SQL Server Native Client 11.0', "192.168.1.91", "Erdis_Read", username, password)
    print("************ Db collegato ******************")

    print("************ rst ***************************")
    rst_consumazioni = db_odbc.rst(connection)

    print("************ SELECT *************************")
    sql = ("SELECT * FROM [Erdis_Read].[dbo].vw_in4_consumazioni_convenzionate WHERE ANNO_MESE_CONSUMAZIONE = '2023-09'")

    rst_consumazioni.read(sql)
    if rst_consumazioni.TotRec > 0:
        print("Records trovati:", rst_consumazioni.TotRec)
    '''
    print("************ INSERT *************************")
    cmd_sql = "INSERT INTO [Erdis_Read].[dbo].[in4_consumazioni]([DATA_REG_EBADGE] ,[DATA_REG_CASSA] ,[PRESIDIO] ,[IDANA] ,[UTENTE_ID] ,[COGNOME] ,[NOME] ,[IDCON] ,[CONSUMAZIONE_ID] ,[STATUS] ,[TESSERA_ID] ,[IDENTIFICAZIONE_ID] ,[TIPO_PAGAMENTO_ID] ,[OPERATORE_USER] ,[TURNO_ID] ,[RISTORANTE_PRESIDIO] ,[RISTORANTE] ,[CASSA] ,[ACQUISTO] ,[TIPO_LISTINO_ID] ,[PREZZO_TOTALE] ,[COSTO_TOTALE] ,[VALORE_PASTO] ,[OFFLINE] ,[PRENOTAZIONE] ,[BRUCIATURA_DATA] ,[BRUCIATURA_CASSA_ID] ,[BRUCIATURA_CASSA] ,[PRA_ANNO_ACCADEMICO] ,[PRA_PROFILO_ID] ,[PRA_PROFILO] ,[PRA_CATEGORIA_ID] ,[PRA_CATEGORIA] ,[PRA_RICAVO_MENSA] ,[PRA_MODALITA_ID] ,[PRA_MODALITA] ,[PRA_TIPO_LISTINO_ID] ,[PRA_TIPO_LISTINO]) VALUES ('2024-01-31 21:19:38', '2024-01-31 21:19:37', 'URBINO', '2000103657', '1000011496', 'MANNISI', 'REBECCA', '1000433503', 'd7439156-65f6-4a7f-9ea3-84ddfab8f7de', 'A', '1003772', 'AUTO', 'BOR', 'OPERATORE_1017', 'TUR02', 'URBINO', 'Mensa Tridente', 'Cassa 01', 'Pasto Completo', 'L00', '0.0', '7.51', '5.50', 'N', '', '', '', '', '2023', 'PTT', 'Tutti i ristoranti', 'F0-09', 'BORSISTI/IDONEI AS GRATUITI', 'R530.001.001', 'GG', 'Primo pasto Gratuito Secondo pasto Gratuito', 'L00', 'Listino 0');"
    rst_consumazioni.exec_sql(cmd_sql)
    connection.commit()
    '''

    print("************ close connection ***************************")
    connection.close()

if __name__ == "__main__":
    main()