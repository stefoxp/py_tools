from library import cbi

def test_cbi_generate():
    path_file_in = './data/input.csv'
    path_file_out = './data/output.cbi'

    cbi.generate(path_file_in, path_file_out)