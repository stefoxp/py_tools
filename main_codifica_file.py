from library import files

# costanti
FILES_PATH = "data/"
FILE_INPUT = "consumazioni.csv"
FILE_LOG = "log_c.txt"
FILE_OUTPUT = "consumazioni_codificato.csv"


def main():
    print("************ Inizio elaborazione ************")

    if files.file_encoding_convert(FILES_PATH + FILE_INPUT,
                                   FILES_PATH + FILE_OUTPUT,
                                   "windows-1252",
                                   "utf-8"):
        print("************ File dati codificato ************")

if __name__ == "__main__":
    main()