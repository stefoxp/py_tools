import configparser
from library import db_odbc, files

def main():
    config = configparser.ConfigParser()
    config.read(['config.cfg', 'config.dev.cfg'])
    db_settings = config['db']

    username = db_settings['username']
    password = db_settings['password']
    db_name =  db_settings['database_name']
    db_address =  db_settings['database_address']
    
    connection = db_odbc.connect('SQL Server Native Client 11.0', db_address, db_name, username, password)
    print("********** db connected **********")

    rst_consumazioni = db_odbc.rst(connection)
    print("********** rst opened **********")

    path_file_out = 'data/consuma.sql'
    lista_consumazioni = files.filetxt_to_list(path_file_out)[2:]
    print("********** files.filetxt_to_list completed **********")
    
    conta_record = 2

    for record in lista_consumazioni:
        conta_record = conta_record + 1
        print(conta_record, "** doing INSERT **", record[680:-2])

        rst_consumazioni.exec_sql(record)
        connection.commit()

    print("********** db connection closed **********")
    connection.close()
    print("********** db connection closed **********")

if __name__ == "__main__":
    main()