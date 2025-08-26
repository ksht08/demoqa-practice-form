import os
from zipfile import ZipFile

TMP_DIR = os.path.join(os.path.dirname(__file__), '..', 'TMP')
ZIP_FILE = "TMP_bk.zip"
ZIP_FILE_PATH = os.path.join(TMP_DIR, ZIP_FILE)
def test_zip_file_contents():
    with ZipFile(ZIP_FILE_PATH) as zip_file:
        archived_files = zip_file.namelist()
        print("\n📦 Archived files:")
        for file in archived_files:
            print(f"{file}")
        print("-------")
        assert len(archived_files) > 0, "The zip file is not empty."
        text = zip_file.read("Полезные ссылки.txt")
        print("\n📄 Content of 'Полезные ссылки.txt':")
        print(text.decode('utf-8'))

def test_extract_zip_file():
    with ZipFile(ZIP_FILE_PATH) as zip_file:
        zip_file.extract("Полезные ссылки.txt", TMP_DIR)
    assert os.path.exists(os.path.join(TMP_DIR, "Полезные ссылки.txt"))