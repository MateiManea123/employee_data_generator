import os
import zipfile


def check_and_add_to_archive(archive_path):
    print(archive_path)
    directory_path_excel = "manager_excels"
    directory_path_pdf = "employee_pdfs"
    directory_paths = list()
    directory_paths.extend([directory_path_excel,directory_path_pdf])
    if not (os.path.exists("excel.flag") and os.path.exists("pdf.flag")):
        return

    for directory_path in directory_paths:
        if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
            raise FileNotFoundError(f"This directory: '{directory_path}' does not exist")

        if not os.path.exists(archive_path):
            with zipfile.ZipFile(archive_path, 'w') as _:
                print(f"Created empty archive: {archive_path}")
        else:
            print(f"The archive already exists: {archive_path}")


        with zipfile.ZipFile(archive_path, 'a', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, os.path.dirname(directory_path))
                    if arcname not in zipf.namelist():
                        zipf.write(file_path, arcname)
                        print(f"Added: {arcname}")
                    else:
                        print(f"Already in archive: {arcname}")


        for root, dirs, files in os.walk(directory_path, topdown=False):
            for file in files:
                try:
                    os.remove(os.path.join(root, file))
                except Exception as e:
                    print(f"Error when deleting file: {file} - {e}")
            for dir in dirs:
                try:
                    os.rmdir(os.path.join(root, dir))
                except OSError:
                    pass
        if os.path.exists("excel.flag"):
            os.remove("excel.flag")
        if os.path.exists("pdf.flag"):
            os.remove("pdf.flag")