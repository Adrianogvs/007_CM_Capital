# controllers/pdf_controller.py
import os
from models.pdf_model import PDFModel
import csv
from config import fields  # Importe fields de config

class PDFController:
    def __init__(self, pdf_dir, pdf_password):
        self.pdf_model = PDFModel(pdf_dir, pdf_password)

    def extract_data(self):
        all_data = []
        for i in range(10):  # Suponha que temos 10 arquivos numerados
            if i == 0:
                file_name = 'report.pdf'
            else:
                file_name = f'report ({i}).pdf'
            
            file_path = os.path.join(self.pdf_model.pdf_dir, file_name)
            
            if os.path.exists(file_path):
                data = self.pdf_model.process_pdf(file_path)
                all_data.extend(data)
            else:
                print(f"O arquivo '{file_path}' não foi encontrado.")

        return all_data

    def save_to_csv(self, data, output_csv):
        output_dir = os.path.dirname(output_csv)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open(output_csv, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["Data (Pregão)", "Nota"] + fields)
            writer.writeheader()
            writer.writerows(data)

        print(f"Dados extraídos e salvos em '{output_csv}'")
