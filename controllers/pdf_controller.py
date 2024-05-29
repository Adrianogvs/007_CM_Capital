import os
import re
from models.pdf_model import PDFModel
from views.pdf_view import PDFView

class PDFController:
    def __init__(self, pdf_dir, pdf_password):
        self.pdf_dir = pdf_dir
        self.pdf_password = pdf_password
        self.model = PDFModel()
        self.view = PDFView()

    def process_pdfs(self):
        all_data = []

        # Lista todos os arquivos no diretório PDF
        for file_name in os.listdir(self.pdf_dir):
            if re.match(r'report(\s\(\d+\))?\.pdf$', file_name):
                file_path = os.path.join(self.pdf_dir, file_name)
                data = self.model.process_pdf(file_path, self.pdf_password)
                all_data.extend(data)
            else:
                self.view.display_message(f"O arquivo '{file_name}' não corresponde ao padrão esperado.")

        # Cria a pasta 'data' se não existir
        output_dir = 'data'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Escreve os dados em um arquivo CSV
        output_csv = os.path.join(output_dir, 'output.csv')
        self.model.save_to_csv(output_csv, all_data)
        self.view.display_message(f"Dados extraídos e salvos em '{output_csv}'")
