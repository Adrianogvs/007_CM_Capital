# models/pdf_model.py
import os
import re
from PyPDF2 import PdfReader
from .utils import convert_value
from config import fields  # Importe fields de config

class PDFModel:
    def __init__(self, pdf_dir, pdf_password):
        self.pdf_dir = pdf_dir
        self.pdf_password = pdf_password

    def process_pdf(self, file_path):
        data = []
        try:
            with open(file_path, 'rb') as pdf_file:
                pdf_reader = PdfReader(pdf_file)
                
                if pdf_reader.is_encrypted:
                    pdf_reader.decrypt(self.pdf_password)
                
                for page in pdf_reader.pages:
                    text = page.extract_text()
                    if not text:
                        continue

                    note_match = re.search(r'Nota(\d+)', text)
                    date_match = re.search(r'Pregão\s*(\d{2}/\d{2}/\d{4})', text)
                    
                    if note_match and date_match:
                        note = note_match.group(1)
                        date = date_match.group(1)
                        record = {"Data (Pregão)": date, "Nota": note}
                        
                        for field in fields:
                            field_pattern = fr'{re.escape(field)}\s*([\d,.]+[CD]?)'
                            field_match = re.search(field_pattern, text)
                            if field_match:
                                record[field] = convert_value(field_match.group(1))
                            else:
                                record[field] = 0.0
                        
                        data.append(record)
        except Exception as e:
            print(f"Erro ao ler o PDF '{file_path}': {e}")
        
        return data
