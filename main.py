# main.py
import os
from dotenv import load_dotenv
from controllers.pdf_controller import PDFController

# Carrega as variáveis do arquivo .env
load_dotenv()

# Recupera o caminho e a senha do arquivo .env
pdf_dir = os.getenv('PDF_DIR')
pdf_password = os.getenv('PDF_PASSWORD')

# Instancia o controlador e extrai os dados
controller = PDFController(pdf_dir, pdf_password)
data = controller.extract_data()

# Salva os dados em um arquivo CSV
output_csv = 'data/output.csv'
controller.save_to_csv(data, output_csv)
