import sys


def print_obj(obj, mode='a', destination=""):
    """
    scrive i record a video o nella destinazione indicata

    :param obj: una stringa o lista o altro oggetto stampabile
    :param mode: può essere 'w', 'a', o altri valori validi per i file
    :param destination: se omesso scrive a video altrimenti nel file indicato
    :return: None
    """
    if len(destination) > 0:
        # crea o svuota il file
        file_out = open(destination, mode)
        print(obj, file=file_out)
        file_out.close()
    else:
        print(obj)


def string_to_list(string, separator):
    """
    spezza una stringa in una lista

    :param string:
    :param separator:
    :return: lista dei valori contenuti nella stringa
    """
    result = string.split(separator)

    return result


def replace_string_element(original_string, substitution_list):
    """
    Sostituisce una lista di elementi all'interno della stringa originale

    :param original_string: stringa di partenza
    :param substitution_list: lista di sostituti. Ogni elemento ha la forma ('valore_attuale', 'valore_nuovo')
    :return: stringa di elementi aggiornati
    """
    result = original_string

    # for riga in originali:
    for element in substitution_list:
        # print('elemento: (', elemento[0], elemento[1], ')')
        result = result.replace(element[0], element[1])

    return result


def sostituisci_elementi_lista(originali, sostituti):
    """
    Sostituisce una lista di elementi all'interno della lista originale

    :param originali: lista di elementi di partenza
    :param sostituti: lista di sostituti. Ogni elemento ha la forma ('valore_attuale', 'valore_nuovo')
    :return: lista di elementi aggiornati
    """
    risultato = []  # ['catid', 'name']

    for valore in originali:
        for elemento in sostituti:
            if valore == elemento[0]:
                risultato.append(elemento[1])

    return risultato


def trova_in_lista(stringa, lista):
    """
    cerca una stringa all'interno di una lista

    :param stringa:
    :param lista:
    :return: 0 in caso di successo
    """
    risultato = 0

    if not(stringa in lista):
        risultato = 1

    return risultato


def prepara_sostituti(stringa_da_csv):
    risultato_list = []
    stringa_da_csv = stringa_da_csv.replace("'", "")
    stringa_da_csv = stringa_da_csv.replace(" ", "")

    preliminare_list = stringa_da_csv.splitlines()
    for elemento in preliminare_list:
        risultato_list.append(elemento.split(','))

    return risultato_list


def wrapper_piattaforma(path):
    """
    Gestisce il path in windows

    :param path:
    :return: path adattato alla piattaforma
    """
    percorso = path

    if 'win' in sys.platform:
        percorso = path.replace('/', '\\')

    return percorso