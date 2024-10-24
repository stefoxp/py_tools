import os
from pypdf import PdfWriter

def pdf_compress(path_origin: str, path_destination: str, file_log_path: str):
    file_out = open(file_log_path, "w", encoding="utf-8")
    print("Inizio elaborazione", file=file_out)
    file_out.close()

    original_files_list = os.listdir(path_origin)

    for original_file in original_files_list:
        print("original_file name:", original_file)
        
        file_out = open(file_log_path, "a", encoding="utf-8")
        print("original_file name:", original_file, file=file_out)

        writer = PdfWriter(clone_from=path_origin + original_file)

        # print("writer:", writer, file=file_out)

        '''
        for page in writer.pages:
            page.compress_content_streams(level=9)  # This is CPU intensive!

        for page in writer.pages:
            for img in page.images:
                img.replace(img.image, quality=80)
        '''

        writer.compress_identical_objects(remove_identicals=True, remove_orphans=True)

        with open(path_destination + original_file, "wb") as f:
            writer.write(f)

        file_out.close()
