import PyPDF2

class PDFExtractor:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def extract_text(self) -> str:
        with open(self.filepath, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            return '\n'.join(page.extract_text() or '' for page in reader.pages)