# import os
from library import pdf

def main():
    PATH_ORIGIN = 'data/pdf/originali/'
    PATH_DESTINATION = 'data/pdf/compressi/'
    # PATH_TEST = 'data/pdf/test/'
    # FILE_NAME = 'mattone.pdf'
    FILE_LOG = "log.txt"

    pdf.pdf_compress(PATH_ORIGIN, PATH_DESTINATION, FILE_LOG)

if __name__ == "__main__":
    main()