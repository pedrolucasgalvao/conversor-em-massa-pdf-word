# Conversor de PDF para Word

Uma aplicação web simples e elegante para converter arquivos PDF para o formato Word (.docx). Criado com Flask em Python para facilitar a vida, tornando a conversão de documentos rápida e acessível diretamente do navegador.

## Funcionalidades

-   **Interface Web:** Acesso fácil pelo navegador, sem a necessidade de instalar programas.
-   **Conversão em Lote:** Permite o upload de múltiplos arquivos PDF para conversão simultânea.
-   **Download Centralizado:** Todos os arquivos convertidos são automaticamente compactados em um único arquivo ZIP para download.
-   **Design Responsivo:** O layout se adapta bem a diferentes tamanhos de tela.

## Pré-requisitos

Para rodar este projeto localmente, você precisa ter o Python 3 instalado na sua máquina.

## Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes tecnologias:

<br>

<p align="center">
  <a href="https://www.python.org/" target="_blank">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://flask.palletsprojects.com/" target="_blank">
    <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  </a>
  <a href="https://gunicorn.org/" target="_blank">
    <img src="https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white" alt="Gunicorn">
  </a>
  <a href="https://pypi.org/project/pdf2docx/" target="_blank">
    <img src="https://img.shields.io/badge/pdf2docx-red?style=for-the-badge&logo=pypi&logoColor=white" alt="pdf2docx">
  </a>
</p>

## Instalação e Uso Local

Siga estes passos para configurar e executar a aplicação no seu computador:

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/pedrolucasgalvao/conversor-em-massa-pdf-word.git]
    ```
    (Substitua o link acima pelo link do seu repositório no GitHub)

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd SEU-REPOSITORIO
    ```
    (Substitua pelo nome da sua pasta)

3.  **Crie e ative um ambiente virtual (opcional, mas recomendado):**
    ```bash
    python -m venv venv
    # No Windows
    venv\Scripts\activate
    # No macOS e Linux
    source venv/bin/activate
    ```

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Execute a aplicação:**
    ```bash
    python app.py
    ```
    A aplicação estará rodando em `http://127.0.0.1:5000`.

## Estrutura do Projeto

A estrutura de pastas do projeto está organizada da seguinte forma:

Claro! Um arquivo README é essencial para documentar seu projeto no GitHub. Ele serve como um guia para qualquer pessoa que queira entender e usar a sua aplicação.

Aqui está um modelo completo de README que você pode copiar e colar no seu projeto. Lembre-se de criar um novo arquivo na pasta principal do projeto e nomeá-lo como README.md.

Markdown

# Conversor de PDF para Word

Uma aplicação web simples e elegante para converter arquivos PDF para o formato Word (.docx). Criado com Flask em Python para facilitar a vida, tornando a conversão de documentos rápida e acessível diretamente do navegador.

## Funcionalidades

-   **Interface Web:** Acesso fácil pelo navegador, sem a necessidade de instalar programas.
-   **Conversão em Lote:** Permite o upload de múltiplos arquivos PDF para conversão simultânea.
-   **Download Centralizado:** Todos os arquivos convertidos são automaticamente compactados em um único arquivo ZIP para download.
-   **Design Responsivo:** O layout se adapta bem a diferentes tamanhos de tela.

## Pré-requisitos

Para rodar este projeto localmente, você precisa ter o Python 3 instalado na sua máquina.

## Instalação e Uso Local

Siga estes passos para configurar e executar a aplicação no seu computador:

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
    ```
    (Substitua o link acima pelo link do seu repositório no GitHub)

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd SEU-REPOSITORIO
    ```
    (Substitua pelo nome da sua pasta)

3.  **Crie e ative um ambiente virtual (opcional, mas recomendado):**
    ```bash
    python -m venv venv
    # No Windows
    venv\Scripts\activate
    # No macOS e Linux
    source venv/bin/activate
    ```

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Execute a aplicação:**
    ```bash
    python app.py
    ```
    A aplicação estará rodando em `http://127.0.0.1:5000`.

## Estrutura do Projeto

A estrutura de pastas do projeto está organizada da seguinte forma:
```
conversor_pdf_word_web/
├── app.py
├── Procfile
├── requirements.txt
├── converted/
├── templates/
│   ├── index.html
│   └── resultado.html
└── uploads/
```

## Como Usar

1.  Acesse `http://127.0.0.1:5000` no seu navegador.
2.  Clique no botão "Escolher arquivos" e selecione um ou mais PDFs.
3.  Clique em "Converter".
4.  Após a conversão, uma página será exibida com um link para baixar um arquivo ZIP contendo todos os arquivos DOCX convertidos.

## Autor

-   Pedro Galvão
