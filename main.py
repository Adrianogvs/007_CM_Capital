from controllers.pdf_controller import PDFController
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

def main():
    # Recupera o caminho e a senha do arquivo .env
    pdf_dir = os.getenv('PDF_DIR')
    pdf_password = os.getenv('PDF_PASSWORD')
    
    controller = PDFController(pdf_dir, pdf_password)
    controller.process_pdfs()

if __name__ == "__main__":
    main()
