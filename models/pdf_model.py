import re
import csv
from PyPDF2 import PdfReader

class PDFModel:
    fields = [
        "Venda disponível", "Compra disponível", "Venda Opções", "Compra Opções", "Valor dos negócios",
        "IRRF", "IRRF Day Trade (Projeção)", "Taxa Corretora Intermediação", "Taxa Corretora",
        "Taxa registro BM&F", "Taxas BM&F (emol+f.gar)", "Outros", "I.S.S.", "Ajuste de posição",
        "Ajuste de day trade", "Total das despesas", "Outros", "IRRF Corretagem", "Total Conta Investimento",
        "Total Conta Normal", "Total líquido (#)", "Total líquido da nota"
    ]

    def convert_value(self, value):
        if value.endswith('C'):
            return float(value[:-1].replace('.', '').replace(',', '.'))
        elif value.endswith('D'):
            return -float(value[:-1].replace('.', '').replace(',', '.'))
        else:
            return float(value.replace('.', '').replace(',', '.'))

    def process_pdf(self, file_path, password):
        data = []
        try:
            with open(file_path, 'rb') as pdf_file:
                pdf_reader = PdfReader(pdf_file)
                
                if pdf_reader.is_encrypted:
                    pdf_reader.decrypt(password)
                
                for page in pdf_reader.pages:
                    text = page.extract_text()
                    if not text:
                        continue

                    note_match = re.search(r'Nota(\d+)', text)
                    date_match = re.search(r'Pregão(\d{2}/\d{2}/\d{4})', text)
                    
                    if note_match and date_match:
                        note = note_match.group(1)
                        date = date_match.group(1)
                        record = {"Data (Pregão)": date, "Nota": note}
                        
                        for field in self.fields:
                            field_pattern = fr'{re.escape(field)}([\d,\.]+[CD])'
                            field_match = re.search(field_pattern, text)
                            if field_match:
                                record[field] = self.convert_value(field_match.group(1))
                            else:
                                record[field] = 0.0
                        
                        data.append(record)
        except Exception as e:
            print(f"Erro ao ler o PDF '{file_path}': {e}")
        
        return data

    def save_to_csv(self, file_path, data):
        with open(file_path, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["Data (Pregão)", "Nota"] + self.fields)
            writer.writeheader()
            writer.writerows(data)
