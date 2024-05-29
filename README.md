# Análise Financeira de Nota de Corretagem 

## Estrutura do projeto

CM Capital/</br>
├── .venv/</br>
├── controllers/</br>
│   └── pdf_controller.py</br>
├── data/</br>
│   └── output.csv</br>
├── models/</br>
│   ├── pdf_model.py</br>
│   └── utils.py</br>
├── pdf/</br>
│   ├── report.pdf</br>
│   ├── report (1).pdf</br>
│   └── report (2).pdf</br>
├── .env</br>
├── .gitignore</br>
├── config.py</br>
├── main.py</br>
└── requirements.txt</br>


# CM Capital

Este projeto é uma aplicação Python para extrair dados de relatórios em PDF da empresa CM Capital e gerar um arquivo CSV com as informações extraídas da Nota de Corretagem, a qual é envida no formato de PDF por e-mail.

## Funcionalidades

- Extrair dados de relatórios em PDF da empresa CM Capital.
- Processar os dados extraídos.
- Gerar um arquivo CSV com os dados processados.

## Estrutura do Projeto

O projeto está estruturado da seguinte forma:

- `controllers/`: Contém os controladores da aplicação.
- `data/`: Diretório para armazenar arquivos de dados gerados pela aplicação.
- `models/`: Contém os modelos da aplicação.
- `pdf/`: Diretório onde os relatórios em PDF da empresa 007 Capital são armazenados.
- `.env`: Arquivo de configuração com variáveis de ambiente, como o diretório dos relatórios em PDF e a senha de acesso.
- `config.py`: Arquivo de configuração que define os campos a serem extraídos dos relatórios em PDF.
- `main.py`: Arquivo principal que inicia a aplicação e executa o processamento dos relatórios em PDF.
- `requirements.txt`: Arquivo que lista as dependências do projeto.
- `.gitignore`: Arquivo de configuração do Git para ignorar arquivos e diretórios desnecessários.

## Como Usar

1. Clone este repositório em sua máquina local.
2. Crie um ambiente virtual Python e ative-o.
3. Instale as dependências do projeto executando `pip install -r requirements.txt`.
4. Configure as variáveis de ambiente no arquivo `.env`, especificando o diretório dos relatórios em PDF da empresa 007 Capital e a senha de acesso.
5. Execute o script `main.py` para processar os relatórios em PDF e gerar o arquivo CSV com os dados extraídos.

```bash
python main.py
```
## Passo 1: Clonar o Repositório do GitHub
Abra um terminal e execute o seguinte comando para clonar o repositório do GitHub:

```bash
git clone https://github.com/Adrianogvs/007_CM_Capital
```

## Passo 2: Navegar até o Diretório do Projeto
Navegue até o diretório recém-clonado usando o comando cd:
```bash
cd 007_CM_Capital
```

## Passo 3: Criar e Ativar o Ambiente Virtual
Crie um ambiente virtual usando o Python venv:
```bash
python -m venv .venv
```
### 3.1 Em seguida, ative o ambiente virtual:
```bash
source .venv/Scripts/activate
```

## Passo 4: Instalar as Dependências
Instale as dependências do projeto listadas no arquivo requirements.txt:

```bash
pip install -r requirements.txt
```

## Passo 5: Configurar as Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto e defina as variáveis de ambiente conforme necessário. Por exemplo:
```.env
Aqruivo .env
PDF_DIR=C:/Users/Administrador/OneDrive/Documentos/GitHub/007_CM_Capital/pdf
PDF_PASSWORD=sua_senha
```

## Passo 6: Executar o Script Principal
Agora, você pode executar o script principal para processar os relatórios em PDF:
```bash
python main.py
```
Isso irá processar os relatórios em PDF, extrair os dados e salvar em um arquivo CSV dentro do diretório data/.

## Passo 7: Executar Análises (Opcional)
Se desejar, você pode executar análises adicionais usando os Jupyter Notebooks fornecidos no projeto:

```bash
jupyter notebook analysis.ipynb
```

## Passo 8: Desativar o Ambiente Virtual (Opcional)
Quando terminar de trabalhar com o projeto, você pode desativar o ambiente virtual:

```bash
deactivate
```