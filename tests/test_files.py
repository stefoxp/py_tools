from library import files

def test_file_encoding_convert():
    path_file_in = './data/dist200015an-verificato.xml'
    path_file_out = './data/test_file_out.xml'

    assert files.file_encoding_convert(path_file_in, path_file_out,
                                       'windows-1252', 'utf-8') is True
