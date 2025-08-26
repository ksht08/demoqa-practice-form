import os
import pytest
from pypdf import PdfReader

# pip install pypdf

TMP_DIR = os.path.join(os.path.dirname(__file__), '..', 'TMP')
PDF_FILE = "Verb_Tenses_The_Secret_to_Use_English_Tenses_like_a_Native_in_2_Weeks_for_Busy_People.pdf"
PDF_FILE_PATH = os.path.join(TMP_DIR, PDF_FILE)
PDF_FILE_PAGES = 151

def test_read_pdf_file():
    reader = PdfReader(PDF_FILE_PATH)
    print(f"\n📝 Number of pages: {len(reader.pages)}")
    assert len(reader.pages) == PDF_FILE_PAGES

    # cover_page = reader.pages[0]

    first_page = reader.pages[1].extract_text()
    print(f"\n📝 Text of the first page:\n{first_page}") # extract text from the first page
    assert "The Secret to Use English Tenses like a Native in 2" in first_page
