def filetxt_to_list(file_in):
    """
    Read file_in.
    Return the list of records

    :return: list
    """
    list_rows = []

    try:
        with open(file_in) as f:
            list_rows = f.read().splitlines()
    except OSError as Error:
        str_msg = 'Error on csv_to_list(): ' + str(Error) + '\n'
        
        print(str_msg)

    return list_rows

def file_encoding_convert(path_from: str, path_to: str,
                          encoding_from: str, encoding_to: str = "utf-8") -> bool:
    """
    Convert file from encoding_from to encoding_to
    """
    with open(path_from, 'r', encoding=encoding_from, errors="surrogateescape") as file_in:
        content = file_in.read()

    # cleaning
    content_byte = content.encode(encoding=encoding_from, errors="surrogateescape")

    # https://www.i18nqa.com/debug/bug-double-conversion.html
    # Only characters with a second UTF-8 byte of 0x81, 0x8D, 0x8F, 0x90, 0x9D fail
    # remove byte 0x81
    content_byte = content_byte.replace(b'\x81', b'')
    # remove byte 0x8D
    content_byte = content_byte.replace(b'\x8D', b'')
    # remove byte 0x8F
    content_byte = content_byte.replace(b'\x8F', b'')
    # remove byte 0x90
    content_byte = content_byte.replace(b'\x90', b'')
    # remove byte 0x9D
    content_byte = content_byte.replace(b'\x9D', b'')

    content = content_byte.decode(encoding=encoding_from)

    # remove
    content = content.replace('”', '')
    content = content.replace('“', '')
    # content = content.replace('"', '')
    # replace
    content = content.replace("’", "'")
    content = content.replace("‘", "'")
    # content = content.replace("à", "a")
    # content = content.replace("À", "A")

    with open(path_to, 'w', encoding=encoding_to) as file_out:
        file_out.write(content)

    return True


'''
def file_clean(path_from: str, path_to: str,
                encoding_from: str = "ascii",
                encoding_to: str = "ascii") -> bool:
    with open(path_from, 'r', encoding=encoding_from, errors="surrogateescape") as f:
        data = f.read()

    # make changes to the string 'data'
    # [] remove ” and “ 
    data.replace('”', '')
    data.replace('“', '')
    # [] replace ’ with '
    data.replace("’", "'")
    # [] remove ; if overload

    with open(path_to, 'w',
            encoding=encoding_to, errors="surrogateescape") as f:
        f.write(data)

    return True
'''
