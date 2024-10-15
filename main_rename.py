import datetime
import os, shutil

if __name__ == "__main__":
    '''
    Rename all files in the directory with a list of names saved on the txt file 
    
    Requirements:
    
    1 - a directory with original files
    2 - a txt file with a list of names

    '''

    ORIGINAL_DIR = "data/files_to_rename"
    RENAMED_DIR = "data/files_renamed"
    NAMES_FILE = "data/names_for_files.txt"
    LOG_FILE = "data/log.txt"
    FILES_EXTENSION = ".xml"


    now = datetime.datetime.now()

    out_file = open(LOG_FILE, "w")

    print("Start time: ", now)
    print("Start time: ", now, file=out_file)

    out_file.close()

    with open(NAMES_FILE) as f:
        rows = f.read().splitlines()

    element_index = 0

    original_files_list = os.listdir(ORIGINAL_DIR)

    out_file = open(LOG_FILE, "a")

    print("Original files list:", original_files_list)
    print("Original files list:", original_files_list, file=out_file)

    out_file.close()

    for original_file in original_files_list:
        file_name = rows[element_index] + FILES_EXTENSION

        shutil.copyfile(ORIGINAL_DIR + "/" + original_file, 
                        RENAMED_DIR + "/" + file_name)
        
        out_file = open(LOG_FILE, "a")

        print("Copy file from:", ORIGINAL_DIR + "/" + original_file, "to:", RENAMED_DIR + "/" + file_name)
        print("Copy file from:", ORIGINAL_DIR + "/" + original_file, "to:", RENAMED_DIR + "/" + file_name, file=out_file)
        
        out_file.close()
        
        element_index += 1
